Lire attentivement les deux programmes suivants permettant de lire et d’écrire une
liste de vecteurs de longueur variable:

## 1. Décrivez en détail le code et son fonctionement.
Fait sur le code (il n'est pas très compliqué, le prof a dû manquer d'idée).

## 2. Pour lire les vecteurs, il faut connaître à l’avance le nombre de vecteurs à lire.  Comment faire pour lire tous les vecteurs présents, sans en connaître le nombre à l’avance ? (vous pouvez changer le format)
En partant du principe que le fichier donnée respecte une bonne structure. On peut developper une fonction qui lit tout les saut de ligne. Donc si N est le nombre de saut de ligne trouvé dans le fichier, on sait qu'on a (N+1)/2 vecteurs à extraire.

## 3. Comment faire pour ne lire qu’un seul vecteur (par exemple le troisième de la liste) ? Présentez une solution en pseudo-code qui ne nécéssite pas un changement de format. Indiquez les appels systèmes et fonctions employées.
Une solution triviale serai d'afficher seulement le vecteur dont on a besoin

```c
int main(int argc , char** argv) {
    double** vecs; //on défini le tableau de vecteur
    int* lengths; //on défini un tableau de longueur
    int iVec; //compteur
    load(3, &vecs , &lengths , "vec.dat"); //on charge 3 vecteurs
    for(iVec = 0; iVec < 3; iVec ++) { //pour chaque vecteur du tableau
	int i;
	for(i = 0; i < lengths[iVec]; i++) {
	    if(i+1 == lengths[iVec]){
		printf("%f ", vecs[iVec][i] ); //on affiche chaque élément du vecteur
	    }
	}
	printf ("\n"); //saut de ligne
    }
    exit( EXIT_SUCCESS );
}
```
