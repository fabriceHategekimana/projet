#include <stdio.h>              //Macro pour inclure le fichier stdio.h à la précompilation     (pour utiliser printf et autres)
#include <stdlib.h>             //Macro pour inclure le fichier stdlib.h à la précompilation    (pour utiliser malloc et free)
#include <math.h>               //Macro pour inclure le fichier math.h à la précompilation      (pour utiliser la fonction pow)

#define E_NOT_VALID_CHAR -1     //Macro (remplace E_NOT_VALID_CHAR par -1 à la précompilation)
#define NB_BITS_OCTETS 8        //Macro (remplace NB_BITS_OCTETS par 8 à la précompilation)

typedef short int number;       //Définition d'un alias pour le type de données "short int" 

char errorMsg[] = "Erreur non documentee\n";    //Variable globale initialisée -> elle se trouve dans la section "Données" dans le ".data"
int unUsedVariable; //variable inutile sauf pour la question 3 -> variable globale non initialisée donc elle se trouve dans la section "Données" dans le ".bss"

/*Fonction permettant de convertir la chaîne passée en paramètre du programme en entier
Elle prend en paramètre un pointeur sur "number" et une chaine de caractère constante (pour s'assurer qu'elle ne sera pas modifiée) */
int convert(number* res, const char* chaine) {
    int i,length = 0;   //Initialisation de variables locales -> pile
    *res = 0;           //Initialisation -> pile

    if(*chaine == '\0')             //Si le premier caractère de la chaîne est vide (c'est-à-dire la chaîne est vide), on retourne -1
        return E_NOT_VALID_CHAR;
        
    while(chaine[length] != '\0')   //On parcourt la chaîne jusqu'au caractère de fin de chaîne '\0' et on incrémente la variable "length"
        length++;
    length = length - 1;            //On retire 1 donc on a "length" = (taille exacte de la chaîne de caractères - 1)
    
    for(i=length; i>=0; i--) {                          //Cette boucle for permet de parcourir la chaîne passée en paramètre
        if( (chaine[i] < '0') || (chaine[i] > '9') )    //On compare le code ASCII des caractères pour vérifier si le caractère est un chiffre entre 0 et 9
            return E_NOT_VALID_CHAR;                    //On retourne -1 si ce n'est pas le cas (donc il s'agit de caractères autre que des chiffres)
            
        *res += (chaine[i] - '0') * pow(10, length-i);  /* (chaine[i] - '0') correspond à la différence entre le caractère de la chaîne et le code ASCII de 0, qui est égal à 48
                                                        Cette différence permet d'obtenir le chiffre en question. Ex: '5' = 53 en ASCII. 53 - 48 = 5
                                                        A chaque tour on multiplie le chiffre par 10^(position du chiffre). Ex: 143 -> (3 * 10^0) + (4 * 10^1) + (1 * 10^2) */
    }
    //A la fin, "res" est égal à l'entier correspondant à la chaîne passée en paramètre de la fonction (Donc pour ./convert 100, res = 100)
    
    return 0;   //On retourne 0 si tout s'est bien passé
}

char* getStr(number value) {    //Fonction permettant de construire la chaîne en binaire correspondant au nombre (short int) passé en paramètre
    number testBit;     //Déclaration -> variable non initialisée donc elle se trouve sur la pile
    int i, nbBits;      //Déclaration -> variables non initialisées donc elles se trouvent sur la pile
    
    nbBits = sizeof(value) * NB_BITS_OCTETS;    /*On multiplie la taille d'un "short int" (minimum 2 octets) par 8
                                                On obtient ainsi le nombre de bits à utiliser pour représenter le nombre en binaire*/
    
    char* str = (char*) malloc(nbBits);         /*On fait une allocation mémoire donc "str" (l'adresse sur laquelle pointe str) est sur le tas, 
                                                mais "&str" (l'adresse du pointeur str) est sur la pile. On a donc une chaîne de caractères
                                                pour représenter le nombre en binaire. Ici le tas est modifié lors de l'exécution du programme*/
    
    if(str == NULL)                             //Si le malloc a échoué on retourne NULL
        return NULL;
        
    for(i=0; i<nbBits; i++) {                   //Boucle permettant de former le nombre binaire
        testBit = pow(2,i);                     /*On fait tour à tour (2^i) donc "testBit" -> 1, 2, 4, 8 etc...
                                                Attention!!! A partir de i = 15, testBit devient négatif à cause de la règle du complément à 2
                                                La fonction pow retourne un double qui est ici convertit en "short int" */
        
        /*On fait un "ET Logique" avec l'opérateur & sur les représentations binaires des nombres
        Si le résultat correspond au bit de test, on met le caractère correspondant dans la chaîne à 0 ou à 1
        Le bit de test permet de connaître chaque bit de la variable "value" 
        Ex: ./convert 10 -> 10 en binaire correspond à 1010. Voir l'image dans le document*/
        if( (testBit & value) == testBit )      
            str[nbBits-i-1] = '1';
        else
            str[nbBits-i-1] = '0';
    }

    return str;     //On retourne la chaîne de caractères obtenue
}

int main(int argc, char* argv []) {     //Fonction main. Les adresses des fonctions (main, getStr et convert) se trouvent dans le segment de code
    number input;   //Déclaration -> variable non initialisée donc elle se trouve sur la pile
    char* str;      //Déclaration -> variable non initialisée donc elle se trouve sur la pile
    
    if(argc < 2) {                                      //On attend au moins un paramètre pour utiliser le programme
        fprintf(stderr, "Usage: convert entier\n\n");   //On écrit sur la sortie d'erreur standard
        return -1;                                      //On retourne -1
    }
    
    /*On utilise la fonction convert et on vérifie qu'il n'y a pas eu d'erreur
    convert retourne -1 s'il y a eu une erreur ou 0 si tout s'est bien passé*/
    if(convert(&input, argv[1]) != 0) {                 //On passe l'adresse de la variable "input" pour qu'elle soit modifiée par la foncion convert
        fprintf(stderr, "%s", errorMsg);                //On écrit sur la sortie d'erreur standard le message d'erreur
        return -1;                                      //On retourne -1
    }
    
    /*On utilise la fonction getStr et on vérifie qu'il n'y a pas eu d'erreur
    getStr retourne NULL s'il y a eu une erreur (erreur d'allocation mémoire) ou une chaîne non nulle si tout s'est bien passé*/
    if( (str = getStr(input)) == NULL) {
        fprintf(stderr, "%s", errorMsg);                //On écrit sur la sortie d'erreur standard le message d'erreur
        return -1;                                      //On retourne -1
    }
    
    printf("%s\n", str);                                //On affiche la chaîne sur la sortie standard
    
    free(str);                                          //On libère la mémoire allouée par le malloc
    
    return 0;                                           //On retourne 0
}
