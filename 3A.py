import numpy as np

x1 = np.array([1,1,1,-1,1,-1,1,1,1])
x2 = np.array([1,1,1,1,-1,1,1,1,1])

b =0
y = np.array([1,-1])

wtold=np.zeros((9),dtype=int)
wtnew = np.zeros((9),dtype=int)

print("For Target 1:")
for i in range(0,9):
    wtold[i]=wtold[i] + x1[i]*y[0]
    wtnew=wtold
    b=b+y[0]

print("For Target 2:")
for i in range(0,9):
    wtold[i]=wtold[i] + x2[i]*y[1]
    wtnew=wtold
    b=b+y[1]

print("New Weights", wtnew)
print("New Bias ",b)