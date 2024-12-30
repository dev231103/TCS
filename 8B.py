n = int(input("Enter the number of element: "))

list1=[]
for i in range(0,n):
    a = int(input(f"Enter element{i+1}"))
    list1.append(a)

search = int(input("Enter the element you want to seacrch in the list: "))

if search not in list1:
    print("Element not in list 1")
else:
    print("Element is present!")

