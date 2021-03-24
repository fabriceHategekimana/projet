l= [1,2,3,4,5,6]
a= 5

def third(l):
    return l[2]+9

print("State(%s, %s, inst)" % (l,a))
print(eval("third(%s)" % l))
