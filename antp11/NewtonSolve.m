function [x,X] = NewtonSolve(f, df, x0, maxit, tol)

  n = numel(x0);
  X = [];
  
  x = x0;
  for i = 1 : maxit
	s = df(x) \ f(x);
	if ( norm(s) <= tol * norm(x) )
		break
	end
    x = x - s;
    if ( nargout == 2 )
      X = [X x];
    end
  end
 
  return
end
	  
	  
