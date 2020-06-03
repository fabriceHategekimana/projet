Solution actuelle:
==================

## Pour afficher les titres
Hi jmroach,

You're going to want to use an sqlite pragma statement. A pragma statement lets you query database meta-data or in some cases alter the behavior of the database. The pragma that gives you column headers is called "table_info." In the example you gave below, you would use it by saying:

    cursor.execute("PRAGMA table_info(tablename)"
        print cursor.fetchall()
	
	And you should get back a printed list of tuples, where each tuple describes a column header.
	
	Hope this helps

## Stratégie de transfert
L'idéal serait d'avoir une séquence comme ça:
```
	tab= getData(key,[query])
	addTab(tab,table)
```
