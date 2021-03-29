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

    mean= np.array([n.sum(axis=0)/len(n) for n in points_by_class])

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

    total= []
    for xtuple in X:
        prob= []
        for i in range(len(prior)):
            prob.append(prior[i]*np.sum(normal_distribution(xtuple, mean[i], std[i])))
        prob= np.array(prob)
        total.append((np.where(prob == np.max(np.array(prob))))[0])

    y_pred= np.array(total)

    return y_pred

#X= np.arange(81).reshape(9,9)
#y= np.array([2, 1, 3, 3, 2, 1, 1, 3, 2])
#X= np.arange(9).reshape(3,3)
#y= np.array([2, 3, 2])

#X= np.arange(4).reshape(2,2)

#X= np.array([[1,2]])
#prior= np.array([0.2,0.8])
#mean= np.array([[1,2],[0,0]])
#std= np.array([[0.5,0.5],[1,1]])

#print(X)
#print(y)

#predict(X, prior, mean, std)
#train_nb(X,y)
