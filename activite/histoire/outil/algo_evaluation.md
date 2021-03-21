eval(action, commands):
	if action == "add":
		addFactRule(commands)
	elif action == "delete":
		deleteFactRule(commands)
	elif action == "check":
		res= checkFacts(commands)
		print(res)
	elif action == "display":
		print("this feature will come later")
		
```python
addFactRule(commands):
	# command[0] contient la commande 
	# command[1] contient le type de la commande
	command= commands[0] 
	t= tuple(command)
	if commands[1] == "fact": 
		sql= "insert into table(subject,link,goal) values(%s,%s,%s)" % t
	elif commands[1] == "rule":
		retropropagation("add", command)
		sql= "insert into table2(premise,conclusion) values(%s,%s)" % t
	sqlModify(sql)
```


```python
retropropagation(mode, rule):
	premise= rule[0].split(" or ")
	conclusion= rule[1].split(" and ")
	res= []
	for p in premise:
		res += union(p)
	if mode == "add":
		sql= "insert into table (subject,link,goal) values "
		entry = "(%s,%s,%s),"
		last= -1
	elif mode == "delete":
		sql= "delete from table where "
		entry= "subject='%s' and link='%s' and goal='%s' or"
		last= -3
	for r in res:
		newfacts = complete(r, conclusion)
		sql += entry % tuple(newfacts)
	sql= sql[:last]
	sqlModify(sql)
```

```python
deleteFactRule(commands):
	command= commands[0]
	t= tuple(command)
	if commands[1] == "fact":
		sql= "delete from table where subject='%s' and link='%s' and goal='%s'" % t
	elif commands[1] == "rule":
		retropropagation("delete", command)
		sql= "delete from table2 where premise='%s' and conclusion='%s'" % t
	sqlModify(sql)
```

```python 
checkFacts(commands):
	tab= commands.split(" or ")
	res= []
	for t in tab:
		res += union(t)
	return res
```
	
```python
#ici plusieurs variables sont possibles (max 10)
#reçois plusieurs conjonctions et essaie de les complèter
union(command):
	#command is a list:
	res= []
	if isComplet(command[0]):
		t= tuple(command[0].split(" "))
		sql= "select subject,link,goal from table where truc='%s' and truc='%s' and truc='%s'" % t
		return sqlQuery(sql)
	else:
		sql= createUnionQuery(command[0].split(" "))
		val= sqlQuery(conj)
		if val == []:
			return []
		elif:
			for v in val:
				newCommand= complete(v, command)
				res += union(newCommand)
			return res
```

```python
#value est une list de un ou plusieurs valeurs
#command est une liste de un ou plusieurs prédicats
complete(values, extCommand)
	command= extCommand.copy() #pour éviter de modifier la liste d'origine
	#On change les variables qui nous inéressent
	for i in len(values):
		 index= command[0].index('VAR')	
		 variable= command[0][index,index+len('VAR')+1]
		 for c in command:
			c.replace(variable,values[i])
	return command
```

```python
createUnionQuery(command):
	variable
	value
	index= variableIndex(command)
	if len(index) == 2:
		tvariable= "%s,%s" % variables
	else:
		tvariable= "%s" % variables
	sql= "select "+tvariable+" where "+tvalue
	return sql
```

```python
countVariable(command):
	index= []
	for i in range(len(command)):
		if command[i].index("VAR") != -1:
			index.append(i)
	return index
```

```python
propagation(fact):
	link= select("link", fact)
	sql= "select * from table2 where premise like '%s'"	% link
	rules= sqlQuery(sql)
	res= []
	for r in rules:
		r= complete(fact, r)
		res += union(r)
	sendFacts(res)	
```
	
main:
	get(entree)
	res = eval(entree)
	print(res)
	

eval(entree):
	query= convert(entree)
	res= toSQL(query)
	complet, incomplet= checkCompletness(res)
	if incomplet:
		res = eval(develop(incomplet))
		complet += res
	return complet
