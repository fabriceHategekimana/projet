# include <stdlib.h>
# include <unistd.h>
# include <stdio.h>
# include <signal.h>
# include <sys/types.h>
# include <sys/wait.h>
# include <string.h>
# include <errno.h>

# define SIG_CAFE SIGUSR1
# define SIG_CREME SIGUSR2
# define SIG_ANUL SIGINT

const char * const cremeStr = " Ajout de creme sur le cafe\n";
const char * const anulStr = "Cafe interrompu par l’utilisateur \n";
const char * const errStr = " Erreure survenue , cafe interrompu \n";
pid_t pidService = 0;
void exit_err ( const char* str)
{
    perror (str);
    exit( EXIT_FAILURE );
}

void set_sigaction_handler (int signum , void (* sig_handler )(int))
    // Le parametre sig_handler est une fonction " handler " ou SIG_IGN
{
    struct sigaction action ;
    //sigemptyset: définit un masque sur un ensemble vide
    //action.sa_mask un ensemble de signaux à masquer pendant l'exécution de l'action
    if( sigemptyset (& action.sa_mask ) == -1)
	exit_err (" set_sigaction_handler , sigemptyset ");
    //action.sa_flags définit le comportement du handler
    action.sa_flags = 0;
    //action.sa_handler prend l'action à exécuter SIG_DFL= default, SIG_ING= ignorer, address de la fonction à exécuter
    action.sa_handler = sig_handler ;
    //sigaction lie l'action &action au signal signum
    if( sigaction (signum , &action , NULL) == -1)
	exit_err (" set_sigaction_handler , sigaction ");
}

void service_handler (int sig)
{
    switch (sig)
    {
	// SIG_CREME recu
	case SIG_CREME :
	    write ( STDIN_FILENO , cremeStr , strlen ( cremeStr ));
	    break ;
	    // SIG_ANUL recu
	case SIG_ANUL :
	    write ( STDIN_FILENO , anulStr , strlen ( anulStr ));
	    exit( EXIT_SUCCESS );
	    break ;
	default :
	    fprintf (stderr , " Signal %d non attendu \n", sig);
	    exit( EXIT_FAILURE );
    }
}
void service ()
{
    set_sigaction_handler (SIG_CREME , service_handler );
    set_sigaction_handler (SIG_ANUL , service_handler );
    int err;
    sigset_t set , oldset ;
    err = sigemptyset (& set);
    err |= sigaddset (&set , SIG_CREME );
    if(err != 0)
	exit_err ("service , construction d’ensemble de signaux ");
    if( sigprocmask (SIG_BLOCK , &set , & oldset ) == -1)
	exit_err ("service , sigprocmask 1");
    printf ("Je commence a preparer un cafe\n");
    sleep (5);
    if( sigprocmask ( SIG_SETMASK , &oldset , NULL) == -1)
	exit_err ("service , sigprocmask 2");
    printf ("Cafe termine \n");
    exit( EXIT_SUCCESS );
}
void btn_handler (int sig)
{
    switch (sig)
    {
	// SIG_CAFE recu
	case SIG_CAFE :
	    //on crée un processus enfant
	    pidService = fork ();

	    if( pidService == -1)
		exit_err (" btn_handler , fork");
	    else if ( pidService > 0)
	    {
		set_sigaction_handler (SIG_CREME , btn_handler );
		set_sigaction_handler (SIG_ANUL , btn_handler );
		int status = 0;
		while ( ( status = waitpid ( pidService , NULL , 0)) == -1)
		    if( errno != EINTR )
			exit_err (" btn_handler , waitpid ");
		if( WIFEXITED ( status ))
		    if( WEXITSTATUS ( status ) != 0)
			write ( STDIN_FILENO , errStr , strlen ( errStr ));
	    }
	    else
		service ();
	    break ;
	    // SIG_CREME recu
	case SIG_CREME :
	    if(kill( pidService , SIG_CREME ) == 1)
		exit_err (" btn_handler , kill");
	    break ;
	    // SIG_ANUL recu
	case SIG_ANUL :
	    if(kill( pidService , SIG_ANUL ) == 1)
		exit_err (" btn_handler , kill");
	    break ;
	default :
	    fprintf (stderr , "Le signal %d non attendu \n", sig);
	    exit( EXIT_FAILURE );
    }
}
int main(void)
{
    set_sigaction_handler (SIG_CAFE , btn_handler );
    set_sigaction_handler (SIG_CREME , SIG_IGN );
    set_sigaction_handler (SIG_ANUL , SIG_IGN );
    while (1)
	pause ();
    return 0;
}
