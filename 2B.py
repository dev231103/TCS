import numpy as np

w11 = int(input("Weight w11 ="))
w12 = int(input("Weight w12 ="))
w21 = int(input("Weight w21 ="))
w22 = int(input("Weight w22 ="))
v1 =  int(input("Weight v1 ="))
v2 = int(input("Weight v2 = "))
theta = int(input("Enter threshold: "))

x1 = np.array([0,0,1,1])
x2 = np.array([0,1,0,1])
z = np.array([0,1,1,0])

y1 = np.zeros((4),)
y2 = np.zeros((4),)
y = np.zeros((4),)

con = 1

while con==1:
    zin1 = w11*x1 + w21*x2
    zin2 = w12*x1 + w22 * x2
    print(zin1)
    print(zin2)

    for i in range(0,4):
        if zin1[i]>=theta:
            y1[i] = 1
        else:
            y1[i]=0

        if zin2[i]>=theta:
            y2[i] = 1
        else:
            y2[i]=0

    yin = np.array([])
    yin = y1*v1 + y2 * v2

    for i in range (0,4):
        if yin[i] > theta:
            y[i] = 1
        else:
            y[i] = 0


    print("The net output")
    y =y.astype(int)

    print(y)
    print(z)

    if np.array_equal(y,z):
        con = 0
    else:
        print("The Net is not learning another set of dta i required")
        w11 = int(input("Weight w11 ="))
        w12 = int(input("Weight w12 ="))
        w21 = int(input("Weight w21 ="))
        w22 = int(input("Weight w22 ="))
        v1 = int(input("Weight v1 ="))
        v2 = int(input("Weight v2 = "))
        theta = int(input("Enter threshold: "))






