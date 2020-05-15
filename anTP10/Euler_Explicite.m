function [t, y]= Euler_Explicite(f, y0, t0, Nt, T)
	h= abs(T-t0)/Nt;
	yn= y0;
	tn= t0;

	y= [yn];
	t= [tn];

	for i= [1:1:Nt-1]
		yn= yn+(h*f(tn, yn));
		tn= tn+h;
		y= [y yn];
		t= [t tn];
	end
end
