function y= matriceGauche(N)
	A= eye(N)*(1);
	for i= [1:1:N]
		if i < N
			A(i, i+1)= -2;
		end
		if i < N-1
			A(i, i+2)= 1;
		end
	end
	y=A;
end
