from numpy import load

data = load('properties_QM9.npz')
lst = data.files
for item in lst:
    print(item)
    #print(data[item])
