def overlapping(list1,list2):
    c = len(list1)
    d = len(list2)
    print("length of list c: ",c, " and of d",d)

    for i in range(c):
        for j in range(d):
            if list1[i]==list2[j]:
                return True
            else:
                return False


list1 =[]
list2=[]

n = int(input("Enter the number of elements in list1: "))

for i in range(0,n):
    x = int(input(f"Enter the element {i+1} "))
    list1.append(x)

m = int(input("Enter the number of elements in list1: "))

for i in range(0,m):
    y = int(input(f"Enter the element {i+1} "))
    list2.append(y)

if overlapping(list1,list2):
    print("The list are overlapping")
else:
    print("Not Overlapping")