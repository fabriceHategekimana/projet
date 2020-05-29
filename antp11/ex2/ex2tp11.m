
n= 2;
D= diag(linspace(10, 1, n));
[Q, ~]= qr(rand(n));
A= Q*D*Q';
P= rand(n);
B= P*(D/P);

%xOA= v_exactA + rand(n,1)/n;
%xOB= v_exactB + rand(n,1)/n;
%eO= lam_exact + 0.04;

f= @(x) ([(A-(x(end)*eye(size(A))))*x(1:end-1) ; 0.5*(x(1:end-1)'*x(1:end-1))-1]);
x0= ones(n+1, 1);
dy= @(x) derivee(x, f, 0.00001)
maxit= 100000;
tol= 0.0000001;
sol= NewtonSolve(f,dy,x0,maxit,tol);
sol

[V, D]= eig(A)

