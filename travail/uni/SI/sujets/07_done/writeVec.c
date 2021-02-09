#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int storeSingle(double *vec , int length , int fd) {
    write(fd, (char *) &length , sizeof (int)); //on écrit la longeur du vecteur
    write(fd, (char *) vec , length * sizeof(double)); // on écrit le contenu du vecteur
    return 1;
}

int store(double **vec , int *lengths , int n, char * fname) {
    int fd = open( fname , O_WRONLY | O_CREAT | O_TRUNC , S_IRUSR | S_IWUSR); //on crée un fichier
    int iVec = 0; //un compteur
    for( iVec =0; iVec < n; iVec ++) {
	storeSingle(vec[iVec], lengths[iVec], fd); //on enregistre chaque vecteur dans le fichier
    }

    close (fd);
    return 1;
}

int main( int argc , char ** argv) {
    int lengths[] = { 2, 8, 5 }; //on défini un tableau de trois longueurs
    double v1[] = {0.1 , 0.5}; //vecteur 1
    double v2[] = {1.0 , 2, 3, 4, 5, 6, 7, 8}; //vecteur 2
    double v3[] = { -100.0 , -10, 1, 10, 100}; //vecteur 3
    double *vecs[3]; //un pointeurs de vecteur
    vecs[0] = v1; //vecteur 1 dans le tableau
    vecs[1] = v2; //vecteur 2 dans le tableau
    vecs[2] = v3; //vecteur 3 dans le tableau
    store(vecs , lengths , 3, "vec.dat"); //on enregistre les vecteurs dans le ficher vec.dat
    exit(EXIT_SUCCESS);
}

