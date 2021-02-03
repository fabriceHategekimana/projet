# Plan du cours

Programmation concurrente:
	- [Exclusion_mutuelle](Exclusion_mutuelle)
	- Synchronisation
	- Synchronisation wait-free
Programmation distribuée
	- Sockets/RMI en Java

# Trouver:
	- problèmes de programmation concurrente
	- contrainte des application concurrente

Programme cocurrent:
Peut s'exécuter en parallèle
composé de processus (programme séquntiel), appellé threads s'ils partagent une même zone mémoire.


# Problèmes classiques
[Interblocage](Interblocage) (deadlock)
Interférence: plusieurs processus modifie la même donnée en même temps
Insuffisance de resources (starvation)

# proriétés (contraintes) désiré(e)s:
Sûreté (safety)
Vivacité (liveness)

un programme concurrent n'est pas forcément parallèle (système multitâches)

Système distribué: composé de systèmes qui communique par message à l'aide d'un réseau

# Java
Les threads partagent la même mémoire grâce à JVM
Les objets encapsulent un thread
On utilise la notion de moniteur (encapsulent des ressources partagées et donnes des méthodes pour les manipuler)
Chez les moniteur, les méthodes s'exécutent de façon atomique. Possède un verrou.
• La méthode main() qui correspond au programme principal est le thread principal.
• La méthode sleep() permet de donner la main à un autre thread (y compris le thread principal).
• On peut invoquer seulement la méthode run(), le programme s’exécute mais dans un seul thread.
• La méthode start() ne peut être appelée qu’une seule fois pour un objet donné.

Thread class pour créer un thread dans le main.
Runnable interface pour créer un thread dans le main.

En fait Thread implémente runnable

Thread.interrupt() permet a un thread d'en interrompre un autre.

![Différents_état_d_un_thread](../../images/Différents_état_d_un_thread.png)

Pour l'ordonnancement des thread, on utilise un système de priorité (max, min, norm)
Cela est placé dans la variable Priority
join() permet a un thread d'attendre qu'un autre finisse
