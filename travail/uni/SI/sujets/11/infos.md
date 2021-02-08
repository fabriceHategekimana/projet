# memory

1. A l’aide d’un schema expliquer la notion d’adressage virtuel et sa relation avec la mémoire physique.

2. Que fait le programme suivant ?

3. A quoi sert l’entrée "install" du makefile ?

4. Décrivez le code et son fonctionement en détail.

5. Qu’est q’un défaut de page mineur / majeur ?

6. Le programme effectue-t-il plus de défaut de page lorsque le paramètre "lock" est passé ou sans paramètre ?

7. Dans un cas général pourquoi utiliser la fonction mlock ?
 
```c 
//la structure rlimit

struct rlimit { 
	rlim_t rlim_cur; /* Soft limit */
	rlim_t rlim_max; /* Hard limit (ceiling for rlim_cur) */
}; 
```

```c 
// la structure rusage

    struct rusage {
    struct timeval  ru_utime;     /* user time used */
    struct timeval  ru_stime;     /* system time used */
    long            ru_maxrss;    /* maximum resident set size */
    long            ru_idrss;     /* integral resident set size */
    long            ru_minflt;    /* page faults not requiring physical 
				     I/O */
    long            ru_majflt;    /* page faults requiring physical I/O */
    long            ru_nswap;     /* swaps */
    long            ru_inblock;   /* block input operations */
    long            ru_oublock;   /* block output operations */
    long            ru_msgsnd;    /* messages sent */
    long            ru_msgrcv;    /* messages received */
    long            ru_nsignals;  /* signals received */
    long            ru_nvcsw;     /* voluntary context switches */
    long            ru_nivcsw;    /* involuntary context switches */
}
```
