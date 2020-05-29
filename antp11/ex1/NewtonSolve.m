function [x,X] = NewtonSolve(f, df, x0, e0, tol, maxit)

  n = numel(x0);
  X = [];
  x = [x0;e0];
  for k=1:maxit
	s = df(x) \ f(x);
	if ( norm(s) <= tol * norm(x) )
		break
	end
    x = x - s;
    X = [X x];
  end
  return
end
	  
	  
