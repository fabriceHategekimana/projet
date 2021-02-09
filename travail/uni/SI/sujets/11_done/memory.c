#include <errno .h>
#include <sys/time.h>
#include <sys/ resource .h>
#include <sys/mman.h>
#include <unistd .h>
#include <stdio .h>
#include <stdlib .h>
#include <string .h>

# define DATA " DonneesPriveesSensibles "
# define GIGA 1073741824 L // nombre d’octets dans 1 Go
# define MAXDATASIZE(7*GIGA) // Taille de la memoire de la machine ou est exectue ce programme

void exit_err( const char* str)
{
    perror(str);
    exit( EXIT_FAILURE );
}

int main(int argc , char* argv [])
{
    struct rlimit myLimits ; //création de la structure pour connaître la limite de la ressource du processus
    struct rusage myUsage ; //création de la structure pour connaître le coût d'un programme
    char *ptr; //pointeur
    long int i; //compteur
    int lock = 0; //verrou binaire

    //on active le lock si on entre l'argument "lock"
    if(( argc > 1) && ( strcmp ("lock", argv [1]) == 0)) 
	lock = 1;

    myLimits.rlim_cur = RLIM_INFINITY ; //on définit la softlimit à une valeur infinie
    myLimits.rlim_max = RLIM_INFINITY ; //on définit la hardlimit à une valeur infinie

    //Prépare la place maximale possible de la RAM
    if( setrlimit( RLIMIT_MEMLOCK , &myLimits ) == -1) //envoie une erreur si on y parvient pas
	exit_err(" Impossible de regler la limite RLIMIT_MEMLOCK ");
    
    //set le userid du processus appellant (c'est pourquoi il est important d'être root)
    if( setuid( getuid ()) == -1) //envoie une erreur si ça marche pas
	exit_err(" Impossible de regler l’uid");
    
    //si le lock est activé, alors on lock toute la mémoire virtuelle du processus appelant dans la RAM 
    if(lock) { //on a une erreur si cela n'est pas possible
	if( mlockall( MCL_FUTURE ) == -1) //Future= toute la mémoire en plus que le processus va créer sera dans la RAM (Je suis pas sûr ici)
	    exit_err(" Impossible de bloquer la memoire ");
	printf(" Memory locked \n");
    }

    //on alloue une partie de mémoire de 7Go
    if(( ptr = malloc( MAXDATASIZE )) == NULL)
	exit_err(" Impossible d’allouer de la memoire ");

    // Initialisation des donnees: on met 0 dans chaque cellule
    for(i=0;i < MAXDATASIZE ; i++)
	*( ptr+i) = 0;

    // Placement des donnees en memoire: on met la chaine "données privées sensibles" dans chaque cellule
    for(i=0;i < MAXDATASIZE ; i+= sizeof(DATA))
	strcpy(ptr+i, DATA);
    
    //on récupère les statistics d'utilisation du processus appelant(dans myUsage)
    if( getrusage( RUSAGE_SELF , &myUsage ) == -1) //renvoie une erreur si on y parvient pas
	exit_err(" Impossible de lire les usages du processus ");

    //ru_majflt=  les défauts de page nécessitant des entrées/sorties physiques
    printf(" Number de defauts de pages majeurs : %ld\n", myUsage.ru_majflt );

    //on fini par soulager la RAM(si on a utilisé lock)
    if(lock)
	if( munlockall() == -1)
	    exit_err(" Impossible de debloquer la memoire ");
    return 0;
}
