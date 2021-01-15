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
#define MAX_PENDING 5   //Nombre max de clients autorisés

void pa( struct sockaddr_in *address,  int port ) {     //Fonction pour préparer la structure correspondant à l'adresse du serveur
    memset(address, 0, sizeof(address));    //Initialisation de la structure à 0
    address->sin_family = AF_INET;      //On précise la famille d'adresse (AF_INET pour Internet dans ce cas)
    address->sin_addr.s_addr = htonl(INADDR_ANY);   //On veut que le serveur soit lié à toutes les interfaces réseaux donc on utilise INADDR_ANY
    address->sin_port = htons(port);    //On convertit le port qui est un entier vers l'ordre des octets du réseau
}

int ms( int port ) {    //Fonction pour créer la socket du serveur et la mettre en passif
    struct sockaddr_in address;
    int sock = socket(PF_INET, SOCK_STREAM , 0);    //On utilise l'appel système socket avec en paramètres le domaine (PF_INET pour Internet), le type de communication (SOCK_STREAM pour TCP) et le protocole
    if( sock < 0 ) {    //On vérifie s'il n'y a pas eu d'erreur
        die("Failed to create socket");
    }
    pa( &address, port );   //On prépare la structure sockaddr_in et on utilise l'appel système bind pour lier la socket à cette adresse
    if( bind( sock, 
            (struct sockaddr *) &address, 
            sizeof(address)
            ) < 0  ) 
        {
            die("Failed to bind the server socket");
        }
    if (listen(sock, MAX_PENDING) < 0) {    //On utilise l'appel système listen pour faire une socket passive (capable d'accepter des connexions)
        die("Failed to listen on server socket");
    }
    return sock;
}

void hc( int clientSock ) {     //Fonction permettant d'envoyer les informations de temps au client
    time_t t;
    struct tm *now;     //On crée une structure tm
    time( &t );     //On affecte à la variable 't' la valeur du temps en secondes
    now = gmtime( &t );     //On transforme le temps obtenu en temps décomposé grâce à gmtime et on met le résultat dans la structure tm 'now'
    write( clientSock , now, sizeof(struct tm) );   //On envoie la structure au client
    close( clientSock );    //On ferme la socket du client
}

void run( int serverSock ) {
    while( 1 ) {
        struct sockaddr_in clientAddress;
        unsigned int clientLength = sizeof(clientAddress);
        int clientSock;
        printf( "Waiting for incoming connections\n");
        clientSock = accept(serverSock , (struct sockaddr *) &clientAddress ,   //On utilise accept pour accepter les connexions clients
                            &clientLength );
        if( clientSock < 0 ) {      //On termine le programme s'il y a eu une erreur
            die("Failed to accept client connection");
        }
        printf( "Client connected: %s\n", inet_ntoa(clientAddress.sin_addr));   //On affiche l'adresse IP du client qui s'est connecté
        hc(clientSock);     //On envoie les informations au client et on ferme la socket
    }
}

int main( int argc, char **argv ) {
    int servSock;
    int port;

    if (argc != 2) {    //On vérifie qu'il y a bien un seul argument (le port du serveur)
        fprintf(stderr, "USAGE: %s <port>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    port = atoi(argv[1]);   //On convertit le port reçu sous forme de chaîne de caractères en entier
    
    servSock = ms( port );      //On fait le nécessaire pour créer la socket du serveur
    
    printf( "Server running on port %d’\n", port );
    
    run( servSock );    //On attend les connexions et on gère les clients
    
    close(servSock);    //On ferme le descripteur de fichier (ici une socket)
    
    return EXIT_SUCCESS;//On termine le programme
}