import numpy as np
X = np.random.random((5,5))

for x in X:
    Z = (x-X.mean())/X.std()
    print(Z)
    