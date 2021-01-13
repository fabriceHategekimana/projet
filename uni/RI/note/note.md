Modèle ISO

## Couche physique:
La couche physique:
est responsable de transmettre ‘physiquement’ l’information d’une
station à une autre. La nature des signaux et du média de
communication doivent être définis.
• Signaux électriques, tensions appliquées
• Signaux optiques, longueur d’ondes
Cette couche est responsable de la transmission d’une suite de 0 et
de 1, sans format, sous la forme d’un flot de données.

## Couche de liason de données
• La couche liaison de données – link layer (LL):
fiabilise les transmissions de la couche physique.
• gère les erreurs de transmission
• Structure le flot de données en trame de données (de 100 à
1000 octets).
• Introduit différents types de trames – contrôles et données –
en particulier les trames d’acquittement qui permettent de
vérifier que les données ont bien été reçues.
• Corrige les erreurs – trames perdues ou transmission.

## Protocol ARQ
Les protocoles ARQ (Automatic-Repeat_Request) sont destinés à
corriger les erreurs de transmissions en répétant les messages non
acquités. Ces protocoles sont implémentés dans les couches liaisons
de données (et transport - TCP).

1. Stop-and-Wait ARQ
2. Go-Back-N ARQ
3. Selective-Repeat ARQ

## Trame
En-tête | Données | CRC


## 1. Stop-and-Wait ARQ
émetteur procède selon les étapes suivantes:
1. transmet une trame
2. déclenche un temporisateur et attend un acquittement
3. si un acquittement positif est reçu, transmet la trame suivante
4. si un acquittement négatif ou que le temporisateur expire,
retransmet la trame.
5. goto 1.


## 2. Go-Back-N ARQ
Avec le protocole Go-Back-N, l’émetteur transmet les trames et
mémorise les trames localement jusqu’à réception de l’acquittement.
Le nombre de trames dans le tampons d’émission s’appelle la fenêtre
de transmission, noté N. N est le nombre de trames transmises
pendant un intervalle RTT.
Le récepteur vérifie que les trames reçues sont correctes. Si oui, il
transmet un acquittement positif (ACK) pour chaque trame séparément.
Lorsque l’émetteur reçoit l’acquittement il supprime la trame
correspondante de son tampon d’émission.
Si erreur: aquitement négatif

## 3. Selective Repeat ARQ (SR ARQ)
Le protocole SR ARQ améliore le protocole Go-Back-N. Avec ce
protocole, l’émetteur ne retransmet que les trames négativement
acquitées.

## Stop-and-wait avec automate
Mesure de performance
Probabillité de transmission d'une trame
e= 1- (1-epsilon)^n=~epsilon*n
L'état d'un émetteur est un vecteur donnant le résultat des trames envoyé selon un temps t
Au temps t=0
s(0)= (1 0 0 ...)
s(1)=(1-e e 0 ...)

![Proba_stop_and_wait](../../images/Proba_stop_and_wait.png)
En définissant une bonne matrice, on peut alors définir l'état d'un système selon cette formule

![Proba2_sto_and_wait](../../images/Proba2_sto_and_wait.png)

