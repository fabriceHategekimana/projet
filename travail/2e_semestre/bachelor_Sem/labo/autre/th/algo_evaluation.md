eval(E):
	if isTerminal(E):
		i = conv(E)
		f = "i"
	else:
		f, sub= extract(E)
		i = eval(sub)
	return func(f, i)
	

isTerminal(E):
	try:
		a= int(E)
		return True
	except:
		return False

conv(E):
	return int(E)
	
func(f,i):
	E= insert i dans f	
	return eval(E)
