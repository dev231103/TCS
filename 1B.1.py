import math

# Input for the number of neurons
n = int(input("Enter the number of input neurons: "))

# Initialize lists for inputs (x) and weights (w)
w = []
x = []

# Taking the value of inputs and their corresponding weights
for i in range(n):
    a = float(input(f"Enter the input x{i + 1}: "))  # Input
    x.append(a)
    b = float(input(f"Enter the weight w{i + 1}: "))  #
    w.append(b)

# Print the given inputs and weights
print("The given weights are: ")
print(w)
print("The given inputs are: ")
print(x)

# Calculate the net input (y = w1*x1 + w2*x2 + ... + wn*xn)
y = 0.0
for i in range(n):
    y += w[i] * x[i]

# Display the net input
print("The net input is: ")
print(round(y, 3))


# Activation Function (Step Function)
def step_activation(y):
    if y >= 0:  # If the net input is positive or zero, return 1
        return 1
    else:  # If the net input is negative, return 0
        return 0

# Apply the step activation function
output_step = step_activation(y)
print(f"Output after applying step activation function: {output_step}")

# Sigmoid Activation Function (Optional)


def sigmoid_activation(y):
    return 1 / (1 + math.exp(-y))  # Sigmoid formula


# Apply the sigmoid activation function (Optional)
output_sigmoid = sigmoid_activation(y)
print(f"Output after applying sigmoid activation function: {output_sigmoid: .3f}")
