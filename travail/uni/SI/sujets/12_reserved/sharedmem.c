#include <sys/mman.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void OnError (char *str)
{
    perror (str);
    exit( EXIT_FAILURE );
}

int processFile (char* fileContent , off_t fileSize , char replaceChar , char byChar )
{
    int i;
    printf (" Processing char %c to be replaced by %c\n", replaceChar ,
	    byChar );
    for(i=0; i < fileSize ; i++)
	if( fileContent [i] == replaceChar )
	    fileContent [i] = byChar ;
    return 0;
}

int main(int argc , char* argv [])
{
    int fd , iArg; //file descriptor et ??
    pid_t fork_res ; //préparation d'un fork
    struct stat fileStat ; //état du fichier
    char* fileContent ; //buffer du fichier

    if (( argc % 2) || (argc < 4)) //si nb arguments impaire ou inferrieur à 4: erreur
    {
	printf (" Wrong number of arguments : %d\n\n",argc);
	printf (" Usage :\n\t sharedmem filename replaceChar byChar [
		replaceChar2 byChar2 [ replaceChar3 byChar3 [...]]]\ n\n");
	exit( EXIT_SUCCESS );
    }

    if (( fd = open(argv [1] , O_RDWR )) == -1) //gestion de l'erreur d'ouverture de fichier
	OnError (" Cannot open file");

    if( fstat (fd , & fileStat ) == -1) //gestion de l'erreur si on peut pas accèder aux infos du fichier
	OnError (" fstat ");

    //met le contenu du fichier dans la variable
    fileContent = (char *) mmap(NULL , ( size_t ) fileStat .st_size , PROT_READ | PROT_WRITE , MAP_SHARED , fd , 0);


    if( fileContent == MAP_FAILED ) //gestion de l'erreur dans le mappage
	OnError ("mmap");

    close (fd);

    for(iArg =2; iArg <argc;iArg +=2)
    {
	fork_res = fork ();
	if( fork_res == -1)
	    OnError ("Fork");
	else if( fork_res == 0)
	    return processFile ( fileContent ,fileStat .st_size , *argv[iArg
	    ], *argv[iArg +1]);
    }
    for(iArg =2; iArg <argc;iArg +=2)
	wait(NULL);
    if( munmap ( fileContent , fileStat . st_size ) == -1)
	OnError (" munmap ");
    return 0;
}
