% Problem 2
close all;

%% Task 1
% E[x] = A*E[z] = A*0 = 0
% Cov Matrix = Kxx = A*Kzz*A'

%% Task 2
% a)
% Kxx = A*Kzz*A'
% with A = U'  => U'*Kzz*U
% Kzz = U*E*U' => U'U*E*U'*U = E = diag(eigenValues)

% b)
% A random orthogonal -> reflexion and/or rotation 
% of the Marginal Distribution
% Au = U' => Kxx = E, rotated the such that the more stretch is vertical  


% Task 3
N = 2;

Kzz = rand(N); Kzz = Kzz*Kzz' % sym def positive
A = orth(rand(N))
[U, E] = eig(Kzz); Au = U';

SampleSize = 10000;
plot_x = zeros(SampleSize, N);
plot_xu = zeros(SampleSize, N);
plot_z = zeros(SampleSize, N);
for i=1:SampleSize
    z = GenCodeMultiGaus(N, 0, Kzz);
    x = A*z;
    xu = Au*z;
    
    plot_x(i,:) = x; 
    plot_xu(i,:) = xu; 
    plot_z(i,:) = z; 
    
    
end
% Multifigure doesn't work on those plot and instruction ask for 2D plot,
% sorry !
figure('Name','N=2 Marginal dist comparsion z');
scatterhist(plot_z(:,1),plot_z(:,2));
title('N=2 - z'); xlabel('z1'); ylabel('z2')
axis equal
figure('Name','N=2 Marginal dist comparsion x');
scatterhist(plot_x(:,1),plot_x(:,2));
title('N=2 - x'); xlabel('x1'); ylabel('x2')
axis equal
figure('Name','N=2 Marginal dist comparsion A = U''');
scatterhist(plot_xu(:,1),plot_xu(:,2));
title('N=2 - A=U'''); xlabel('xu1'); ylabel('xu2')
axis equal

N = 4;

Kzz = rand(N); Kzz = Kzz*Kzz' % sym def positive
A = orth(rand(N))
[U, E] = eig(Kzz); Au = U';

SampleSize = 10000;
plot_x = zeros(SampleSize, N);
plot_xu = zeros(SampleSize, N);
plot_z = zeros(SampleSize, N);
for i=1:SampleSize
    z = GenCodeMultiGaus(N, 0, Kzz);
    x = A*z;
    xu = Au*z;
    
    plot_x(i,:) = x; 
    plot_xu(i,:) = xu; 
    plot_z(i,:) = z; 
    
    
end
% Multifigure doesn't work on those plot and instructions ask for 2D plot,
% sorry++ !
figure('Name','N=4 Marginal dist comparsion z, z1/z2');
scatterhist(plot_z(:,1),plot_z(:,2));
title('N=4 - z'); xlabel('z1'); ylabel('z2')
axis equal
figure('Name','N=4 Marginal dist comparsion z, z1/z3');
scatterhist(plot_z(:,1),plot_z(:,3));
title('N=4 - z'); xlabel('z1'); ylabel('z3')
axis equal
figure('Name','N=4 Marginal dist comparsion z, z1/z4');
scatterhist(plot_z(:,1),plot_z(:,4));
title('N=4 - z'); xlabel('z1'); ylabel('z4')
axis equal
figure('Name','N=4 Marginal dist comparsion z, z2/z3');
scatterhist(plot_z(:,2),plot_z(:,3));
title('N=4 - z'); xlabel('z2'); ylabel('z3')
axis equal
figure('Name','N=4 Marginal dist comparsion z, z2/z4');
scatterhist(plot_z(:,2),plot_z(:,4));
title('N=4 - z'); xlabel('z2'); ylabel('z4')
axis equal
figure('Name','N=4 Marginal dist comparsion z, z3/z4');
scatterhist(plot_z(:,3),plot_z(:,4));
title('N=4 - z'); xlabel('z3'); ylabel('z4')
axis equal

figure('Name','N=4 Marginal dist comparsion x, x1/x2');
scatterhist(plot_x(:,1),plot_x(:,2));
title('N=4 - x'); xlabel('x1'); ylabel('x2')
axis equal
figure('Name','N=4 Marginal dist comparsion x, x1/x3');
scatterhist(plot_x(:,1),plot_x(:,3));
title('N=4 - x'); xlabel('x1'); ylabel('x3')
axis equal
figure('Name','N=4 Marginal dist comparsion x, x1/x4');
scatterhist(plot_x(:,1),plot_x(:,4));
title('N=4 - x'); xlabel('x1'); ylabel('x4')
axis equal
figure('Name','N=4 Marginal dist comparsion x, x2/x3');
scatterhist(plot_x(:,2),plot_x(:,3));
title('N=4 - x'); xlabel('x2'); ylabel('x3')
axis equal
figure('Name','N=4 Marginal dist comparsion x, x2/x4');
scatterhist(plot_x(:,2),plot_x(:,4));
title('N=4 - x'); xlabel('x2'); ylabel('x4')
axis equal
figure('Name','N=4 Marginal dist comparsion x, x3/x4');
scatterhist(plot_x(:,3),plot_x(:,4));
title('N=4 - x'); xlabel('x3'); ylabel('x4')
axis equal

figure('Name','Marginal dist comparsion A = U'', xu1/xu2');
scatterhist(plot_xu(:,1),plot_xu(:,2));
title('N=4 - A=U'''); xlabel('xu1'); ylabel('xu2')
axis equal
figure('Name','Marginal dist comparsion A = U'', xu1/xu3');
scatterhist(plot_xu(:,1),plot_xu(:,3));
title('N=4 - A=U'''); xlabel('xu1'); ylabel('xu3')
axis equal
figure('Name','Marginal dist comparsion A = U'', xu1/xu4');
scatterhist(plot_xu(:,1),plot_xu(:,4));
title('N=4 - A=U'''); xlabel('xu1'); ylabel('xu4')
axis equal
figure('Name','Marginal dist comparsion A = U'', xu2/xu3');
scatterhist(plot_xu(:,2),plot_xu(:,3));
title('N=4 - A=U'''); xlabel('xu2'); ylabel('xu3')
axis equal
figure('Name','Marginal dist comparsion A = U'', xu2/xu4');
scatterhist(plot_xu(:,2),plot_xu(:,4));
title('N=4 - A=U'''); xlabel('xu2'); ylabel('xu4')
axis equal
figure('Name','Marginal dist comparsion A = U'', xu3/xu4');
scatterhist(plot_xu(:,3),plot_xu(:,4));
title('N=4 - A=U'''); xlabel('xu3'); ylabel('xu4')
axis equal

%%% 1D - Comparison
map = [0.894117647058824,0.101960784313725,0.109803921568627;0.215686274509804,0.494117647058824,0.721568627450980;0.301960784313725,0.686274509803922,0.290196078431373;0.596078431372549,0.305882352941177,0.639215686274510];
figure('Name','N=4 - z 1D comparison'); title('N=4 - z');
hold on
histogram(plot_z(:,1),50,'facecolor',map(1,:),'facealpha',.5,'edgecolor','none')
histogram(plot_z(:,2),50,'facecolor',map(2,:),'facealpha',.5,'edgecolor','none')
histogram(plot_z(:,3),50,'facecolor',map(3,:),'facealpha',.5,'edgecolor','none')
histogram(plot_z(:,4),50,'facecolor',map(4,:),'facealpha',.5,'edgecolor','none')
box off
legend('z1', 'z2', 'z3', 'z4')
axis tight

map = [0.894117647058824,0.101960784313725,0.109803921568627;0.215686274509804,0.494117647058824,0.721568627450980;0.301960784313725,0.686274509803922,0.290196078431373;0.596078431372549,0.305882352941177,0.639215686274510];
figure('Name','N=4 - x 1D comparison'); title('N=4 - x');
hold on
histogram(plot_x(:,1),50,'facecolor',map(1,:),'facealpha',.5,'edgecolor','none')
histogram(plot_x(:,2),50,'facecolor',map(2,:),'facealpha',.5,'edgecolor','none')
histogram(plot_x(:,3),50,'facecolor',map(3,:),'facealpha',.5,'edgecolor','none')
histogram(plot_x(:,4),50,'facecolor',map(4,:),'facealpha',.5,'edgecolor','none')
box off
legend('x1', 'x2', 'x3', 'x4')
axis tight

map = [0.894117647058824,0.101960784313725,0.109803921568627;0.215686274509804,0.494117647058824,0.721568627450980;0.301960784313725,0.686274509803922,0.290196078431373;0.596078431372549,0.305882352941177,0.639215686274510];
figure('Name','N=4 - A=U'' 1D comparison'); title('N=4 - A=U''');
hold on
histogram(plot_xu(:,1),50,'facecolor',map(1,:),'facealpha',.5,'edgecolor','none')
histogram(plot_xu(:,2),50,'facecolor',map(2,:),'facealpha',.5,'edgecolor','none')
histogram(plot_xu(:,3),50,'facecolor',map(3,:),'facealpha',.5,'edgecolor','none')
histogram(plot_xu(:,4),50,'facecolor',map(4,:),'facealpha',.5,'edgecolor','none')
box off
legend('xu1', 'xu2', 'xu3', 'xu4')
axis tight
%% Task 4 
% |Det(Kxx)| = |Det(A*Kzz*A')| = |Det(A) * Det(Kzz) * Det(A')|
% = |Det(A)*Det(A')*Det(Kzz)| = |Det(A*A') * Det(Kzz)|
% = |Det(I) * Det(Kzz)| = |1 * Det(Kzz)| 
% = |Det(Kzz)|
