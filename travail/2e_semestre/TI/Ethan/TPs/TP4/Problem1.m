%% Problem 1
var_x = 1;
N = 4;
corr_coef = [0.1 0.5 0.95];

for phi = corr_coef
    Corr = zeros(N);
    Corr(1,1) = 1;
    for i = 2:N
        Corr(i,2:i) = Corr(i-1,1:i-1);
        Corr(i,1) = phi*Corr(i-1,1);
    end
    Corr = Corr + tril(Corr,-1)';
    
    disp('phi');
    disp(phi)
    Kxx = var_x * Corr
    [U,D] = eig(Kxx) % <=> [U, D, ~] = svd(Kxx) in a other order
end

% Small corr_coef : data variabbility similar in every direction.
% Big corr_coef : data variability (<=> magnitude of spread) significantly
% highter in a direction.

