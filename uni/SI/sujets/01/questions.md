Le programme ci-dessous est implémenté dans une machine à café dont les boutons
envoies les signaux CAFE, CREME et ANUL au programme principal (c.f. code).

À voir:
[signaux](signaux)

1. Combien de processus ce programme génère-t-il ? Décrire le rôle et les actions
de chaque processus.
2. Que ce passe-t-il si le bouton CAFE est pressé plusieurs fois de suite ?
3. Que ce passe-t-il si l’on appuye sur SIG_CREME sans qu’un café ne soit lancé ?
Que ce passe-t-il si l’on appuye sur SIG_CREME lorsqu’un café est lancé ?
4. Dans quel cas le programme affiche-t-il l’erreur "Erreure survenue, cafe inter-
rompu" ?
5. Pourquoi utiliser la fonction "write" au lieu de "printf" dans les handlers de
signaux ?
