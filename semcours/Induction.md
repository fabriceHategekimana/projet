## Induction mathématique
Selon les notions mathématique qu'on connait et avec la notion d'induction.

## Induction structurelle
S'applique à des structures (liste, opérations, ensembles) avec la notion d'induction.
    
      
## Jugement  
Premisse | conclusion
  
Déduction:  
	Série d'application de règles de définition inductives

## État d'un système  
Composé de termes typables (l'arité définit sur des noms de types S)
* S: ensemble des types définis sur les termes
* OP: ensemble des opérations
* mu: arité (profil) d'un type mu: OP->S*xS
  
Définitions Ch4.pdf
## Système de transition:  
se fait de State à State  
pour tou x et y appartenant à state la transition va de x à y
x -> y
  
## Système de transition avec context:  
Comme le système de transition mais la relation se fait avec le context
c|- x -> y
Par exemple, un context peut être une substitution de variables.
  
## Système de transition avec label  
Comme le système de transition mais la relation se fait avec un label au milieu  
   l
x -> y
Par exemple, un label peut être un évènement ou une action.
