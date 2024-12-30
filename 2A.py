n = int(input("Enter the number of inputs: "))
theta=1
x1=[]
x2=[]

for i in range(0,n):
    a = int(input("Enter the input x1: "))
    x1.append(a)
    b = int(input("Enter the input x2: "))
    x2.append(b)

print("x1 = ",x1,"\n x2 = ",x2,"and the value of theta(threshold) is 1")

print("Case 1: The Net input when weights w1=w2=1: ")
case_y1=[]
case_yin1=[]
w1=w2=1

print("x1  w1   x2  w2    case_y1    case_yin1")
for i in range(0,n):
    case_y1.append((x1[i]*w1)+(x2[i]*w2))
    if case_y1[i] >= theta:
        case_yin1.append(1)
    else:
        case_yin1.append(0)

    print(f"{x1[i]}   {w1}     {x2[i]}   {w2}     {case_y1[i]}              {case_yin1[i]}")


print("Case 2: The Net input when weights w1=1 w2=-1: ")
case_y2=[]
case_yin2=[]
w1=1
w2=-1

print("x1  w1   x2  w2    case_y2    case_yin2")
for i in range(0,n):
    case_y2.append((x1[i]*w1)+(x2[i]*w2))
    if case_y2[i] >= theta:
        case_yin2.append(1)
    else:
        case_yin2.append(0)

    print(f"{x1[i]}   {w1}     {x2[i]}   {w2}     {case_y2[i]}              {case_yin2[i]}")