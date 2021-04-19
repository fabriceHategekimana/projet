#HATEGEKIMANA Fabrice
from distances import *
from k_nearest_neighbor import KNearestNeighbor

X_train= np.array([[1,1],[1,3],[3,1],[3,3],[0,0],[1,0]])
X_test=  np.array([[2,2],[1.1,1.1]])
y_train= np.array([[0,1,1,1,0,0]])

dists= compute_euclidean_dist_two_loops(X_train, X_test)
print(dists)
# [[1.41421356 1.41421356 1.41421356 1.41421356]]

# Create a k-NN classifier instance. 
# Remember that training a k-NN classifier is a noop: 
# the Classifier simply remembers the data and does no further processing 
knn = KNearestNeighbor()
knn.train(X_train, y_train)

# Don't forget to implement the following method in k_nearest_neighbor.py
# We use k = 1 (which is the Nearest Neighbor).
y_test_pred = knn.predict_labels(dists, k=3)

print(y_test_pred)

# Compute and print the fraction of correctly predicted examples
#num_correct = np.sum(y_test_pred == y_test)
#accuracy = (float(num_correct) / num_test)*100
#print('Got %d / %d correct => accuracy: %f' % (num_correct, num_test, accuracy))
