Intelligence Artificielle
Biais et équité
Stephane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 1

Contenu
• Définition de l’équité
• Correspondance probabiliste
• Etudes de cas

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 3

Protection contre la discrimination
Des textes légaux:
https://www.conseil-constitutionnel.fr/le-bloc-de-constitutionnalite/declaration-des-droits-de-l-homme-et-du-citoyen-de-1789

GDPR: https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32016R0679&from=FR#d1e1874-1-1

https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2#Article9

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 4

Protected caracteristics

https://en.wikipedia.org/wiki/Protected_group

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 5

Un sujet d’importance

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 6

Une conscience technologique
Le développement de la conscience des conséquences
sociales et sociétales potentielles de la création ou de
l’utilisation d’une technologie fait partie intégrante des
programmes d’éducation visant à former les créateurs,
promoteurs ou utilisateurs de cette technologie.
C’est en particulier vrai pour l’Intelligence Artificielle qui
vise à s’intégrer au plus profond des nos processus
sociaux
(savoir,
communication,
comportement,
échanges,…)

 Besoin de développer des critères objectifs pour
maintenir un regard bienveillant mais critique envers
toute proposition
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 7

Classification équitable
Constat: L’apprentissage (classification) est par
définition un problème de discrimination (entre
classes)
 posterior: argmaxclasse P(classe|donnée)
Le problème de l’équité consiste à (inclut le fait
de) ne pas faire cette “discrimination” sur des
caractéristiques protégées
On doit éviter les biais de classification et donc
des dissymétries corrélées aux caractéristiques
protégées
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 8

Vision Bayesienne (conditionnelle)
Formulation:
• xi = [xik] ∈ X ⊆ ℝK
xi = [xiA,xiP] avec:

: Attributs des données

A = caractéristiques acceptées
P = caractéristiques protégées

• yi ∈ Y = {1 … C}
On cherche:
fq : X
xi
Stephane Marchand-Maillet – University of Geneva

: Label (classe)
Y
fq (xi) =yi
Intelligence Artificielle

AI Fairness 9

Ignorance (unawareness)
La première solution consiste simplement à ignorer les
caractéristiques protégées.
On veut:
fq (x) = fq (xA)
Le classifieur est entrainé seulement avec les caractéristiques
acceptées
Faiblesse: On ignore les corrélations entre xA et xP dans les
données. La suppression de xP n’est pas une garantie d’équité
Exemple: corrélation entre profession (xA) et genre (xP) dans
l’attribution de prêts bancaires
 Insuffisant
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 10

Parité de groupe (Group parity)
On impose équivalence du classifieur conditionné aux
caractéristiques protégées
P(fq(x),XP=xP) = P(fq(x),XP≠xP)

Exemple: La prédiction d’un engagement pour un travail
(fq(X)=oui/non) doit rester la même quelque soit le genre
(xP) de la personne
Faiblesse: On ignore les corrélations initiales entre x et y.
Si les statistiques de base sont différentes on encourage
implicitement le groupe le moins représenté
(discrimination positive)
 Peut être discutable
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 11

Egalité des chances (Equal opportunity)
On obtient l’égalité des chances si on s’assure que le taux de vrais
positifs est constant:
P(fq(x)=1,XP=xP|Y=1) = P(fq(x)=1,XP≠xP|Y=1)
Plus généralement, la parité d’erreur (accuracy parity):
P(fq(x)≠y,XP=xP) = P(fq(x)≠y,XP≠xP)
ou encore, egalité de cotes (normalized odds):
P(fq(x),XP=xP|Y) = P(fq(x),XP≠xP|Y)
Exemple: On veut engager la même proportion de genres à
compétences égales

Faiblesse: On maintient le biais des données qui lui-même a tendance
à s’aggraver (cf plus tard)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 12

Parité de prédiction (Prediction parity)
La décision réelle (Y) devient indépendante des
caractéristiques protégées sachant la prédiction:
P(Y,XP=xP|fq(x)) = P(Y,XP≠xP|fq(x))
Exemple: La décision d’embauche doit être liée à
la capacité réelle d’une personne à faire une
tâche (indépendamment de son genre)
Faiblesse: Conserve les biais initiaux qui peuvent
eux-mêmes s’aggraver
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 13

Compromis équité/performance
En biaisant la décision vers un comportement
autre que celui intrinsèque aux données, on
dégrade mécaniquement la performance
(EEntrainement et ETest)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 14

Effet d’aggravation (compounding)
Si un système préserve une dissymétrie (sociale)
dans les données, les résultats de prédiction vont
décourager la minorité qui aura tendance à se sousreprésenter… etc
Exemple: Si un algorithme d’embauche prédit
(comme il le lit dans les données) que la corrélation
“Médecin-Homme” est plus forte que “MédecinFemme” alors il aura tendance à ne recommander
que des hommes pour l’embauche sur un poste de
médecin. Ce qui diminuera d’autant le taux de
femmes dans cette profession et ainsi de suite…
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 15

Effet d’aggravation intrinsèque
L’itération de déséquilibres tend à polariser les phénomènes:
Soient a > b
Normalisation :
a/max(a,b) = 1
b/max(a,b)<1
Itération:
an=1
bn  0

a0
a1
…
an
0b

n

…

b1

b01 c0

…

cn

+∞

C’est ce qui se passe implicitement dans beaucoup
d’algorithmes itératifs
• Exagération des caractéristiques dominantes
• Polarisation des limites
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 16

Biais dans les recrutements
Setup: Résumés (bios) collectés sur le Web
(eg Wikipedia)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

Bias in Bios: A Case Study of Semantic
Representation Bias in a High-Stakes
Setting. Maria De-Arteaga, Alexey
Romanov, Hanna Wallach, Jennifer
Chayes, Christian Borgs, Alexandra
Chouldechova, Sahin Geyik, Krishnaram
Kenthapadi, Adam Tauman Kalai. CoRR
abs/arXiv:1901.09451, 2019

AI Fairness 17

Biais dans les recrutements
Setup: Association bio-profession par Word
Embeddings (type GloVe)
On constate des biais dans ces représentations:

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 18

Parenthèse: causalité dans les séquences
Exemple: texte
Les mots ne sont pas equiprobables
– Give me a word
– Give me the next word
• I am a ….  “man”, “woman”, “teacher” / “car” is
unlikely

– Give me the missing word
• The sun is … today  “shinning”, “hiding” /
“running” is unlikely

Cette causalité peut être apprise
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 19

Word Embedding
Idée principale: apprend un vecteur par mot
fq(wi)=vi

Le vecteur est une représentation du contexte dans
lequel le mot est utilisé
Illustration: vecteur vi = probabilités d’occurrence
de chaque mot comme voisin de ce mot wi
On crée une géométrie grâce à ces vecteurs
«King» – «Male» ~ dominant
dominant + “Female” = “Queen”
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 20

Modèle Word2Vec
Word from context

Context from word

Continuous BoW

Ideas combined into the Glo(bal)Ve(ctors) idea (GloVe)

Picture from Landthaler, Joerg & Waltl, Bernhard & Huth, Dominik & Braun, Daniel & Matthes, Florian & Stocker, Christoph & Geiger, Thomas. (2017).
Extending Thesauri Using Word Embeddings and the Intersection Method.

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 21

Géométrie de la sémantique

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 22

… pour des concepts divers
Superlatives

“CEO of”

(Fin de la parenthèse)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 23

Biais dans les recrutements
https://www.youtube.com/watch?v=IDNXZitcQng

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 24

Biais dans les recrutements

Bias in hiring

Bias in Bios: A Case Study of Semantic
Representation Bias in a High-Stakes Setting. Maria
De-Arteaga, Alexey Romanov, Hanna Wallach,
Jennifer Chayes, Christian Borgs, Alexandra
Chouldechova, Sahin Geyik, Krishnaram
Kenthapadi, Adam Tauman Kalai. CoRR
abs/arXiv:1901.09451, 2019

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 25

On doit trouver des voies d’améliorations

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 26

Un sujet d’importance

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 27

https://fatconference.org/

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 28

Résumé
• L’équité (fairness) est un objectif important dans le développement
d’un technologie
• C’est un sujet qui doit faire partie intégrante de la conception de la
technologie
– Pas un correctif

• La définition de l’équité comporte beaucoup de facettes souvent
contradictoire
– Exemple: paradoxe de Simpson

• Son implémentation peut être liée à la notion d’indépendance
probabiliste
• Les effets d’aggravation peuvent être inhérents aux algorithmes
(exemple: par polarisation), pas seulement aux données
• L’équité est en lien avec l’éthique mais n’est en pas la seule
composante (voir Techno-Ethics)
 La recherche a beaucoup de progrès à faire sur le sujet
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 29

Quelques references
• Tolga Bolukbasi,Kai-Wei Chang,James Zou,Venkatesh Saligrama,Adam
Kalai. Man is to Computer Programmer as Woman is to Homemaker?
Debiasing Word Embeddings, ArXiv 1607.06520, 2016
• Solon Barocas, Andrew D. Selbst. Big Data’s Disparate Impact. 104
CALIF.Law REV.671(2016). DOI: http://dx.doi.org/10.15779/Z38BG31
• Pratik Gajane, Mykola Pechenizkiy. On Formalizing Fairness in Prediction
with Machine Learning. ArXiv 1710.03184, 2017
• Sahil Verma, Julia Rubin. Fairness Definitions Explained. 2018 ACM/IEEE
International Workshop on Software Fairness
• L. Hu, Y Chen. A Short-term Intervention for Long-termFairness in the
Labor Market. ArXiv 1712.00064, 2017
• Michael P. Kim,Omer Reingold, Guy N. Rothblum. Fairness Through
Computationally-Bounded Awareness. arXiv 1803.03239, 2018
• Alexandra Chouldechova. Fair prediction with disparate impact:A study of
bias in recidivism prediction instruments. ArXiv 1610.07524, 2016
• Richard Zemel, Yu Wu, Kevin Swersky, Toniann Pitassi, Learning Fair
Representations. ICML 2013.
• Muhammad Bilal Zafar, Isabel Valera, Manuel Gomez Rodriguez, Krishna P.
Gummadi. Fairness Constraints: Mechanisms for Fair Classification.
AISTATS 2017.
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 30

Liens
Videos:
• Bias in bios: fairness in a high-stakes machinelearning setting
• CNBC report: https://www.youtube.com/watch?v=ZMsSc_utZ40
• Demo interactive:
• Techno-ethics: https://en.wikipedia.org/wiki/Ethics_of_technology
https://www.youtube.com/watch?v=IDNXZitcQng (ArXiv 1901.09451, 2019)

http://research.google.com/bigpicture/attacking-discrimination-in-ml/

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Fairness 31

