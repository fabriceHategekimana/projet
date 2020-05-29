%% Exercice 2 : Itération du quotient de Rayleigh

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

ErrAEx2 = []; 
[~, outA2Ex2] = NewtonSolveEx2(fA, dfA, A, x0A, e0, eps, 6);
lam_newtonEx2 = outA2Ex2(n,:);
kEx2 = 1:length(lam_newtonEx2);
ErrA2Ex2=abs(outA2Ex2(length(outA2Ex2),:)-lam_exact);
vkEx2 = outA2Ex2(1:n,:);

for i = kEx2
    ErrAEx2 = [ErrAEx2 abs(subspace(vkEx2(:,i),v_exactA))];
end

hold on
plot(k, ErrA2, 'o-r')
plot(k, ErrA, 'x-r')
plot(kEx2, ErrA2Ex2, 'o-m')
plot(kEx2, ErrAEx2, 'x-m')
set(gca,'YScale','log')
legend('Newton val', 'Newton vec', 'RQI val', 'RQI vec')
hold off
axis([1 6 10e-15 1])
xlabel('iteration')
ylabel('error')

%% Partie B
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

ErrBEx2 = [];
[~, outB2Ex2] = NewtonSolveEx2(fB, dfB, B, x0B, e0, eps, 6);
lam_newtonEx2 = outB2Ex2(n,:);
kEx2 = 1:length(lam_newtonEx2);
ErrB2Ex2=abs(outB2Ex2(length(outB2Ex2),:)-lam_exact);
vkEx2 = outB2Ex2(1:n,:);

for i = kEx2
    ErrBEx2 = [ErrBEx2 abs(subspace(vkEx2(:,i),v_exactB))];
end


figure
hold on
plot(k, ErrB2, 'o-r')
plot(k, ErrB, 'x-r')
plot(kEx2, ErrB2Ex2, 'o-m')
plot(kEx2, ErrBEx2, 'x-m')
set(gca,'YScale','log')
legend('Newton val', 'Newton vec', 'RQI val', 'RQI vec')
hold off
axis([1 10 10e-15 1])
xlabel('iteration')
ylabel('error')
