#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <time.h>

#include "common.h"

void pa( struct sockaddr_in *address, const char *host, int port ) {    //Fonction pour préparer la structure correspondant à l'adresse du client
    memset(address, 0, sizeof(struct sockaddr_in));     //Initialisation de la structure à 0
    address->sin_family = AF_INET;      //On précise la famille d'adresse (AF_INET pour Internet dans ce cas)
    inet_pton( AF_INET, (char*) address, &(address->sin_addr) );    //On utilise inet_pton pour convertir une chaîne de caractères en binaire (Exemple: "127.0.0.1" -> 0x7F000001)
    address->sin_port = htons(port);    //On convertit le port qui est un entier vers l'ordre des octets du réseau
}

int ms( const char *host, int port ) {      //Fonction pour créer la socket du client et effectuer une connexion au serveur
    struct sockaddr_in address;
    int sock = socket(PF_INET, SOCK_STREAM , 0);    //On utilise l'appel système socket avec en paramètres le domaine (PF_INET pour Internet), le type de communication (SOCK_STREAM pour TCP) et le protocole
    if( sock < 0 ) {    //On vérifie s'il n'y a pas eu d'erreur
        die("Failed to create socket");
    }
    pa( &address, host, port );     //On prépare la structure sockaddr_in avec les paramètres précisés plus haut
    if( connect(sock, (struct sockaddr *) &address, sizeof(struct sockaddr_in)) < 0) {      //On initie une connexion vers l'adresse du serveur
        die("Failed to connect with server");
    }
    return sock;
}

int get( int socket, struct tm *answer ) {      //Fonction permettant de recevoir les données du serveur
    int r = read( socket, answer, sizeof(struct tm) );      //On utilise l'appel système read pour lire les données reçues sur le descripteur de fichier
    return r;
}

void display( struct tm *t ) {      //Fonction permettant d'afficher les informations reçues du serveur
    printf( "%d/%d/%d - %d:%d:%d\n", 
            t->tm_mday, (t->tm_mon+1), (t->tm_year+1900),   //tm_mday -> jour du mois (1-31), tm_mon -> mois (0-11), tm_year -> nombre d'années depuis l'an 1900
            t->tm_hour, t->tm_min, t->tm_sec );             //tm_hour -> heure (0-23), tm_min -> minutes (0-59), tm_sec -> secondes (0-60)
}

int main(int argc, char *argv[]) {
    int sock;
    char *host;
    int port;
    struct tm answer;

    if (argc != 3) {    //On autorise uniquement deux paramètres (l'hôte et le port du serveur)
        fprintf(stderr, "USAGE: %s <host> <port>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    host = argv[1];
    port = atoi(argv[2]);       //On convertit le port reçu sous forme de chaîne de caractères en entier

    sock = ms( host, port );    //On fait le nécessaire pour créer la socket du client

    if( get(sock,&answer) <  0 ) {      //On reçoit les données du serveur et on vérifie qu'il n'y a pas eu d'erreur
        die( "Reception error." );
    }

    close(sock);        //On ferme la socket du client
    
    display(&answer);   //On affiche les données reçues sur la sortie standard
    
    exit(EXIT_SUCCESS); //On termine le programme
}