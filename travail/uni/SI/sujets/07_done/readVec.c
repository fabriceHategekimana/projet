#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

double * loadSingle (int fd , int *length ) {
    double *v; //on prépare le vecteur d'accueil
    int l; //on prépare la longeur d'accueil
    read(fd , length , sizeof(int)); //on enregistre la longeur dans length
    l = (*length) * sizeof(double); //l contient la taille en bytes du vecteurs
    v = (double *) malloc (l); //on alloue cet espace pour v
    read( fd , v, l ); //v capture la valeur du vecteur
    return v;
}

int load(int n, double ***vecs , int **lengths , char *fname) {
    int fd = open(fname, O_RDONLY); //on ouvre le fichier en lecture seul
    int iVec = 0; //compteur

    *vecs = calloc(n, sizeof(double*)); //alloue de la mémoire pour n vecteurs
    *lengths = calloc(n, sizeof(int)); //alloue de la mémoire pour n longeurs

    for(iVec=0; iVec < n; iVec++){
	(*vecs)[iVec] = loadSingle(fd , &((* lengths)[iVec]));
    }

    close(fd);
    return 1;
}

int main(int argc , char** argv) {
    double** vecs; //on défini le tableau de vecteur
    int* lengths; //on défini un tableau de longueur
    int iVec; //compteur
    load(3, &vecs , &lengths , "vec.dat"); //on charge 3 vecteurs
    for(iVec = 0; iVec < 3; iVec ++) { //pour chaque vecteur du tableau
	int i;
	for(i = 0; i < lengths[iVec]; i++) {
	    printf ("%f ", vecs[iVec][i] ); //on affiche chaque élément du vecteur
	}
	printf ("\n"); //saut de ligne
    }
    exit( EXIT_SUCCESS );
}
