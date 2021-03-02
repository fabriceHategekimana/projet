import numpy as np

### Exercise 1
# The cosine function has the following infinite product representation
# 
# $$\cos x = \prod_{k=1}^{\infty}(1 - \frac{4 x^2}{\pi (2k -1)^2})$$
# 
# Write a function called cos_product which takes input parameters x and returns the Nth partial product
# 
# $$\prod_{k=1}^{\infty}(1 - \frac{4 x^2}{\pi (2k -1)^2})$$
# 
def cos_product(x,N):
    "Compute the product \\prod_{k=1}^N (1 - 4x^2/(pi^2 (2k - 1)^2)."
    prod= 1
    for i in range(N):
        k= i+1
        prod= prod*(1-(4*np.power(x,2)/(np.power(np.pi,2)*np.power(2*k-1,2))))
    print(prod)

    # Verify your function using values for which you know the result. For example, $\cos(0) = 1$ , $\cos(\pi) = -1$ 
cos_product(0,10)

cos_product(np.pi,1000)

