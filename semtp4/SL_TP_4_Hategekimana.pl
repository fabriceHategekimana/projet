%Exercice Exercice 2
/*Les expressions sont écrit sous la forme de tableau*/
/*Les instructions empty,pushE,topP,popP*/
evaluation1([E], X):- sousEvaluation1(E,[],X).
evaluation1([H|T], Y):- sousEvaluation1(H,[],X), evaluationHelper1(T,X,Y).
evaluationHelper1([],P,X):- sousEvaluation1([],P,X).
evaluationHelper1([E],P,X):- sousEvaluation1(E,P,X).
evaluationHelper1([H|T],P,Y):- sousEvaluation1(H,P,X), evaluationHelper1(T,X,Y).
%empty
sousEvaluation1(empty,P,X):- X= [].
%push
sousEvaluation1(pushE,P,X):- X= [e|P].
%top
sousEvaluation1(topP,[],X):- X=[].
sousEvaluation1(topP,[E],X):- X=[].
sousEvaluation1(topP,[H|T],X):- X=H.
%pop
sousEvaluation1(popP,[],X):- X=[].
sousEvaluation1(popP,[E],X):- X=[].
sousEvaluation1(popP,[H|T],X):- X=T.

%Exercice 2
evaluation2([E], X):- sousEvaluation2(E,[],X).
evaluation2([H|T], Y):- sousEvaluation2(H,[],X), evaluationHelper2(T,X,Y).
evaluationHelper2([],P,X):- sousEvaluation2([],P,X).
evaluationHelper2([E],P,X):- sousEvaluation2(E,P,X).
evaluationHelper2([H|T],P,Y):- sousEvaluation2(H,P,X), evaluationHelper2(T,X,Y).
%number
sousEvaluation2(N,P,X):- number(N), X= [N|P].
%swap
sousEvaluation2(swap,[N,NP|P],X):- X= [NP,N|P].
%dup
sousEvaluation2(dup,[N|P],X):- X= [N,N|P].
%drop
sousEvaluation2(drop,[N|P],X):- X=P.
%over
sousEvaluation2(over,[N,NP|P],X):- X= [NP,N,NP|P].
%+
sousEvaluation2(+,[N,NP|P],X):- S is N+NP, X= [S|P].
%-
sousEvaluation2(-,[N,NP|P],X):- S is N-NP, X= [S|P].
%*
sousEvaluation2(*,[N,NP|P],X):- S is N*NP, X= [S|P].
%/
sousEvaluation2(/,[N,NP|P],X):- S is N/NP, X= [S|P].

%Exercice3

%Exercice4

