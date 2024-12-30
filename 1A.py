# Input for weight, bias, and input value
w = float(input("Enter the value for weight: "))
b = float(input("Enter the value for bias: "))
x = float(input("Enter the value for input: "))

def threshold_activation(yin):
    if yin >0:
        return 1
    else:
        return 0

y = b + (w*x)
print("The net input = ",y)

print("The net input after applying activation function = ",threshold_activation(y))