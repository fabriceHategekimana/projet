Assistante: Frantzeska.Lavda@etu.unige.ch
Attention: algorithm from scratch

Supervised learning:

	- density estimation
	- linear methode
	- non-linear methode
	- regulation

Evaluation and experimentation of the constructed pipeline

Dimensionallty reduction methode

python scikit-Learn and Tensorflow

Supervised learning
(classification, regression)
ground truth => y

Model
- features to describe leraning instances
- - collect training data
- Apply a learning algorithm
- carefully evaluate the model performance (no model is perfect , especially right away)

Generative models
- dataset x -[learn]-> density function P(x)
- P(x) -> sample, generate sample

**Vocabulary**
vector of d variable/atribute
table of n lines and d columns

a model is a high-level description, summarizing a large collection of data describing its important features. Often a model is global in the sense that it applies to all point...

A pattern is a local description, applying to some subset of the data space, perhaps showing how just a few data points behave or characterizing some persistent but unusual...


# Data mining
Overfitting arrive quand on a pas assez de donnée.
quand on entraîne un système avec peu de donnée d'entrainement.
S'évite avec la régularisation, Priors ou la méthode Baésienne.

3 type d'algorithme:
- generative (make statement with p(x,y)) bcp de maht quand on a la distribe, on peut générer des datas qui lui ressemble.
- discriminative (P(y|x)) pour des cas plus simple sans estimation
- (f(x)->y)
- 

![bayes_theorem](images/bayes_theorem.png)
![bayes_theorem2](images/bayes_theorem2.png)

# Kernel density function
Si on a plusieur paramètres, on les traite de façon indépendante s3p20 (ou 19)

upper bounded définition

# Linear Regression
Deux approches:
- geometrique
- probabilistique

Régularization
![gradient](images/gradient.png)
When this gradient is null, we can have the response
