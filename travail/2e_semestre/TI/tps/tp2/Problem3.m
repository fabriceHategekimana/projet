% Problem 3

% a) Markov inequality
% X = X*1{X<=t} + X*1{X>t}
% with 1 the indicator function
% E[X] = E[X*1{X<=t}] + E[X*1{X>t}]
%      >= E[X*1{X>t}]
%      >= E[t*1{X>t}] = t*E[1{X>t}] = t*Pr{X>t}
% ==> Pr{X > t} =< E[X]/t.
% We can apply the same idea using Sum or integral notation of E[|X|]

% Taking X such that P(X=0)=1, we get P(X>t) = 0 = E[X]/t

% b) Chebychev inequality
% Let's set X = |Y-m|^2
% We have Pr{|X-m|>epsilon} = Pr{(X-m)^2>eps^2} = Pr{Y>eps^2}
% Using Markov we get Pr(Y>eps^2) =< E[Y]/eps^2
% E[Y] = E[(X-m)^2] = Var(X)
% Finally ==> Pr(|X-m|>eps) =< Var(X)/eps^2

% c) Weak law of large numbers
% Using Chebychev with X=Sum(Zi, i=1..n)/n we get
% Pr(|Sum(Zi, i=1..n)/n - m|>eps) =< Var(Sum(Zi, i=1..n)/n)/eps^2
% Var(Sum(Zi, i=1..n)/n) = Var(Sum(Zi, i=1..n))/n^2 
% = Sum(Var(Zi), i=1..n)/n^2 = (n*Var(Z))/n^2
% = Var(Z)/n
% Finally ==> Pr(|Sum(Zi, i=1..n)/n - m|>eps) =< Var(Z)/(n*eps^2)