
Nx= 30;
X= linspace(0, 1, Nx);
y= @(x) ((x.^2).*(1-x));
x0= y(X)';
dx= 1/Nx;
t0= 0;
T= 2; % pour un interval entre (t0, T)
tol= 1e-12;

Nt= 4000;
%[T1, Y1]= Euler_Explicite_chaleur(x0, t0, Nt, T, dx);
[T2, Y2]= Euler_Implicite_chaleur(x0, t0, Nt, T, dx);
%U1= Ex3b_ref(X', T1, tol);
%plot(T1, Y1, T2, Y2, T1, U1);
plot(T2, Y2);
 
%err_exp1= max(abs(U1-Y1));
%err_imp1= max(abs(U1-Y2));
