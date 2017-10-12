import hashlib
import numpy as np

# parameters
d = 100         # dimension of the super
l = 40          # precision of the span
C = 3.14159     # verification or encoding key information
hashfun = hashlib.sha512()

# input password
# p = str("hello word").encode('utf-8')
p = input("input password: ")
p = str(p).encode('utf-8')

v = np.ones((d,d))      # all points
v = np.array(v, dtype='object')

# register authentic hash value (datapoint)
seed = p                 # hash input
for i in range(0,d):    # iterate the hash process
    hashfun.update(seed)
    hi = hashfun.hexdigest()
    seed = str(hi).encode('utf-8')   # reset hash input
    hi = hi[0:max(l,len(hi))]
    v[0][i] = int(hi,16)    # save hash value

v = np.array(v, dtype='float64')

# generate other random points
v_det = 0
while v_det == 0:
    high = np.max(v)    # range of random values
    for i in range(1,d):
        for j in range(0,d):
            v[i][j] = high*np.random.rand(1)
    v_det = np.linalg.det(v)  # calculate the determinant of v to guarantee the existence of solution

# calculate the coefficients
v_inv = np.linalg.inv(v)
coef = np.dot( np.dot(v_inv, np.ones((d,1))), C)
np.savez("op_data", coef, d, l, C) # store the coefficients
print('finished')
