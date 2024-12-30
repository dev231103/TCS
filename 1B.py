import math

# Input for bias 
bias = float(input("Enter the value of bias: "))

# Input for the number of neurons (inputs)
n = int(input("Enter the number of input neurons: "))

# Initialize lists for weights and inputs
w = []  # List for weights
x = []  # List for inputs

# Taking the value of inputs and their corresponding weights
for i in range(n):
    a = float(input(f"Enter the input x{i+1}: "))  # Input values (x)
    x.append(a)
    b = float(input(f"Enter the weight w{i+1}: "))  # Weights (w)
    w.append(b)

# Print the given inputs and weights
print("The given weights are: ")
print(w)
print("The given inputs are: ")
print(x)

# Calculate the net input (y = bias + w1*x1 + w2*x2 + ... + wn*xn)
y = bias
for i in range(n):
    y += w[i] * x[i]

# Display the net input
print("The net input is: ")
print(round(y, 3))

# Step activation function
def step_activation(y):
    if y >= 0:  # If net input is positive or zero, return 1
        return 1
    else:  # If net input is negative, return 0
        return 0

# Apply the step activation function
output_step = step_activation(y)
print(f"Output after step activation function: {output_step}")

# Sigmoid Activation Function (Optional)
def sigmoid_activation(y):
    return 1 / (1 + math.exp(-y))  # Sigmoid formula

# Apply the sigmoid activation function (Optional)
output_sigmoid = sigmoid_activation(y)
print(f"Output after sigmoid activation function: {output_sigmoid:.3f}")
