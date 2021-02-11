#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>          //Ajouté par rapport au code initial
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int handle(char *name) {
    ssize_t nread, nwrit;   /*Déclarations et initialisations*/
    int fifo = -1;
    long buffer = 0;

    int result = mkfifo( name, 0600 );          /*On utilise la fonction "mkfifo" avec en paramètres le nom du fifo à créer et le mode (modifié avec umask)
                                                Le mode 0600 correspond à lecture/écriture pour l'utilisateur, et rien pour le groupe et les autres*/

    if( result < 0 ) {                          //"mkfifo" retourne 0 en cas de succès et -1 en cas d'erreur
        perror( "Cannot create the fifo" );     //On affiche le message d'erreur système. A noter que "perror" utilise errno pour afficher l'erreur correspondante
        exit( EXIT_FAILURE );                   //On quitte le programme
    }

    fifo = open( name, O_RDWR );                //On ouvre le fifo en lecture écriture avec "open" et on obtient un descripteur de fichier (entier)

    if( fifo < 0 ) {                            //On vérifie si le descripteur de fichier est valide
        perror( "Cannot open the fifo" );       //On affiche le message d'erreur système
        exit( EXIT_FAILURE );                   //On quitte le programme
    }

    buffer *= 2;                                //On multiplie "buffer" par 2

    nwrit = write( fifo, &buffer, sizeof buffer );  //On écrit sur le fifo avec l'appel système "write" ("write" écrit les données en binaire)
    if ( nwrit < 0 ) {                              //L'appel "write" retourne -1 en cas d'erreur donc on vérifie (cf. man 2 write)
        perror( "Transmission failure" );           //On affiche le message d'erreur système pour indiquer qu'il y a une erreur à l'écriture
        exit( EXIT_FAILURE );                       //On quitte le programme
    }

    nread = read( fifo, &buffer, sizeof buffer );   //On lit sur le fifo avec l'appel système "read"
    if ( nread < 0 ) {                              //L'appel "read" retourne -1 en cas d'erreur donc on vérifie (cf. man 2 read)
        perror( "Reception failure" );              //On affiche le message d'erreur système pour indiquer qu'il y a une erreur à la lecture
        exit( EXIT_FAILURE );                       //On quitte le programme
    }

    unlink(name);           //Ajouté pour supprimer le fifo à la fin de l'exécution du programme
    return (int) buffer;    //Ajouté par rapport au code initial pour respecter le type de retour de la fonction
}

/* Fonction main juste pour tester que le programme fonctionne et ne bloque pas. Ex: ./fifo myfifo */
int main(int argc, char* argv[]) {
    handle(argv[1]);
    printf("Done\n");
    return 0;
}