%% Nguyen Stéphane
% Problem set 1

% IMPORTANT:
% See report for more informations
% Not all the tasks are here (Problem 2), they're in the report
% I wrote back some comments in the report. Reason: easier to read in a
% pdf.

format compact
close all
warning('off')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Problem 1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% a)
% 
nBins=50;
N=1000;
m=0;
v=1; % variance, not standard deviation sigma.
vect=GenCodeUniGaus(N, m, v);

% Task 1.1 ----------
% Histogram plot
% Random variable Y=X*sigma + mu
% The expected value is mu and the standard deviation is sigma.
title("N realization of the random variable Y");
hist(vect,nBins);
histfit(vect,nBins);
grid on;
xlim([-3.5,3.5]);

% Task 1.2 ----------
% Verify the absolute errors for the mean and standard deviation
% and also variance.
% N=1'000
[err_mean,err_std,err_var]=errors_UniGaus(vect,m,v);
% They're sometimes lower than 0.01, otherwise they're greater than 0.01

% Now when changing to N=100'000
N2=100000;
vect2=GenCodeUniGaus(N2, m, v);
[err_mean2,err_std2,err_var2]=errors_UniGaus(vect2,m,v);

% They're closer to the real mean and the real standard deviation and
% variance

% Task 3
% Strong law of large numbers, see pdf report.

%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%
% b)

% Before starting, note that we need to use Cholesky decomposition
% to get the "standard deviation" (standard deviations on diagonals) if
% the covariance matrix is diagonal.
% We can use Cholesky decomposition because the covariance matrix is 
% symmetric definite positive.

% Affine random variable transform:

% Our case: Z=A*X + m_X with Z of sixe Nx1 and X the same size.
% Each element in the random vector X, X_i are independant or not
% from the other X_j with j!=i and the covariance matrix shows us that.

% So what is A ? Is it the Cholesky decomposition of K_xx the covariance
% matrix?
% If K_xx is diagonal, A is correctly L from K_xx=L*L'

% Proof that A is the L from the Cholesky decomposition:
% Compute Var(Z) and find that Var(Z)=A*R_zz*A'
% But R_zz=Var(Z)=Identity_N so Var(Z)=A*A' (Cholesky decomposition).


% (Careful) Now in these paragraphs I change the representations..
% In general (if we take the representation used from randn matlab page):
% Z is a m x n matrix, X is a m x n, L being the Cholesky decomposition
% of the square matrix K_xy.

% Z=X*L + m_X with K=LL' K_xy being the cross-covariance matrix.

% Considering X as a matrix containing n vectors of dimension m,IF
% they are all independant the different vectors follow an Univariate
% Normal Distributions, and their means are given by the vector m_X
% and their standard deviation for example for the X_i vector,
% it's the i'th element on the diagonal of the LL' Cholesky decomposition.


%-------------------------------------------------------------------------%
% Task 1 ----------
N=2;
m_x=[0 0]';
K_xx=eye(N);
vect_multi=GenCodeMultiGaus(N,m_x,K_xx) % Same as using GenCodeUniGaus
% Task 2 ----------
m_x_2=[0 1]';
K_xx_2=K_xx+0.8*K_xx([2,1],[1,2]);

vect_multi_2=GenCodeMultiGaus(N,m_x_2,K_xx_2) 
% Task 3 ----------
N1=3;
m_x_3=[0 0 0]';
K_xx_3=[3.4 -2.75 -2; -2.75 5.5 1.5;-2 1.5 1.25];

vect_multi_3=GenCodeMultiGaus(N1,m_x_3,K_xx_3)
%-------------------------------------------------------------------------%
% Task 4 ----------

% Scatter plot then also contour plot with marginal distributions.
% However, I'll only plot the marginal distributions for Task 3
% because 4D -> 2D is hard to represent (joint distribution).
%-------------------------------------------------------------------------%
% FOR TASK 2
%-------------------------------------------------------------------------%

% SCATTER HISTOGRAM
% I'll create many many samples CodeWords.
M=100000; % 100 thousand samples
data2=zeros(N,M); % of size NxM, M samples.

for j=1:M
    % for task 2
    data2(:,j)=GenCodeMultiGaus(N,m_x_2,K_xx_2); % for each column
    
end

% https://fr.mathworks.com/help/stats/scatterhist.html
x1=data2(1,:); % the first row
x2=data2(2,:); % the second row
figure

h=scatterhist(x1,x2,'Color','k'); % histogram, counts the number of occurences..

h(1).Title.String='Scatter plot';
grid on
% The two histograms
h(2).Children(1).FaceColor = 'b';
h(3).Children(1).FaceColor = 'r';

%-------------------------------------------------------------------------%
% CONTOUR PLOT for the joint probability density function.
% 2D !!
figure

subplot(2,2,2)
det_K_xx_2=det(K_xx_2);
p_x=@(X,Y) 1/sqrt((2*pi)^N *det_K_xx_2) * exp(-1/2*([X;Y]-m_x_2)'*(K_xx_2\([X;Y]-m_x_2)) );
cont=fcontour(p_x,[-3.5 3.5 -3.5 3.5]);
title("Contour plot of joint pdf");
ylabel("x_1")
ylabel("x_2")
grid on

%-------------------------------------------------------------------------%
% PROBABILITY DENSITY FUNCTIONS of each (Marginal distributions):
f_X = @(X)integral(@(Y)p_x(X,Y),-inf,inf,'ArrayValued',true);
% https://fr.mathworks.com/matlabcentral/answers/45443-marginal-density-from-a-joint-distribution
f_Y = @(Y)integral(@(X)p_x(X,Y),-inf,inf,'ArrayValued',true);


subplot(2,2,1)
fplot(f_Y);
title("pdf f_{X2}(x_2)")
xlabel("x_2")
ylabel("f_{X2}")
grid on

subplot(2,2,4)
fplot(f_X);
title("pdf f_{X1}(x_1)")
xlabel("x_1")
ylabel("f_{X1}")
grid on

% p_x=@(X,K_xx,m_x,N) 1/sqrt((2*pi)^N * det(K_xx)) * exp(-1/2*(x-m_x)'*(K_xx\(x-m_x)) );

% 3D plot
subplot(2,2,3)
fsurf(p_x,[-3.5 3.5 -3.5 3.5])

suptitle('Marginal Distributions for Task 2');

hold off

%-------------------------------------------------------------------------%
% FOR TASK 3
%-------------------------------------------------------------------------%
% T3 for task 3
% We have 3 arguments..
% det_K_xx_3=det(K_xx_3);
% p_x_T3=@(X,Y,Z) 1/sqrt((2*pi)^N1 * det_K_xx_3) * exp(-1/2*([X;Y;Z]-m_x_3)'*(K_xx_3\([X;Y;Z]-m_x_3)) );
% 
% 
% % PROBABILITY DENSITY FUNCTIONS of each (Marginal distributions):
% f_X_tmp = @(X,Z)integral(@(Y)p_x_T3(X,Y,Z),-inf,inf,'ArrayValued',true); % wrt Y
% f_X_T3= @(X) integral(@(Z) f_X_tmp(X,Z),-inf,inf,'ArrayValued',true); % wrt Z
% 
% %
% f_Y_tmp = @(Y,Z) integral(@(X)p_x_T3(X,Y,Z),-inf,inf,'ArrayValued',true); % wrt X
% f_Y_T3= @(Y) integral(@(Z) f_Y_tmp(Y,Z),-inf,inf,'ArrayValued',true); % wrt Z
% 
% %
% %f_Z_tmp = @(Y,Z) integral(@(X)p_x_T3(X,Y,Z),-inf,inf,'ArrayValued',true); % wrt X
% f_Z_T3= @(Z) integral(@(Y) f_Y_tmp(Y,Z),-inf,inf,'ArrayValued',true); % wrt Y


% xvec=linspace(-3.5,3.5,20);
% 
% % f_Y_tmp=f_Z_tmp..
% 
% 
% % From this we can compute the "wrt Z and wrt Y". for yvect_2 and yvect_3
% yvec_1 = arrayfun(f_X_T3,xvec);
% yvec_2 = arrayfun(f_Y_T3,xvec);
% yvec_3 = arrayfun(f_Z_T3,xvec);


% Univariate normal distribution.
f = @(x,v,m) 1/(sqrt(2*pi*v))*exp( (-(x-m).^2)/(2*v)); % v for variance

xvec=linspace(-5.5,5.5,100);

% Way faster than computing integrals..
yvec_1=f(xvec,K_xx_3(1,1),m_x_3(1));
yvec_2=f(xvec,K_xx_3(2,2),m_x_3(2));
yvec_3=f(xvec,K_xx_3(3,3),m_x_3(3));

figure
subplot(2,2,1)
plot(xvec,yvec_1)
title("pdf f_{X1}(x_1)")
xlabel("x_1")
ylabel("f_{X1}")
grid on

subplot(2,2,2)
plot(xvec,yvec_2)
title("pdf f_{X2}(x_2)")
xlabel("x_2")
ylabel("f_{X2}")
grid on

subplot(2,2,3)
plot(xvec,yvec_3)
title("pdf f_{X3}(x_3)")
xlabel("x_3")
ylabel("f_{X3}")
grid on

suptitle('Marginal Distributions for Task 3');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Problem 2
%--------------------------------------------------------------------------
% Investigations of orthonormal transforms.
rho=0.9;
m_z=[0 0]';
K_zz=[1 rho; rho 1];
[V,D]=eig(K_zz);

m_z4=[0 0 0 0]';
K_zz4=diag(linspace(1.5,0.2,4),0)+diag(linspace(0.8,-0.2,4-1),1)+diag(linspace(0.8,0.2,4-1),-1);% identity then add a bit of covariance.

[V4,D4]=eig(K_zz4);

% Marginal distributions then scatter plot
yvec_z1=f(xvec,K_zz(1,1),m_z(1));
yvec_z2=f(xvec,K_zz(2,2),m_z(2));

figure
subplot(2,1,1)
plot(xvec,yvec_z1)
title("pdf f_{X1}(x_1)")
xlabel("x_1")
ylabel("f_{X1}")
grid on

subplot(2,1,2)
plot(xvec,yvec_z2)
title("pdf f_{X2}(x_2)")
xlabel("x_2")
ylabel("f_{X2}")
grid on


suptitle('Marginal Distributions for Problem 2 Task 3 N=2');


% For N=4

% Marginal distributions then scatter plot
yvec_1z=f(xvec,K_zz4(1,1),m_z4(1));
yvec_2z=f(xvec,K_zz4(2,2),m_z4(2));
yvec_3z=f(xvec,K_zz4(3,3),m_z4(3));
yvec_4z=f(xvec,K_zz4(4,4),m_z4(4));

figure
subplot(2,2,1)
plot(xvec,yvec_1z)
title("pdf f_{X1}(x_1)")
xlabel("x_1")
ylabel("f_{X1}")
grid on

subplot(2,2,2)
plot(xvec,yvec_2z)
title("pdf f_{X2}(x_2)")
xlabel("x_2")
ylabel("f_{X2}")
grid on

subplot(2,2,3)
plot(xvec,yvec_3z)
title("pdf f_{X3}(x_3)")
xlabel("x_3")
ylabel("f_{X3}")
grid on

subplot(2,2,4)
plot(xvec,yvec_4z)
title("pdf f_{X4}(x_4)")
xlabel("x_4")
ylabel("f_{X4}")
grid on

suptitle('Marginal Distributions for Problem 2 Task 3 N=4');

% The scatter histogram now:

% SCATTER HISTOGRAM

M2=10000; % 10 thousand samples
data_22=zeros(2,M2); % of size 2xM2, M2 samples. 22for problem 2, N=2


for j=1:M
    % for task 2
    data_22(:,j)=GenCodeMultiGaus(2,m_z,K_zz); % for each column
    
end

% https://fr.mathworks.com/help/stats/scatterhist.html
x1_2=data_22(1,:); % the first row
x2_2=data_22(2,:); % the second row
figure

h2=scatterhist(x1_2,x2_2,'Color','k'); % histogram, counts the number of occurences..

h2(1).Title.String='Scatter plot Problem 2 N=2';
grid on
% The two histograms
h2(2).Children(1).FaceColor = 'b';
h2(3).Children(1).FaceColor = 'r';

% Investigation on the N=2 with matrix U and another matrix A orthonormal.
% K_new=D
random_matrix=rand(2);
% QR decomposition with m=n so I don't need to modify the matrices to
% get the reduced form and use A=Q.
[A,~]=qr(random_matrix);
% Just verify the rank of the matrix if = 2
while rank(A)~=2 % try to generate another matrix.. Just in case
    [A,~]=qr(random_matrix);
end

% Contour plot with original, A=U^T and A=Q

figure
% These 3 firsts are originals..
subplot(3,2,1)
det_K_zz=det(K_zz);
p_x=@(X,Y) 1/sqrt((2*pi)^2 *det_K_zz) * exp(-1/2*([X;Y])'*(K_zz\([X;Y])) ); % to simplify I don't write the m_z
cont1=fcontour(p_x,[-3.5 3.5 -3.5 3.5]);
title("Original");
ylabel("x_1")
ylabel("x_2")
grid on

subplot(3,2,3)
det_K_zz=det(K_zz);
p_x=@(X,Y) 1/sqrt((2*pi)^2 *det_K_zz) * exp(-1/2*([X;Y])'*(K_zz\([X;Y])) ); % to simplify I don't write the m_z
cont2=fcontour(p_x,[-3.5 3.5 -3.5 3.5]);
title("Original");
ylabel("x_1")
ylabel("x_2")
grid on

subplot(3,2,5)
det_K_zz=det(K_zz);
p_x=@(X,Y) 1/sqrt((2*pi)^2 *det_K_zz) * exp(-1/2*([X;Y])'*(K_zz\([X;Y])) ); % to simplify I don't write the m_z
cont3=fcontour(p_x,[-3.5 3.5 -3.5 3.5]);
title("Original");
ylabel("x_1")
ylabel("x_2")
grid on

% Decorrelation one with D for covariance matrix.
subplot(3,2,2)
det_D=det(D);
p_x=@(X,Y) 1/sqrt((2*pi)^2 *det_D) * exp(-1/2*([X;Y])'*(D\([X;Y])) ); % to simplify I don't write the m_z
cont4=fcontour(p_x,[-3.5 3.5 -3.5 3.5]);
title("A=U^T");
ylabel("x_1")
ylabel("x_2")
grid on

% "Random" orthogonal matrix
% To get the covariance, I compute, K_ro=A*K_zz*A'
K_ro=A*K_zz*A'; % ro for random orthogonal

subplot(3,2,4)
det_K_ro=det(K_ro);
p_x=@(X,Y) 1/sqrt((2*pi)^2 *det_K_ro) * exp(-1/2*([X;Y])'*(K_ro\([X;Y])) ); % to simplify I don't write the m_z
cont5=fcontour(p_x,[-3.5 3.5 -3.5 3.5]);
title("A=Q from QR decomposition");
ylabel("x_1")
ylabel("x_2")
grid on

% use the random matrix directly
% before that, verify that the determinant != 0 so we don't get det(K_r)=0
% If the absolute value of the determinant is within the range, I create
% another matrix because the determinant is bad.
tol=0.5; % if set at 0, we can see some weird transformations due to matrices being nearly singular.
% I generally put 0.5

while abs(det(random_matrix)) < tol % stops when we get non 0 % So we don't get matrices to be too close of being singular..
    random_matrix=rand(2);
end
% Create K_r and verify symmetric definite positive with Cholesky
K_r=random_matrix*K_zz*random_matrix';
[R,p]=chol(K_r); % see help chol
while p ~= 0
    random_matrix=rand(2);
    while abs(det(random_matrix)) < tol % same as above
        random_matrix=rand(2);
    end
    
    K_r=random_matrix*K_zz*random_matrix';
    [R,p]=chol(K_r); % see help chol
end

% contour plot..
subplot(3,2,6)
det_K_r=det(K_r);
p_x=@(X,Y) 1/sqrt((2*pi)^2 *det_K_r) * exp(-1/2*([X;Y])'*(K_r\([X;Y])) ); % to simplify I don't write the m_z
cont5=fcontour(p_x,[-3.5 3.5 -3.5 3.5]);
title("Random matrix A such that keep covariance matrix sym def pos");
ylabel("x_1")
ylabel("x_2")
grid on

suptitle('N=2 comparison between different linear transforms');

% Determinant of K_zz
disp("Determinant of K_zz")
disp(det(K_zz))

% Determinant of random A orthonormal
disp("Determinant of Covariance matrix with A orthonormal")
disp(det(K_ro))

% Determinant of random matrix with some assumptions
disp("Determinant of Covariance matrix with A random with some assumptions")
disp(det(K_r))

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% FUNCTIONS
function vect=GenCodeUniGaus(N, m, v)
    % "generates N realization of a ‘random variable’ x which is
    % distributed according to univariate Gaussian distribution of ‘mean’ m and ‘variance’
    % v = sigma^2"
    vect = ones(N,1)*m + randn(N,1)*sqrt(v); % sqrt to get the standard deviation.
    
end

function [err_mean,err_std,err_var]=errors_UniGaus(vect,m,v)
    [M,~]=size(vect); % outside this function, M corresponds to N
    % and N to 1.
    
    % M inside the function = N outside the function
    % N inside the function = 1 
    
    err_mean=abs(m-mean(vect)); % the real sample mean..
    
   
    err_std=abs(sqrt(v)-sqrt(1/M*sum( (vect-m).^2))); % I'll use this.
    % Also std(vect)=std(vect,0) and divides by M-1 instead of N (for N
    % I add the 1: std(X,1)).
    
    % std(vect,1) vs sqrt(1/N*sum( (vect-m).^2)) for std
    % There's a difference in the two. In the in-built function, they
    % compute the standard deviation front the variance but the variance
    % is computed using the SAMPLE MEAN ! -> check implementation of var.
    

    err_var=abs(v-1/M*sum( (vect-m).^2)); % Same reason as above, I'll use
    % 1/N * sum((vect-m).^2)) instead of err_var=abs(v-var(vect))
    
    % No square root when computing the variance
    % from realizations : 1/N * sum((vect-m).^2));
    
    fprintf("N=%d: \n",M);
    fprintf("Mean error: %.4f\t|",err_mean)
    fprintf("Std error: %.4f\t|",err_std)
    fprintf("Var error: %.4f\t\n",err_var)
    disp("error < 0.01 ?");
    fprintf("Mean error: %s\t|",mat2str(err_mean<0.01))
    fprintf("Std error: %s\t|",mat2str(err_std<0.01))
    fprintf("Var error: %s\t\n\n",mat2str(err_var<0.01))
end

function vect=GenCodeMultiGaus(N,m,Cov)
    % Only create ONE sample of dimension specified by N.
    
    % m being Nx1
    % Cov being NxN
    
    % Just to make it clear:
    K_xx=Cov;
    m_x=m;
    
    % I affine transform a random standard normal multivariate vector
    % into another one called X.
    % X is of size Nx1 and Z is of size Nx1
    
    % Z follows the standard normal multivariate vector
    % where K_zz=I_n=R_zz m_Z=0
    
    % K_xx=Var(X)=A*R_zz*A'=A*A'
    
    % Where A is used to transform : X=A*Z+m_x
    
    % Generate Z following the standard normal multivariate vector:
    % Each Z_i follows a normal univariate distribution.
    Z=GenCodeUniGaus(N, 0, 1);
    
    A=chol(K_xx,'lower'); % cholesky decomposition
    
    vect=A*Z+m_x;
end