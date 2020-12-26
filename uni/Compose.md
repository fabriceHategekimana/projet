Compose Pattern

Problème:

part-whole hierarchie?

Crée un arbre et fait exécuter des éléments dans les nodes.
C'est comm si on manipule une un groupe d'objet avec une seule instance seulement.

4 membres:
1. Component: L'interface qui défini le protocole de comunication
2. Leaf: définit le comportement des enfants (les plus bas)
3. Composite: Contient les enfants et fait des actions en rapport avec eux.
4. Client: manipule les objet de la composition par le biais de l'interface

On peut donc définir une action sur le parent et l'action va être reproduite par les enfants.

![composite_design_pattern](../../images/composite_design_pattern.png)
