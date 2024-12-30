import math

n = int(input("Enter the number of input neurons"))
bias = float(input("Enter the Bias: "))

x=[]
w=[]
def binary_sigmoid(yin):
    y = 1/(1+math.exp(-yin))
    return y

def bipolar_sigmoid(yin):
    y = (2 / (1 + math.exp(-yin))) - 1
    return y

for i in range(0,n):
    a = float(input(f"Enter input {i}: "))
    x.append(a)
    b=float(input(f"Enter weight for input {i}: "))
    w.append(b)

y=bias


for i in range(0,n):
    y=y+ (w[i]*x[i])

print("The Calculated net input = ",y)

print("The net input on applying binary function = ",round(binary_sigmoid(y),3))
print("The net input on applying Bipolar function = ",round(bipolar_sigmoid(y),3))

