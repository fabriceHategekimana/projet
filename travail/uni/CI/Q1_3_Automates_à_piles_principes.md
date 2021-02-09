# Q1 3 Automates à piles 

Automate à piles principes

Automate disposant d'une pile
Un principe de transition définit.


Un automate à pile (non déterministe) est un 7-uplet A = ( Q , A , Z , δ , z 0 , q 0 , T ) {\displaystyle {\mathcal {A}}=(Q,A,Z,\delta ,z_{0},q_{0},T)} {\mathcal {A}}=(Q,A,Z,\delta ,z_{0},q_{0},T), où :

    Q est l'ensemble d'états ;
    A est l'alphabet d'entrée ;
    Z est l'alphabet de pile ;
    δ : Q × ( A ∪ { ε } ) × Z → P ( Q × Z ∗ ) est la fonction de transition (la notation P {\displaystyle {\mathcal {P}}} \mathcal{P} désigne l'ensemble des parties) ;
    
    z 0 ∈ Z est le symbole de fond de pile ;
    q 0 ∈ Q est l'état initial ;
    T ⊂ Q est l'ensemble des états terminaux.
    
L'automate à pile nous permet de pouvoir résoudre des problèmes du type a^nb^n
