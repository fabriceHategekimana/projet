function [t, y] = Euler_Implicite(f, df, t0, T, y0, Nt)
	maxit = 100;
	tol = 1e-8;

	h= abs(T-t0)/Nt;
	N = Nt; 
	M = length(y0);
	    
	t = t0:h:t0+(N-1)*h;
	y = zeros(M,N);
	y(:,1) = y0;

	g = @(h, tk, yk) (@(yk_plus_1) yk_plus_1 - yk - h*f(tk,yk_plus_1));
	dg = @(h, tk) (@(yk_plus_1) eye(M) - h*df(tk,yk_plus_1));

	for k=1:N-1
	    % Solve the equation y(k+1) - y(k) - h*f(t(k),y(k+1)) = 0
	    y(:,k+1) = NewtonSolve(g(h,t(k),y(:,k)), dg(h,t(k)), y(:,k), maxit, tol);
	end
end
