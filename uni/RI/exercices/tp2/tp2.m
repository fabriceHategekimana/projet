%probabilité de faire une erreur
e= 0.5;

transition= [1-e e 0 0; 1-e 0 e 0; 1-e 0 0 e; 1 0 0 0];

xf= [1 e e^2 e^3]'
x0= [e 0 0 0 ]'

for i = [0:1:10]
    x= transition*x0
end
