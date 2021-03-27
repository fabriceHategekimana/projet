# Write a function called count_transitions_for which takes 1 inputx x, a 1-dimensional vector of True and False and count the number of “False to True” transitions in the sequence with a for loop and a function called count_transitions without a for loop.
import numpy as np

def count_transitions_for(x):
    count = 0
    last= None
    for i in range(len(x)):
        if x[i] == False:
            last= False
        else:
            if last == False:
                count= count+1
            last= True
    return count

def count_transitions(x):
    count= 0
    return count

np.random.seed(444)
vect1 = np.random.choice([False, True], size=100000)
vect1
#count_transitions(vect1)
#myvect= np.array([True, False, True, False, True, True])
print(count_transitions_for(vect1))

