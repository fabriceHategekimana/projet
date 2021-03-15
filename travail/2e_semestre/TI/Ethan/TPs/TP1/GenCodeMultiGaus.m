function vec = GenCodeMultiGaus(N, m, Cov)
% Inputs:
% N: codeword block-length (dimension)
% m: mean vector mx
% Cov: covariance matrix Kxx
% Outputs:
% vec : generated sequence (codeword)
% (R = mvnrnd(mu,sigma,n))

%[T,err] = cholcov(Cov);
% if err ~= 0
%     error("cov is not positive semi-definite");
% end
% vec = T*vec + m;

vec = randn(N,1); % <=> GenUniGaus(N, 0, 1)
vec = Cov*vec + m;

end