#creating an array and mainpulating some functions
import array as a
arr = a.array('i',[1,2,3,4,5,6])
print(arr)
arr.insert(2,111111)
print(arr)
print("first element",arr[0])
print("last element",arr[-1])
print("second element",arr[1])
print("third to fifth element",arr[2:5])
print("first to last element",arr[0:])
print("beigning to 3rd element",arr[:3])
print("printing all element",arr[:])
