% Problem 1
close all

%%% a)
%% Task1
figure('Name','UniGauss-N=1000');
N = 1000;
m = 0;
v = 1;
x = GenUniGaus(N, m, v);
histogram(x,50)

disp("UniGauss-N=1000");
test1 = abs(m - sum(x)/N)
if (test1 < 0.01) ("abs(m - sum(x)/N) < 0.01")
else              ("abs(m - sum(x)/N) >= 0.01")
end
test2 = abs(v - sum((x-m).^2)/N)
if (test2 < 0.01) ("abs(v - sum(x-m).^2/N) < 0.01") 
else              ("abs(v - sum(x-m).^2/N) >= 0.01")
end

%% Task2
figure('Name','UniGauss-N=100000');
N = 100000;
m = 0;
v = 1;
x = GenUniGaus(N, m, v);
histogram(x,50)

disp("UniGauss-N=100000");
test1 = abs(m - sum(x)/N)
if (test1 < 0.01) ("abs(m - sum(x)/N) < 0.01")
else              ("abs(m - sum(x)/N) >= 0.01")
end
test2 = abs(v - sum((x-m).^2)/N)
if (test2 < 0.01) ("abs(v - sum(x-m).^2/N) < 0.01") 
else              ("abs(v - sum(x-m).^2/N) >= 0.01")
end

%% Task3
% explain the above investigation
% The Strong law of large numbers :
% X1...XN independant of same law
% P(lim n->inf sum(Xk)/n = E[X]) = 1
% States that the sample average converges
% almost surely to the expected value.
% So the more value there is, the smaller the difference gets
% the easier it is to get below a certain threshold.
% similarely, replacing Xk with (Xk-m)^2,
% we find that sum((Xk-m)^2)/n is a good estimator of
% E[(X-m)^2] = v

%%% b)
%% Task1
disp("MultiGauss Task 1");
N = 2;
m = [0 ; 0];
Cov = [1 0 ;
       0 1];

vec1 = GenCodeMultiGaus(N, m, Cov)

%% Task2
disp("MultiGauss Task 2");
N = 2;
m = [0 ; 1];
Cov = [1 0.8 ;
       0.8 1];

vec2 = GenCodeMultiGaus(N, m, Cov)

SampleSize = 10000; % sample size to aproximate density function
figure('Name','Marginal dist 2D');
plot_ = zeros(SampleSize, N);
for i=1:SampleSize
     plot_(i,:) = GenCodeMultiGaus(N, m, Cov);
end
scatterhist(plot_(:,1),plot_(:,2));
title('Task 2'); xlabel('x1'); ylabel('x2')

%% Task3
disp("MultiGauss Task 3");
N = 3;
m = [0 ; 0 ; 0];
Cov = [3.40 -2.75 -2.00 ;
       -2.75 5.50  1.50 ;
       -2.00 1.50  1.25];

vec3 = GenCodeMultiGaus(N, m, Cov)

figure('Name','Marginal dist 3D');
plot_ = zeros(SampleSize, N);
for i=1:SampleSize
     plot_(i,:) = GenCodeMultiGaus(N, m, Cov);
end
scatter3(plot_(:,1),plot_(:,2),plot_(:,3));

figure('Name','Marginal dist 2D 1,2');
scatterhist(plot_(:,1),plot_(:,2));
title('Task 3 1/2'); xlabel('x1'); ylabel('x2')
figure('Name','Marginal dist 2D 1,3');
scatterhist(plot_(:,1),plot_(:,3));
title('Task 3 1/3'); xlabel('x1'); ylabel('x3')
figure('Name','Marginal dist 2D 2,3');
scatterhist(plot_(:,2),plot_(:,3));
title('Task 3 2/3'); xlabel('x2'); ylabel('x3')

map = [0.894117647058824,0.101960784313725,0.109803921568627;0.215686274509804,0.494117647058824,0.721568627450980;0.301960784313725,0.686274509803922,0.290196078431373];
figure
histogram(plot_(:,1),50,'facecolor',map(1,:),'facealpha',.5,'edgecolor','none')
hold on
histogram(plot_(:,2),50,'facecolor',map(2,:),'facealpha',.5,'edgecolor','none')
histogram(plot_(:,3),50,'facecolor',map(3,:),'facealpha',.5,'edgecolor','none')
box off
axis tight
