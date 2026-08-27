# Découvrir Agentstration

Sample professionnel conçu pour démontrer une orchestration **Handoff** avec Microsoft Agent Framework.

## Équipe

- **Agent d'accueil** — reçoit la demande et introduit la conversation.
- **Conseiller solution** — répond sur les usages et l'adoption.
- **Expert technique** — répond sur l'architecture, les modèles et l'exécution locale.
- **Expert intégration** — répond sur les tools, MCP, AEP et les systèmes externes.

Le flow déclare les participants et les routes de handoff autorisées. La sélection du prochain participant est gérée par l'orchestration Handoff du runtime, pas par un workflow séquentiel codé dans les prompts.

## Conversation de démonstration

Commencez par :

> Nous cherchons une solution pour faire collaborer plusieurs agents spécialisés. Est-ce qu'Agentstration peut répondre à ce besoin ?

Puis poursuivez naturellement avec :

> Certaines de nos données doivent rester entièrement sur notre infrastructure. Peut-on utiliser des modèles locaux ?

> Et si nos agents doivent utiliser nos outils internes ou appeler nos propres services ?

> Cela semble correspondre à notre besoin. Par quoi nous conseilleriez-vous de commencer ?

L'objectif est d'observer les changements de spécialiste au fil de la conversation plutôt que d'imposer une séquence fixe.

## Modèle

Le sample utilise `default/reasoning-default`, conformément aux autres packs de démonstration. Adaptez le Model Profile dans Agentstration si nécessaire avant l'exécution.
