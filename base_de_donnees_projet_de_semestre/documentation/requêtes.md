Principales requêtes:
======================

Ce projet est rédigé en python et exploite une base de donnée sql.  

Le logiciel se base sur un comptage annuel. Cela veut simplement dire que les requêtes prennent en compte l'année indiquée dans le logiciel.  

On classe les requêtes en deux catégories:  
## Requête de sélection
Ces requêtes on pour but d'interroger la base de donnée et d'obtenir des tables à afficher.  

#### Requête simple et générale
Cette requête sert juste a afficher des tables brutes avec une condition (=where) simple.    
Son but est de générer les listes dont on a besoins pour l'outil de sélection par liste.    
Les variables "table" et "where" peuvent apporter des variations.    
```python
        tab= self.data.getTab("select * from "+table+" "+where, True) 
```
#### Requêtes de sélection pour les outils d'édition
Ces requêtes génèrent les données pour l'outil de selection d'une liste d'employé pour un chantier.    
Les employés sont gérés par leurs idée mais l'utilisateur à besoin de voir les détails pour faire une sélection pertinente.  
```python
        tabAll= self.data.getTab("select ID_EMPLOYES from employes", False)
        tab= self.data.getTab("select * from employes", True)
	
```
#### Requêtes pour la visualisation de la table chantier
Ces requêtes permettent d'obtenir des donnée de la table chantier (qui est l'une des tables les plus utilisées).  
```python
	#La première requête permet d'afficher les détail d'un chantier par son identifiant (sa clé primaire)
        tab= self.data.getTab("select * from chantiers where NUM_CHANTIER='"+self.ID+"'", True)
	
	#La deuxième requête sert à générer le date de début et la durée de chaque chantier pour créer le planning visuel au centre du logiciel.
        tab= self.data.getTab("select DATE_DEBUT,DUREE from chantiers where DATE_DEBUT like '%/"+self.annee+"'", False)
	
	#La troisième ne sert seulement qu'à générer une table vide avec un en-tête (je crois que c'était pour un test)
        header= self.data.getTab("select * from chantiers where ADRESSE='rien'", True)
	
	#La quatrième sert à générer les chantiers remplissant la colonne de gauche.
        tab= self.data.getTab("select NUM_CHANTIER from chantiers where DATE_DEBUT like '%/"+self.annee+"'", False)
```
#### Requêtes pour la visualisation de la table livraisons
Ces requêtes servent à générer des informations à propos de la table livraisons.  
```python
	#Cette requête génère tout les identifiant possibles des livraison (cela servira pour créer un nouvel identifiant)
        lastID= self.data.getTab("select ID_LIVRAISON from livraisons", False).pop().pop()
	
	#Cette requête ser seulement qu'à générer une table vide avec un en-tête(je crois que c'était pour un test)
        header= self.data.getTab("select * from livraisons where HEURE='rien'", True)
	
	#affiche toute les livraisons
        tab= self.data.getTab("select * from livraisons where DATE_LIVRAISON like '%/"+self.annee+"'", True)
	
	#affiche les livraison pour un jour spécifique (généré par le calendrier)
        tab= self.data.getTab("select * from livraisons where DATE_LIVRAISON='"+self.date_livraison[1]+"'", True)
```
	
## Requêtes de modifications
Ces requêtes modifient directement la base de donnée. Le logiciel se contente de charger les données mises à jour.  

#### Requêtes de mise à jour de la table livraisons
Ces requêtes servent à la mise à jour de la table livraisons  
```python
	#fonction générale où aboutissent la plus part des outils d'édition, la colonne_a_modifier indique ou faire la modification alors que ID_LIVRAISON indique quel livraison changer
        self.data.modify("update livraisons set "+self.colonne_a_modifier+"='"+nouveau+"' where ID_LIVRAISON='"+self.ID+"'")
        self.data.modify("update livraisons set "+self.colonne_a_modifier+"='"+self.date_retenue+"' where ID_LIVRAISON='"+self.ID+"'")
        self.data.modify("update livraisons set "+self.colonne_a_modifier+"='"+nouveau+"' where ID_LIVRAISON='"+self.ID+"'")
```
#### Requêtes pour la mise à jour de la table chantiers
Ces requêtes servent à la mise à jour de la table chantiers  
```python
	#fonction générale où aboutissent la plus part des outils d'édition, la colonne_a_modifier indique ou faire la modification alors que NUM_CHANTIER indique quel chantier changer
        self.data.modify("update chantiers set "+self.colonne_a_modifier+"='"+nouveau+"' where NUM_CHANTIER='"+self.ID+"'")
        self.data.modify("update chantiers set "+self.colonne_a_modifier+"='"+text+"' where NUM_CHANTIER='"+self.ID+"'")
        self.data.modify("update chantiers set "+self.colonne_a_modifier+"='"+self.date_retenue+"' where NUM_CHANTIER='"+self.ID+"'")
```
#### Requêtes pour l'insertion et la suppression des livraisons
Ces requêtes servent à l'insertion et à la suppression des livraisons  
```python
	#Cette requête insert crée une nouvelle livraison avec des paramètres par défaut qui pourront être modifié ultérieurement
        self.data.modify("insert into livraisons ("+",".join(header[0])+") values ("+chaine+")")
	
	#cette requête delete supprime just la livraison indiqué par ID_LIVRAISON
        self.data.modify("delete from livraisons where ID_LIVRAISON='"+self.ID+"'")
```

#### Requêtes pour l'insertion et la suppression des chantiers
Ces requêtes servent à l'insertion et à la suppression des chantiers  
```python
	#Cette requête insert crée un nouveau chantier avec des paramètres par défaut qui pourront être modifié ultérieurement
        self.data.modify("insert into chantiers ("+",".join(header[0])+") values ("+chaine+")")
	
	#Cette requête delete supprime juste le chantiers indiqué par le NUM_CHANTIER
        self.data.modify("delete from chantiers where NUM_CHANTIER='"+self.ID+"'")
```
