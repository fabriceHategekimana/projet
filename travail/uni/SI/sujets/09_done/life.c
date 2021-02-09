#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sched.h>

#define NB_LIGNES 10
#define NB_COLS 10
#define MEM_NAME "/ plateau "

void exit_err( const char* str) {
    perror(str);
    exit( EXIT_FAILURE );
}

char val_tab( const char*plateau , int x , int y) {
    return plateau [NB_COLS *x + y];
}

/* Cette fonction affiche le plateau toujours au meme
   endroit sur l’ecran , vous n’aurez pas de question sur
   cette fonction */
void affiche_plateau(const char* plateau) {
    int i,j; //ligne, colonnes
    for(i=0;i < NB_LIGNES ; i++)
	for(j=0;j < NB_COLS ; j++)
	    //affiche d'une couleur/valeur spéciale chaque élément du tableau (0 ou 1 avec un formatage spécial)
	    printf(" \033[%d;%dH%d", i+1, j+1, val_tab(plateau , i, j));
}

int compte(char* plateau , int x, int y)
{
    int i,j, cpt= 0; //on introduit ligne, colonne, compteur
    for(i= -1; i < 2 ;i++)
	for(j= -1; j < 2; j++)
		//on somme la valeur de tous les voisin de la cellule qui sont dans le tableau (on ne dépasse pas les bords)
	    if( !((i == 0) && (j == 0)) && (x+i >= 0) && (y+j >= 0) && ( x+i < NB_LIGNES ) && (y+i < NB_COLS ))
			cpt += val_tab(plateau, x+i, y+j);
    return cpt;
}
	    
void cellule(char* plateau , int x, int y) {
    char *cell = ( plateau + NB_COLS *x + y );//on sélectionne la cellule en question (son adresse)
    // % -> modulo( reste de la division )
    *cell = getpid() % 2; //on lui attribut une valeur  (0 si pair, 1 si impaire)

    while(1) {
	int cpt = compte(plateau , x, y); //la somme de tout les voisins de la cellule
	if(* cell > 0) { //si la cellule vaut plus que zéro (=1)
	    if( (cpt < 2) || (cpt > 3) ) //2. Une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt.
		*cell = 0; //la cellule reste à zéro
	}
	else if(cpt == 3) //1. Une cellule morte possédant exactement trois voisines vivantes devient vivante (elle naît).
	    *cell = 1;
	sched_yield(); //le thread s'arrête pour laisser un nouveau thread se lancer
    }
    exit( EXIT_SUCCESS ); //on quitte
}

int main() {
    char * plateau ; //pointeur plateau
    int fd_mem ; //fichier mémoire qui sera partagé
    size_t mem_size = NB_LIGNES * NB_COLS * sizeof(char); //tableau de taille 10x10 (char)
    fd_mem = shm_open(MEM_NAME , O_RDWR | O_CREAT | O_EXCL , 0600) ; //crée/accède une mémoire partagée entre processeurs

    if(fd_mem == -1) //erreur si l'allocation n'a pas marché
	exit_err("main , shm_open ");

    shm_unlink(MEM_NAME); //ferme la mémoire précédemment créée

    if(ftruncate(fd_mem , mem_size ) == -1) //tronc la mémoire à la taille 10x10
	exit_err("main , ftruncate ");

    plateau = (char *) mmap(NULL , mem_size , PROT_READ | PROT_WRITE , MAP_SHARED , fd_mem , 0); //map l'adresse du tableau dans la variable plateau

    if( plateau == MAP_FAILED ) //erreur si le mappage a échoué
	exit_err("main , mmap");

    close(fd_mem); //on ferme le fichier mémoire

    // Le code commente ci - dessous est en lien avec une des question ci - dessus
	/*
	   struct sched_param sp;
	   sp.sched_priority = 1;
	   sched_setscheduler( getpid() , SCHED_FIFO , &sp);
	   */
    int i, j; //on définit les lignes et colonnes
    for(i=0; i < NB_LIGNES ; i++){
	for(j=0;j < NB_COLS ; j++){
	    pid_t res = fork(); //on créer 10x10 processus (une pour chaque cellule)
	    if(res == -1)//erreur si le fork échoue
		exit_err("main , fork");
	    else if(res == 0)// chaque processus exécute la méthode cellule
		cellule(plateau , i, j); //chaque cellule respecte les règles du jeu de la vie
	}
    }

    while(1) //le processus parent affiche l'état du plateau en direct
	affiche_plateau(plateau);

    if( munmap(plateau , mem_size ) == -1) //quand on a fini, on supprime l'adresse mémoire
	exit_err("main , munmap ");

    return 0;
}
