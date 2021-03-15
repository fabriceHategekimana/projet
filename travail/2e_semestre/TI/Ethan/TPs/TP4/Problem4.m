%% Problem 4
close all

Means = [0.25 0.5]; % <=> Probability of success
Number_trials = [32 1024 5024];

Precision = 1000;
figure('Name','Hamming Weight')
tiledlayout(2,3);
for teta = Means
   for N = Number_trials
       nexttile
       hold on
       X = binornd(N, teta, 1, Precision);
       histogram(X, 'Normalization', 'pdf')
       
       pmf = zeros(1, Precision);
       x = linspace(1, N, Precision);
       mu = mean(X);    % ~ N*teta
       sigma = std(X);  % ~ sqrt(N*teta*(1-teta))
       for i = 1: Precision
           % pmf(1, k) = nchoosek(N,k)*teta^k*(1-teta)^(N-k); % worse approx
           pmf(1, i) = exp(-(x(i)-mu)^2/(2*sigma^2))/(sigma*sqrt(2*pi));
       end
       plot(x, pmf(1,:))
       hold off
       
       title("N = " + N)
       xlabel('omega')
       ylabel('pw')
       xlim([0 N])
   end
end

% Observations:

% the Hamming weight has the same shape as the binomial (/Gaussian) pmf

% The smaller teta is the smaller the mean gets
% The closer teta gets to 0.5, the highter the variance gets.

% The bigger N is the peakier the shape gets (<= variance).
% The bigger N is the less the sequence will end on the same exact number,
% and so the lower pw peaks (teta = 1/4 is a bit highter because less variance)
