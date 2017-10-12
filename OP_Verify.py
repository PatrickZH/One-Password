import hashlib
import numpy as np

eps = 0.00000001  # precision
hashfun = hashlib.sha512()

# load coefficients
op_data = np.load('op_data.npz')
coef = op_data['arr_0']
d = op_data['arr_1']
l = op_data['arr_2']
C = op_data['arr_3']

# verification
# input testing password
# pt = str("hello word").encode('utf-8')
pt = input("input test password: ")
pt = str(pt).encode('utf-8')


v = np.ones((1,d))      # all points
v = np.array(v, dtype='object')

# calculate the testing datapoint
seed = pt        # hash input
for i in range(0,d):    # iterate the hash process
    hashfun.update(seed)
    hi = hashfun.hexdigest()
    seed = str(hi).encode('utf-8')   # reset hash input
    hi = hi[0:max(l,len(hi))]
    v[0][i] = int(hi,16)    # save hash value

v = np.array(v, dtype='float64')

dot = np.dot(v, coef)
if np.abs( dot - C) < eps:
    print('True')
else:
    print('False')


print('finished')
