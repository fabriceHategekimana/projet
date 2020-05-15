function [t, y]= Euler_Implicite_chaleur(y0, t0, Nt, T)
	h= abs(T-t0)/Nt;
	yn= y0;
	tn= t0;

	L= length(y0);
	I= eye(L);
	A= matriceGauche(L);

	y= [yn];
	t= [tn];

	for i= [1:1:Nt]
		%yn= yn+(h*f(tn, yn));
		yn= yn*inv(I-((h*A)/Nt^2));
		tn= tn+h;
		y= [y; yn];
		t= [t; tn];
	end
	y= y';
end
