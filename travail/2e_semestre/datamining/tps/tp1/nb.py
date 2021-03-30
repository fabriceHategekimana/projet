import numpy as np



def train_nb(X, y):
    """
    Train the Naive Bayes classifier. For NB this is just
    computing the necessary probabilities to perform classification
    1. The probability P(ci) for every class -> prior (the prior comes from the distribution of labels)
    2. The mean and std -> mean, std (The mean and variance are applied to each feature in the input data X)

    Inputs:
    - X: A numpy array of shape (num_train, D) containing the training data
    consisting of num_train samples each of dimension D.
    - y: A numpy array of shape (N,) containing the training labels, where
        y[i] is the label for X[i].

    Outputs:
    - prior : list with length equal to the number of classes
    - mean : A numpy array of shape (num_classes, num_features)
    - std  : A numpy array of shape (num_classes, num_features)

    **** train() should be run with X as training data
    """
    # use list comprehension

    # Separate training points by class
    unique_y = np.unique (y)
    points_by_class = np.array([np.array([x for x, t in zip (X, y) if t == c]) for c in unique_y])

    #########################################################################
    # TODO:                                                                 #
    # compute class prior                                                   #
    #########################################################################
    
    #We get the probability of each distinct values by a division: nb_of_occurence/total_nb_of value
    prior = np.array([len(n)/len(y) for n in points_by_class])

    #########################################################################
    # TODO:                                                                 #
    # Estimate mean and std for each class / feature                        #
    #########################################################################
    
    #for each distinct value of y, we just compute the mean by doing the sum
    #of the coresponding tuple x divided by the total number of tuples
    mean= np.array([n.sum(axis=0)/len(n) for n in points_by_class])
    
    #for the standar deviation, we just do the same as the mean but we apply (x-mean)**2
    #for each column
    std = np.sqrt(np.array([((xs-m)**2).sum(axis=0)/len(xs) for xs,m in zip(points_by_class,mean)]))

    return prior, mean, std

def normal_distribution(x, mean, std):
    """
    Compute normal distribution
    output size: (num_input_data, num_features)

    """
    #########################################################################
    # TODO : Compute normal distribution                                    #
    #########################################################################
    
    #we just apply for each column the computation of the normal distributions
    #with the given mean and standard deviation: Normal(xij, meanij, stdij)
    normal= (1/std*(np.sqrt(2*np.pi))) * np.exp(-((x-mean)**2)/(2*(std**2)))

    return normal


def predict(X, prior, mean, std):
    """
    Using the distributions from before, predict labels for test data (or train data) using this classifier.
    We predict the class of the data maximizing the likelihood or you can
     maximize the log likelihood to make it numericaly more stable.
     (This is possible since f(x)=log(x) is a monotone function)

    You have to compute:
    - Compute the conditional probabilities  P(x|c) (or log P(x|c) )
    - The posterior (if you compute the log likelihood the product  becomes sum)
    - Make the prediction

    Inputs:
    - X: A numpy array of shape (num_test, D) containing test data consisting
        of num_test samples each of dimension D.
    - prior, mean, std: output of train() function

    Returns:
    - y_pred : A numpy array of shape (num_test,) containing predicted labels for the
    test data, where y[i] is the predicted label for the test point X[i].

    *** predict() should be run with X as test data, based on mean and variance and prior from the training data
        (to compute the training accuracy run with X as train data)

    """
    # use list comprehension

    #################################################################################
    #        # Compute the conditional probabilities  P(x|c)                        #
    #             # There are three loops in the code.                              #
    #             # 1. through each sample.                                         #
    #             # 2. through each class.                                          #
    #             # 3. through each attribute and apply the Normal/ logNormal distribution. #
    #        # Compute the posterior                                                #
    #                                                                               #
    #################################################################################


    #########################################################################
    #                           TODO
    #             compute the posterior and predict                         #
    # - hint for prediction: class having the biggest probability[argmax()] #
    #########################################################################

    #we define the total list tha will contain the index of the most probable y
    total= []
    #for each x from the testing set:
    for xtuple in X:
        #the prob list will contain the probability of each y for the given tuple
        prob= []
        #computing the probability of each column and finally sum them and do a
        #a multiplication by the prior of y
        for i in range(len(prior)):
            prob.append(prior[i]*np.sum(normal_distribution(xtuple, mean[i], std[i])))
        #formating the prob table
        prob= np.array(prob)
        #append the index of the most probable y from the prob array
        total.append((np.where(prob == np.max(np.array(prob))))[0][0])

    y_pred= np.array(total)

    return y_pred

def train_nb2(X, y):
    # Separate training points by class
    unique_y = np.unique (y)
    points_by_class = np.array([np.array([x for x, t in zip (X, y) if t == c]) for c in unique_y])
    
    #We get the probability of each distinct values by a division: nb_of_occurence/total_nb_of value
    prior = np.array([len(n)/len(y) for n in points_by_class])

    # Compute the probability of each instance of each column from the training set x
    proba= []
    # for each value of y:
    for pbc in points_by_class:
        tab= []
        #for each column:
        for i in range(pbc.shape[1]):
            column= list(pbc[:,i])
            unique= np.unique(column)
            #creating a dictionnary that will contain the probability of each values
            #from each column
            d= {}
            for u in unique:
                d[u]= column.count(u)/len(column)
            #we put the dictionnary to the list
            tab.append(d)
        proba.append(tab)

    return prior, proba

def predict2(X, prior, proba):
    #of each x from the testing set
    final= []
    #for each tuple in the testing set
    for xtuple in X:
        prob= []
        #for for each distinct value y
        for i in range(len(prior)):
            somme= 0
            #compute the probability of each column
            for j in range(len(xtuple)):
                #finally do a summation 
                somme += proba[i][j].get(xtuple[j], 0)
            #and multiply by the prior (divided by the number of column)
            prob.append(prior[i]*somme/len(xtuple))
        #formating prob
        prob= np.array(prob)
        #put the most probable y
        final.append((np.where(prob == np.max(prob)))[0][0])
        
    return final

