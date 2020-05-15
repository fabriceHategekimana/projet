function u = Ex3b_ref(x,t,tol)

% function u = Ex3b_ref(x,t,tol)
% Purpose: Computes a reference solution for the IVP
%          u_t - u_xx = 0, u(x,0)=x^2*(1-x)
%          using the Fourier expansion of the initial value with respect to
%          the system of sin(pi*k*x), k=1,2,...
% Input:
%  - x is a vector of spatial points
%  - t is a vector of temporal points
%  - tol is the threshold used for the truncation of the expansion
% Output:
%  - u is the matrix of the values of the evaluated reference solution
%    at the space-time points x*t'
% Created:     08.05.2020
% Last change: 08.05.2020

Nx = numel(x);
Nt = numel(t);
u = zeros(Nx,Nt);

for i=1:Nt
    k = 0;
    while true
        k = k+1;
        c = (-4)*(1 + 2*(-1)^k)/(pi*k)^3 * exp(-t(i)*(pi*k)^2);
        if (abs(c) <= tol)
            k = k-1;
            break
        end
        u(:,i) = u(:,i) + c*sin(pi*k*x);
    end
end

end
