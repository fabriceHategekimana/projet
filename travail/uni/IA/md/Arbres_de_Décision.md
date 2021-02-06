VOIR VIDÉO DU COURS

# Quel est le principe des arbres de décision ?
Nous avons un ensemble de valeurs et nous souhaitons placer des limites juste pour permettre à notre algorithme de faire une reconnaissance efficace sur des nouvelles données (on fait du clustering).

# On pourra rappeler le principe de l’apprentissage supervisé. Comment est mesuré le gain d’information ?
L'apprentissage supervisé est un type d'apprentissage où le programme se voit donnée une base d'entraînement labélisé lui permettant d'apprendre à faire des distinctions.
 
# Pourquoi peut-on utiliser l’entropie ?
Oui pourquoi?

# Comment fonctionne l’algorithme ID3 ?
• Algorithme type glouton (greedy) pour la
construction d’arbres de décision
• Utilise un critère récursif de partition basé sur le
gain d’information maximum
ID3(W)
1. Soit W les données et H(X) l’entropie de la
variable associée
2. Partitionner W= W 1 UW 2 (créer les sous-arbres)
selon la caractéristique C telle que le gain
d’information I(X;C) soit maximum
3. Soient X i les restrictions de W à W i
a. Si H(X i )>0 alors ID3(W i )
Stephane Marchand-Maillet – University of Geneva
Intelligence Artificielle
AI D

# Qu’est-ce que le sur-apprentissage ?
Je ne sais pas

# Comment le mesurer/détecter ?

# Comment l’éviter ou le contrer ?

# On pourra mentionner l’évaluation des méthodes d’apprentissage.
