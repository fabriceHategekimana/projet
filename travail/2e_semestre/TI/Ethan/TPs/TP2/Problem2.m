% Problem 2
close all

SampleSize = 1000;
N = 2;
mu = zeros(N,1);
Kxx = [1   0.8;
       0.8   1];

plot_y = zeros(SampleSize, N);
figure('Name','Effect of Randomization, Y=X+Z')
tiledlayout(2,3);
    
for varz = [0 0.1 0.5 1 2 10]
    for i=1:SampleSize
        x = GenCodeMultiGaus(N, mu, Kxx);
        z = GenCodeMultiGaus(N, mu, eye(N)*varz);

        plot_y(i,:) = x + z;  
    end

    cc = corrcoef(plot_y(:,1), plot_y(:,2));

    nexttile
    scatter(plot_y(:,1), plot_y(:,2));
    title_ = "Var(z)=" + varz + " corr=" + cc(2,1);
    title(title_)
    xlabel("y1");
    ylabel("y2");
    axis equal
end

% Progressively the diagonal line/elipse become more big and stretched like a circle.
% where 0.1 changes almost imperceptively the correlation, around 8
% the corrcoef get below the error due to randomess. 
