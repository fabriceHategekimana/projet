Dashboard
=========

## description:
crée la fenêtre principale.
Elle est composée de:
1. une colonne de N avec l'identifiant de chaque chantier
2. une table de Nx52 pour colorier les dates de chantier
3. une ligne de 52 pour noter les dates de chantier (mois)
4. un calendrier pour afficher les dates de livraison

## génération
1. get_colonne_chantier(annee)
2. compute_planning(annee)
3. compute_date_chantier(annee)
4. get_calendar(annee)
remarque: l'année pourrai être une variable globale


## actions possibles

[chantier](chantier)
[livraison](livraison)
