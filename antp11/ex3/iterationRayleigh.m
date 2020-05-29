function Vn= iterationRayleigh(V, A, k)
	Vn= V;
	[L,C]= size(A);
	I= eye(L,C);
	for i in [1:1:k]
		lambda= quotientRayleigh(V,A);
		%matrice gauche
		Gauche= zeros(L+1, C+1);
		Gauche(1:L, 1:C)= (A-(lambda)*I);
		Gauche(1:L,C:C+1)= [Vn;0];
		Gauche(L:L+1,1:C)= Vn'; 
		%matrice droite
		Droite= [(A-lambda*I)*v;0.5*(V'*V)-1];
		Vn= Vn-(inv(Gauche)*droite);
	end
end
