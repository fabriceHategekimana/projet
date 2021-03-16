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
