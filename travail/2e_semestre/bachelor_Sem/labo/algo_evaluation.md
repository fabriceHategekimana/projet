eval(E):
	if terminal(E):
		i = conv(E)
		f = "i"
	else:
		f, sub= extract(E)
		i = eval(sub)
	return func(f, i)
