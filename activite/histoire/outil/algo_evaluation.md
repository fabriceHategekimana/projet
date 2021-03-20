eval(action, commands):
	if action == "add":
		addFactRule(commands)
	elif action == "delete":
		deleteFactRule(commands)
	elif action == "check":
		checkFacts(commands)
	elif action == "display":
		
		
addFactRule(commands):
	command= commands[0]
	t= tuple(command)
	if commands[1] == "fact":
		sql= "insert into table(subject,link,goal) values(%s,%s,%s)" % t
	elif commands[1] == "rule":
		retropropagation("add", command)
		sql= "insert into table2(premise,conclusion) values(%s,%s)" % t
	sqlModify(sql)

deleteFactRule(commands):
	command= commands[0]
	t= tuple(command)
	if commands[1] == "fact":
		sql= "delete from table where subject='%s' and link='%s' and goal='%s'" % t
	elif commands[1] == "rule":
		retropropagation("delete", command)
		sql= "delete from table2 where premise='%s' and conclusion='%s'" % t
	sqlModify(sql)
	
checkFacts(commands):
	tab= commands.split(" or ")
	res= []
	for t in tab:
		res += union(t)
	print(res)

#ici plusieurs variables sont possibles
union(command):
	res= []
	r= unionHelper(t)
	if r != [False]:
		res += r
	if len(res) > 0:
		return res
	else:
		return [False]

unionHelper(fact):
	
	
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
