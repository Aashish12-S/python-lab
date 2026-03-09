# 1). positive indexing
from array import array

arr=array('i', [10,20,30,40,50])

print(arr[0]) 
print(arr[2])
print(arr[4])

print("*"*30)

# 2). negative indexing
from array import array

arr=array('i', [10,20,30,40,50])

print(arr[-1])
print(arr[-3])
print(arr[-5])

print("*"*30)

# 3). modify elements using indexing
from array import array

arr=array('i', [10,20,30,40,50])

arr[2]=35
print(arr)