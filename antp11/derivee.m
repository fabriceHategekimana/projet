function derive= derivee(x,f,h)
	%x is a vertical vector of values
	%f is a function that return a vector the same length as x
	%h is the step precision
	derive= [];
	l= length(x);
	for i = 1:1:l	
		XG= x;
		XD= x;
		XG(i)= XG(i)+(0.5*h);
		XD(i)= XD(i)-(0.5*h);
		derive= [derive (f(XG)-f(XD))/h];
	end
end
