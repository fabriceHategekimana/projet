function y= matriceGauche(N)
	A= eye(N)*(-2);
	for i= [1:1:N]
		if i < N
			A(i, i+1)= 1;
		end
		if i > 1 && i < N-1
			A(i, i-1)= 1;
		end
	end
	y=A;
end
