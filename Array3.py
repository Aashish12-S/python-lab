# 1). Basic slices
from array import array

arr=array('i', [10,20,30,40,50])

print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[:])

print("*"*30)

# 2). Slices with step
from array import array

arr=array('i', [10,20,30,40,50,60])

print(arr[::2])
print(arr[1::2])
print(arr[::3])

print("*"*30)

# 3). Negative slicing
from array import array

arr=array('i', [10,20,30,40,50])

print(arr[-4:-1])
print(arr[-3:-1])
print(arr[:-2])

print("*"*30)

# 4). reverse array using slices
from array import array

arr=array('i', [10,20,30,40,50])

print(arr[::-1])

print("*"*30)

# 5). modify slices
from array import array

arr=array('i', [10,20,30,40,50])

arr[1:4]=array('i', [25,35,45])
print(arr)