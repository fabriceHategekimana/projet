function [x,X] = NewtonSolveEx2(f, df, matrice, x0, e0, tol, maxit)

  n = numel(x0);
  X = [];
  x = [x0;e0];
  for k=1:maxit
	s = df(x) \ f(x);
	if ( norm(s) <= tol * norm(x) )
		break
	end
    x = x - s;
    x(length(x)) = (x(1:length(x)-1)'*matrice*x(1:length(x)-1))/(x(1:length(x)-1)'*x(1:length(x)-1));
    X = [X x];
  end
  return
end
	  