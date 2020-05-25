%Début de l'exercice 3
%(a) 
%On a la condition initiale suivante:
%dy= -50(y-cos(t)) pour t appartenant à [0,T] et y(0) = 0 où T=2
%La solution exacte est donnée par
%y= (2500/2501)(cos(t)-e^(-50t))+(50/2501)*sin(t) pour t appartenant à [0, T] où T=2 toujours

%Euler_Explicite(f, y0, t0, Nt, T);
%Euler_Implicite(f, df, t0, T, y0, Nt);

%On doit résoudre le problème avec la méthode d'Euler explicite Nt= 20, 40, 80, 160 (donc trois résultas)
%On doit résoudre le problème avec la méthode d'Euler implicite Nt= 20, 40, 80, 160 (donc trois résultas)
%Euler_Implicite(f, df, t0, T, y0, Nt);
f= @(t, y) (-50*(y-cos(t)));
df= @(t, y) (-50);
y0= 0;
t0= 0;
T= 2;
Nt= 20;
[T1, Y1]= Euler_Explicite(f, y0, t0, Nt, T);
[T2, Y2]= Euler_Implicite(f, df, t0, T, y0, Nt);
%plot(T1, Y1, "-", T2, Y2);
Nt= 40;
[T3, Y3]= Euler_Explicite(f, y0, t0, Nt, T);
[T4, Y4]= Euler_Implicite(f, df, t0, T, y0, Nt);
%plot(T3, Y3, "-", T4, Y4);
Nt= 80;
[T5, Y5]= Euler_Explicite(f, y0, t0, Nt, T);
[T6, Y6]= Euler_Implicite(f, df, t0, T, y0, Nt);
%plot(T5, Y5, "-", T6, Y6);
Nt= 160;
[T7, Y7]= Euler_Explicite(f, y0, t0, Nt, T);
[T8, Y8]= Euler_Implicite(f, df, t0, T, y0, Nt);
%plot(T7, Y7, "*", T8, Y8, "*");
%hold on

%On calcul aussi les valeur de de la solution exacte avec directement 160 points (donc un résultat)
solution_exacte= @(t)((2500/2501)*(cos(t)-e^(-50))+(50/2501)*sin(t));
x1= linspace(0, 2, 20);
y1= solution_exacte(x1);
%plot(x1, y1);

x2= linspace(0, 2, 40);
y2= solution_exacte(x2);
%plot(x2, y2);

x3= linspace(0, 2, 80);
y3= solution_exacte(x3);
%plot(x3, y3);

x4= linspace(0, 2, 160);
y4= solution_exacte(x4);
%plot(x4, y4);

%On calcul l'erreur entre les résultats trouvés et la vrai fonction
err_explicite1= max(norm(y1-Y1));
err_implicite1= max(norm(y1-Y2));

err_explicite2= max(norm(y2-Y3));
err_implicite2= max(norm(y2-Y4));

err_explicite3= max(norm(y3-Y5));
err_implicite3= max(norm(y3-Y6));

err_explicite4= max(norm(y4-Y7));
err_implicite4= max(norm(y4-Y8));

%Qu'est-ce qu'on observe lorsqu'on raffine le pas pour ces deux fonctions?
%-pour la methode d'Euler explicite, l'erreur de la fonction ne s'amélior pas.
%-pour la methode d'Euler implicite, l'erreur l'erreur est minimum et diminue à force de raffinement

%----------------------------------------------------------------

%(b) dy-ddy= 0 sur [0,1] x [0,T] et y(x, 0)= (x^2)(1-x) pour tout x appartenant à (0,1)

%voir la discussion de la discrétisation du problème dans la section 8.6 du polycopié

%On doit résoudre le problème avec la méthode d'Euler explicite Nx= 30 et Nt= 1000, 2000, 4000
%On doit résoudre le problème avec la méthode d'Euler implicite Nx= 30 et Nt= 1000, 2000, 4000
Nx= 20;
X= linspace(0, 1, Nx);
y= @(x) ((x.^2).*(1-x));
x0= y(X)';
dx= 1/Nx;
t0= 0;
T= 2; % pour un interval entre (t0, T)
tol= 1e-12;


Nt= 1000;
[T1, Y1]= Euler_Explicite_chaleur(x0, t0, Nt, T, dx);
[T2, Y2]= Euler_Implicite_chaleur(x0, t0, Nt, T, dx);
U1= Ex3b_ref(X', T1, tol);
%plot(T1, Y1, T2, Y2, T1, U1);
err_exp1= max(abs(U1-Y1));
err_imp1= max(abs(U1-Y2));

Nt= 2000;
[T3, Y3]= Euler_Explicite_chaleur(x0, t0, Nt, T, dx);
[T4, Y4]= Euler_Implicite_chaleur(x0, t0, Nt, T, dx);
U2= Ex3b_ref(X', T3, tol);
%plot(T3, Y3, T4, Y4, T2, U2);
err_exp2= max(abs(U2-Y3));
%err_imp2= max(abs(U2-Y4));

Nt= 4000;
[T5, Y5]= Euler_Explicite_chaleur(x0, t0, Nt, T, dx);
[T6, Y6]= Euler_Implicite_chaleur(x0, t0, Nt, T, dx);
%plot(T5, Y5, T6, Y6, T3, U3);
U3= Ex3b_ref(X', T5, tol);
err_exp3= max(abs(U3-Y5));
%err_imp3= max(abs(U3-Y6));

%Tracer les erreurs (sur une échelle logarithmique= semilog) par rapport au temps t pour les deux Méthodes et pour toutes les valeurs de Nt
%Comparer les deux méthodes
