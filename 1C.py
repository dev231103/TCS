import math

n = int(input("Enter the number of input neurons: "))
bias = float(input("Enter the value of Bias: "))
x=[]
w=[]

for i in range(1,n+1):
    a = float(input(f"Enter input {i}: "))
    x.append(a)
    b = float(input(f"Enter the weight for input {i}: "))
    w.append(b)

y = bias
print("The given weights are = ",w," And the Given Inputs are: ", x)

for i in range(0,n):
    y = y + (w[i]*x[i])

print("The calculated net input = ",y)
binary = 1/(1 +(math.exp(-y)))
print("Using the Binary Sigmoidal Function, the net input = ",round(binary,3))

bipolar = (2/(1+(math.exp(-y))))-1
print("Using the Bipolar Sigmoidal Function, the net input = ",round(bipolar,3))
