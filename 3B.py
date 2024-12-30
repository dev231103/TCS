import numpy as np
import time

x = np.zeros((3),)
weights = np.zeros((3),)
desired = np.zeros((3),)
actual = np.zeros((3),)

for i in range(0,3):
    x[i]= float(input("Enter initial inputs :"))
for i in range(0,3):
    weights[i]= float(input("Enter initial weights :"))

for i in range(0,3):
    desired[i]= float(input("Enter initial desired output :"))

a = float(input("Enter learning rate"))

actual = np.multiply(x,weights)
print("Initial")
print(actual)
print(desired)
while True:
    if np.array_equal(actual,desired):
        break
    else:
        for i in range(0,3):
            weights[i] = weights[i] + a *(desired[i] - actual[i])*x[i]
    actual = np.multiply(x,weights)
    print("*"*30)
    print("Updated weights: ",weights)
    print("Actual Output: ",actual)
    print("Desired",desired)


print("Final")
print("Updated weights: ", weights)
print("Actual Output: ", actual)
print("Desired", desired)
