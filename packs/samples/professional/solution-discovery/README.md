# Découvrir Agentstration

Sample professionnel conçu pour démontrer une orchestration **Handoff** avec Microsoft Agent Framework.

## Équipe

- **Agent d'accueil** — reçoit la demande et introduit la conversation.
- **Conseiller solution** — répond sur les usages et l'adoption.
- **Expert technique** — répond sur l'architecture, les modèles et l'exécution locale.
- **Expert intégration** — répond sur les tools, MCP, AEP et les systèmes externes.

Le flow démarre avec l'Agent d'accueil et autorise ensuite les handoffs entre tous les spécialistes ainsi que les retours vers l'accueil. La sélection du prochain participant est gérée par l'orchestration Handoff du runtime, pas par un workflow séquentiel codé dans les prompts.

## Conversation de démonstration

Commencez par :

> Nous cherchons une solution pour faire collaborer plusieurs agents spécialisés. Est-ce qu'Agentstration peut répondre à ce besoin ?

Puis poursuivez naturellement avec :

> Certaines de nos données doivent rester entièrement sur notre infrastructure. Peut-on utiliser des modèles locaux ?

> Et si nos agents doivent utiliser nos outils internes ou appeler nos propres services ?

> Cela semble correspondre à notre besoin. Par quoi nous conseilleriez-vous de commencer ?

L'objectif est d'observer les changements de spécialiste au fil de la conversation plutôt que d'imposer une séquence fixe.

## Modèle

Le Pack déclare le binding requis `agent-model`. À l'installation, sélectionnez le Model Profile que les quatre agents doivent partager ; le Pack ne dépend d'aucun profil nommé ou namespace particulier.
