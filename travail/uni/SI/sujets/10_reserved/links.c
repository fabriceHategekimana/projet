#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {    //On vérifie qu'il y a uniquemnt deux arguments, la source et la destination
        printf("Invalid number of arguments:\nUsage:\n\t%s source dest\n", argv[0]);
        return 0;
    }
    
    char *in_dir = argv[1];     //Dossier d'entrée
    char *out_dir = argv[2];    //Dossier de sortie
    
    struct stat stats;
    if(stat(out_dir, &stats) < 0) {     //On utilise l'appel système stat pour récupérer les informations sur le fichier
        perror(out_dir);
        exit(EXIT_FAILURE);
    }
    
    if ( !(stats.st_mode & S_IFDIR) ) { //On vérifie que le second paramètre est bien un dossier
        fprintf(stderr, "%s: is not a directory\n", out_dir);
        exit(EXIT_FAILURE);
    }
    
    DIR *d = opendir(in_dir);   //On essaie d'ouvrir le dossier passé en premier paramètre
    if (! d) {
        fprintf(stderr, "Cannot open directory ’%s’: %s\n", in_dir,strerror(errno));
        exit(EXIT_FAILURE);
    }
    
    struct dirent *entry;
    while( (entry = readdir(d)) != NULL ) {     //On parcourt tout le dossier en ignorant les entrées '.' et '..'
        if (strcmp(entry->d_name, "..") != 0 && strcmp(entry->d_name, ".") != 0) {
            
            char path_in[PATH_MAX];     //On copie dans la variable 'path_in' la chaîne de caractères "<nom_du_dossier_d'entrée>/<nom_du_fichier"
            int res = snprintf(path_in, PATH_MAX ,
                                "%s/%s", in_dir, entry->d_name);
            if(res >= PATH_MAX)     //Vérification d'erreur
                fprintf(stderr, "Input path length is too long.\n");
                
            char path_out[PATH_MAX];    //On copie dans la variable 'path_out' la chaîne de caractères "<nom_du_dossier_de_sortie>/<nom_du_fichier"
            res = snprintf(path_out, PATH_MAX ,
                                    "%s/%s", out_dir, entry->d_name);
            if(res >= PATH_MAX)     //Vérification d'erreur
                fprintf(stderr, "Output path length is too long.\n");
            
            if(link(path_in, path_out) < 0)     //On utilise la fonction link pour créer une nouvelle entrée (lien dur vers le fichier) dans le second dossier
                perror("not possible to link");
        }
    }

    if( closedir(d) ) {     //On ferme le répertoire
        fprintf(stderr, "Could not close ’%s’: %s\n", in_dir, strerror (errno));
        exit (EXIT_FAILURE);
    }
    
}