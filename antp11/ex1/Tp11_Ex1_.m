%% Exercice 1 : La méthode de Newton pour le calcul des valeurs et des vecteurs propres

n = 100;
D = diag(linspace(10,1,n));
[Q,~] = qr(rand(n));
A = Q*D*Q';
P = rand(n);
B = P*(D/P);

v_exactA=Q(:,n);
v_exactB=P(:,n);
lam_exact=D(n,n);

x0A = v_exactA + rand(n,1)/n;
x0B = v_exactB + rand(n,1)/n;
e0 = lam_exact + 0.04;

v=[v_exactA  ; lam_exact];
[m,~]= size(v);

fA = @(v) [(A-v(m)*eye(n))*v(1:m-1); (1/2)*(v(1:m-1))'*(v(1:m-1))-1];
dfA = @(v) [ A-v(m)*eye(n), -v(1:m-1) ; v(1:m-1)' , 0];


ErrA = []; 
[~, outA2] = NewtonSolve(fA, dfA, x0A, e0, eps, 6);
lam_newton = outA2(n,:);
k = 1:length(lam_newton);
ErrA2=abs(outA2(length(outA2),:)-lam_exact);
vk = outA2(1:n,:);

for i = k
    ErrA = [ErrA abs(subspace(vk(:,i),v_exactA))];
end

hold on
plot(k, ErrA2, 'o-r')
plot(k, ErrA, 'o-r')
set(gca,'YScale','log')
legend('Newton val', 'Newton vec')
hold off
axis([1 6 10e-15 1])
xlabel('iteration')
ylabel('error')

%% Pour B

fB = @(v) [(B-v(m)*eye(n))*v(1:m-1); (1/2)*(v(1:m-1))'*(v(1:m-1))-1];
dfB = @(v) [ B-v(m)*eye(n), -v(1:m-1) ; v(1:m-1)' , 0];


ErrB = [];
[~, outB2] = NewtonSolve(fB, dfB, x0B, e0, eps, 6);
lam_newton = outB2(n,:);
k = 1:length(lam_newton);
ErrB2=abs(outB2(length(outB2),:)-lam_exact);
vk = outB2(1:n,:);

for i = k
    ErrB = [ErrB abs(subspace(vk(:,i),v_exactB))];
end
figure
hold on
plot(k, ErrB2, 'o-r')
plot(k, ErrB, 'o-r')
set(gca,'YScale','log')
legend('Newton val', 'Newton vec')
hold off
axis([1 10 10e-15 1])
xlabel('iteration')
ylabel('error')
