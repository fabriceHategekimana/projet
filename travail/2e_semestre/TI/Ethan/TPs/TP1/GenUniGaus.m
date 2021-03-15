function x = GenUniGaus(N, m, v)
% Inputs:
% N: number of generated samples / codeword block-length (dimension)
% m: mean
% v: variance
% Outputs:
% x : generated sequence (codeword)

 x = randn(1,N)*sqrt(v) + m;
end
