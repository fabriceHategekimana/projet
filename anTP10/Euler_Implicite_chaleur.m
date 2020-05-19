function [t, x]= Euler_Implicite_chaleur(x0, t0, Nt, T, dx)
	h= abs(T-t0)/Nt;
	xn= x0;
	tn= t0;

	L= length(x0);
	I= eye(L);
	A= matriceGauche(L)/dx^2;

	x= [xn];
	t= [tn];

	for i= [1:1:Nt]
		%xn= xn+(h*f(tn, xn));
		xn= inv(I-(h*A))*xn;
		tn= tn+h;
		x= [x xn];
		t= [t tn];
	end
end
