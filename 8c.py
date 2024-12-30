
new_list1 = [1,2,3,'a']
new_list2 = [1,4,3,'b']

new_tuple1 = (1,3,4,'a')
new_tuple2 =(1,3,4,'b')

print("The type of new_list1 = ",type(new_list1))
print("The type of new_list2 = ",type(new_list2))
print("The type of new_tuple1 = ",type(new_tuple1))
print("The type of new_tuple2 = ",type(new_tuple2))

if type(new_list1) is not type(new_tuple1):
    print("new_list1 and new_tuple 1 are not of same type")
else:
    print("Same Type")

if type(new_list2) is not type(new_list1):
    print("new_list1 and new_list 1 are not of same type")
else:
    print("Same Type")