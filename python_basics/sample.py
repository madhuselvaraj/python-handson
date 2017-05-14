import numpy as np
a = np.array([1,2,3])
print(a)
print("------------------")

import time
import sys
s= range(1000)
print(sys.getsizeof(5)*len(s))
D = np.arange(1000)
print(D.size*D.itemsize)
print("------------------")

SIZE = 1000
L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)
start = time.time()
result = [(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)
start = time.time()
result = A1+A2
print((time.time()-start)*1000)

