from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "packs"
AUDIENCES = {"personal", "professional", "universal"}
PURPOSES = {"sample", "template", "standard"}
PURPOSE_COLLECTIONS = {"sample": "samples", "template": "templates", "standard": "standard"}
SUPPORTED_KINDS = {"ModelProvider", "RuntimeProfile", "ModelProfile", "Agent", "Flow", "Entry"}
NAME = re.compile(r"^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def load_yaml(path: Path, errors: list[str]) -> dict:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, path, f"invalid YAML: {exc}")
        return {}
    if not isinstance(value, dict):
        fail(errors, path, "document root must be an object")
        return {}
    return value


def validate_pack(pack_file: Path, errors: list[str]) -> None:
    root = pack_file.parent
    manifest = load_yaml(pack_file, errors)
    metadata = manifest.get("metadata") or {}
    definition = manifest.get("definition") or {}
    audience = metadata.get("audience")
    purpose = metadata.get("purpose")
    name = metadata.get("name")
    publisher = metadata.get("publisher")
    version = metadata.get("version")

    if manifest.get("apiVersion") != "agentstration.io/v1":
        fail(errors, pack_file, "apiVersion must be agentstration.io/v1")
    if manifest.get("kind") != "Pack":
        fail(errors, pack_file, "kind must be Pack")
    if "spec" in manifest:
        fail(errors, pack_file, "legacy Pack 'spec' envelope is unsupported; use 'definition'")
    if not isinstance(manifest.get("definition"), dict):
        fail(errors, pack_file, "definition is required and must be an object")
    if audience not in AUDIENCES:
        fail(errors, pack_file, "metadata.audience must be personal, professional, or universal")
    if root.parent.name != audience:
        fail(errors, pack_file, "directory collection must match metadata.audience")
    if purpose not in PURPOSES:
        fail(errors, pack_file, "metadata.purpose must be sample, template, or standard")
    if purpose in PURPOSE_COLLECTIONS and root.parent.parent.name != PURPOSE_COLLECTIONS[purpose]:
        fail(errors, pack_file, "directory purpose collection must match metadata.purpose")
    if root.name != name:
        fail(errors, pack_file, "directory name must match metadata.name")
    if not isinstance(name, str) or not NAME.fullmatch(name):
        fail(errors, pack_file, "metadata.name must be lowercase kebab-case")
    if not isinstance(publisher, str) or not NAME.fullmatch(publisher):
        fail(errors, pack_file, "metadata.publisher must be lowercase kebab-case")
    if not isinstance(version, str) or not SEMVER.fullmatch(version):
        fail(errors, pack_file, "metadata.version must use Semantic Versioning")
    if definition.get("requirements"):
        fail(errors, pack_file, "requirements are unsupported by Pack V1")
    for required in ("README.md", "CHANGELOG.md"):
        if not (root / required).is_file():
            fail(errors, pack_file, f"{required} is required")

    resources = definition.get("resources")
    if not isinstance(resources, list) or not resources:
        fail(errors, pack_file, "definition.resources must be a non-empty list")
        return
    if len(resources) != len(set(resources)):
        fail(errors, pack_file, "definition.resources contains duplicate paths")

    documents: list[tuple[str, str, str, dict]] = []
    identities: set[tuple[str, str]] = set()
    for relative in resources:
        if not isinstance(relative, str):
            fail(errors, pack_file, "resource paths must be strings")
            continue
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts:
            fail(errors, pack_file, f"unsafe resource path: {relative}")
            continue
        path = root / candidate
        if not path.is_file():
            fail(errors, pack_file, f"missing resource: {relative}")
            continue
        document = load_yaml(path, errors)
        kind = document.get("kind")
        resource_metadata = document.get("metadata") or {}
        resource_name = resource_metadata.get("name")
        if document.get("apiVersion") != "agentstration.io/v1":
            fail(errors, path, "apiVersion must be agentstration.io/v1")
        if kind not in SUPPORTED_KINDS:
            fail(errors, path, f"unsupported resource kind: {kind}")
        if not isinstance(resource_name, str) or not NAME.fullmatch(resource_name):
            fail(errors, path, "metadata.name must be lowercase kebab-case")
        if "definition" not in document:
            fail(errors, path, "definition is required")
        identity = (str(kind), str(resource_name))
        if identity in identities:
            fail(errors, path, f"duplicate resource identity: {kind}/{resource_name}")
        identities.add(identity)
        documents.append((relative, str(kind), str(resource_name), document))

    agent_names = {name for _, kind, name, _ in documents if kind == "Agent"}
    flow_names = {name for _, kind, name, _ in documents if kind == "Flow"}
    for relative, kind, resource_name, document in documents:
        path = root / relative
        definition = document.get("definition") or {}
        if kind == "Flow":
            flow_spec = definition.get("spec") or {}
            if flow_spec.get("flowKind") != "orchestration":
                fail(errors, path, "official orchestration samples must use flowKind: orchestration")
                continue
            participants = flow_spec.get("participants") or []
            participant_names = [item.get("id") for item in participants if isinstance(item, dict)]
            if len(participant_names) < 2 or len(participant_names) != len(set(participant_names)):
                fail(errors, path, "orchestration requires at least two distinct participants")
            unknown = sorted(set(participant_names) - agent_names)
            if unknown:
                fail(errors, path, f"unknown participant agents: {', '.join(unknown)}")
            pattern = flow_spec.get("pattern") or {}
            strategy = pattern.get("strategy")
            if strategy not in {"sequential", "concurrent", "handoff", "groupChat", "magentic"}:
                fail(errors, path, f"unsupported orchestration strategy: {strategy}")
            if strategy == "handoff":
                initial = pattern.get("initialParticipant")
                routes = pattern.get("handoffs") or []
                if initial not in participant_names:
                    fail(errors, path, "handoff initialParticipant must be a participant")
                reachable = {initial}
                changed = True
                while changed:
                    changed = False
                    for route in routes:
                        if not isinstance(route, dict):
                            continue
                        source, target = route.get("from"), route.get("to")
                        if source in reachable and target not in reachable:
                            reachable.add(target)
                            changed = True
                if set(participant_names) - reachable:
                    fail(errors, path, "every handoff participant must be reachable")
            if strategy == "groupChat" and not 1 <= int(pattern.get("maximumIterations", 0)) <= 100:
                fail(errors, path, "groupChat maximumIterations must be between 1 and 100")
            if strategy == "magentic":
                manager = pattern.get("manager") or {}
                manager_name = manager.get("id")
                if manager_name not in agent_names:
                    fail(errors, path, "magentic manager must reference a contained Agent")
                if manager_name in participant_names:
                    fail(errors, path, "magentic manager must be distinct from participants")
        elif kind == "Entry":
            binding = definition.get("binding") or {}
            if binding.get("kind") != "flow" or binding.get("resourceId") not in flow_names:
                fail(errors, path, "Entry must bind to a contained Flow")

    declared = set(resources)
    actual = {
        str(path.relative_to(root)).replace("\\", "/")
        for path in root.rglob("*.yaml")
        if path.name != "pack.yaml"
    }
    if declared != actual:
        missing = sorted(actual - declared)
        extra = sorted(declared - actual)
        if missing:
            fail(errors, pack_file, f"YAML resources not declared: {', '.join(missing)}")
        if extra:
            fail(errors, pack_file, f"declared paths are not YAML resources: {', '.join(extra)}")


def main() -> int:
    errors: list[str] = []
    pack_files = sorted(PACKS.glob("*/*/*/pack.yaml"))
    if not pack_files:
        errors.append("no Packs found")
    for pack_file in pack_files:
        validate_pack(pack_file, errors)
    forbidden = sorted(path for path in ROOT.rglob("*.zip") if ".git" not in path.parts)
    for path in forbidden:
        fail(errors, path, "generated ZIP archives must not be committed")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(pack_files)} Packs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
