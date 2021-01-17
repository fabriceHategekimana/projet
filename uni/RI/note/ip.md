IP jusqu'à la diapo 92
# IP
Protocole de niveau 3
Routage des données dans le réseau
Sans connexion
Ne gère pas la perte de datagramme

Structure:
16 bits en hexadécimal (donc 2 octet)
prefix|interface ID
préfix numéro du réseau(0-128)
Interface ID (le reste des bits)

Adresses Unicast:
	- Global unicast Adress (GUA)
	- Link Local Unicast Address (L-LUA)

GUA: servent à router les datagrammes

5 registre internet régionaux (Regional Internet Restistries RIR):
	1. AfriNIC
	2. APNIC
	3. LACNIC
	4. RIPE NCC

L'allocation d'adresse GUA:
	- statique
	- dynamique
    - datagramme en trois parties:
	1. Global Routing Prefix
	2. Subnet ID
	3. Interface ID

IANA (Internet Assigned Numbers Authority)

Adresse Unicast (point to point protocole)
GUA (Global Unicast Address)
L-LUA (link local unicast address)


RA (router Advertisement)

Allocatio adresses GUA

ULA (Unique Local Address): addresse privé (pas pour internet)

# Adresses Multicast
Déterminent des groupes multicasts
L'adresse de l'expéditeur doit être unicast (one-to-many)

# SNM (Solicited-node Multicast)
addresse associé aux adresse globales
Quand on connait l'adresse IP mais pas l'adresse MAC
Par rapport au broadcast c'est que les interfaces peuvent filtrer les messages multicast
Utilise des mécanisme de génération aléatoires pour être généré

# Routage des adresses multicast niveau 3
3 types de messages:
	1. Multicast Listener Query
	2. Multicast Listener Report
	3. Multicast Listener Done

# Format des datagrammes IP
ver|trafic class|Flow label|Payload lenght|Next header|Hop limit

Ver.:la version du protocole (6)
Trafic class: Composé du:
	- DSCP (DiffServ Code Point)
	- CU (Currently Unused)
Flow label: associe un même identifiant à tous les datagrammes qui composent un même flow de données (pour être traité de la même façon)
Payload length: indique la taille des données du datagramme sans l'entête.
Next header: vérifie que les bits après l'en-tête sont l'entête d'une autre protocole (encaps IPV6)
Hop limit: champ décrémenté à chaque routeur.

Datagrammes IP

# IPesc
Suite de protocoles utillisées pour garantir la sécurité des transmissions (authentification et intégrité) grâce à:
	- AH (autentification header)
	- ESP (Encapsuleting security payload)

# Algorithme de routage pour internet
Plusieurs algos
AS (autonome système): composent un système et utilisent un algo de routage propre
- IGP (inferiror Gateway protocole) protocole de routage utilisé dans un AS
- EGP (Exterior gatway protocole) protocole de communication entre AS

# Routage par vecteur de distance
Appellé algorithme de bellman-Ford, c'est un IGP. Routage par le plus court chemin.
S'utilise dans un réseau où:
- taille limité
- métrique fixe pour déterminer les distances entre routeurs
La métrique (fonction de distance), 
Dispose d'un algo précis

# RIPng
RIPng (Routing Information Protocol next eneration)
Protocole à vecteur de distance
métrique: nombre de saut
taille limite: 15 saut (16 = infini)
datagrammes UDP échangé sur le port 521
Deux type de messages:
	- request
	- response
Deux type de procéssus appelés:
	- processus d'entrée
	- processus de sortie

# Routage par des états des liens
Créer pour remplacer la lente convergence de l'algo par vecteur de distance
Les idées de bases de l’algorithme sont:
1. découvrir les routeurs voisins et leur adresse réseau
2. calculer le délai (coût) pour atteindre chaque voisin
3. construire un paquet résumant les informations découvertes
4. transmettre le paquet aux autres routeurs
5. calculer le plus court chemin vers chaque routeur

Contrainte: chaque routeur possède un identificateur unique
