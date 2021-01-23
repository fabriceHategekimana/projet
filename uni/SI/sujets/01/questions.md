Le programme ci-dessous est implémenté dans une machine à café dont les boutons
envoies les signaux CAFE, CREME et ANUL au programme principal (c.f. code).

À voir:
[signaux](signaux)

# 1. Combien de processus ce programme génère-t-il ? Décrire le rôle et les actions de chaque processus.
Ce programme génère seulement un processus enfant par appel du signal CAFE.

# 2. Que ce passe-t-il si le bouton CAFE est pressé plusieurs fois de suite ?
À chaque fois, l'enfant précédent va être abandonné à sont sort et on ne pourra seulement annuler le comportement du dernier enfant.

# 3. Que ce passe-t-il si l’on appuye sur SIG_CREME sans qu’un café ne soit lancé ?
Il ne va rien se passer, par défaut le programme ignore les signaux SIG_CREME et SIG_ANUL jusqu'à ce que SIG_CAFE soit envoyé.

## Que ce passe-t-il si l’on appuye sur SIG_CREME lorsqu’un café est lancé ?
Si SIG_CREME est lancé avant la fin de la préapration d'un café, alors le processus parent envera le signal au processus enfant qui le traitera avant ou après la préparation du café.

# 4. Dans quel cas le programme affiche-t-il l’erreur "Erreure survenue, cafe inter- rompu" ?
Quand le processus enfant a quitté d'une manière inattendue, par exemple une suppression forcé du processus.

# 5. Pourquoi utiliser la fonction "write" au lieu de "printf" dans les handlers de signaux ?
Il se peut que plusieurs processus utilisent les même handler, de ce fait, ils ne peuvent pas tous afficher dans le stdin courant avec printf, C'est pourquoi ils utilisent le write qui les permettra d'écrire dans le tty courant.
