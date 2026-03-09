# 1). len()-Number of elements
from array import array

arr=array('i', [10,20,30,40,50])
print(len(arr)) 

print("*"*30)

# 2). append(x)-add element at end 
from array import array

arr=array('i', [10,20,30])
arr.append(40)
print(arr)

print("*"*30)

# 3). insert(pos, x)-insert at position
from array import array

arr=array('i', [10,20,40])
arr.insert(2, 30)
print(arr)

print("*"*30)

# 4). remove(x)-remove first occurrence 
from array import array

arr=array('i', [10,20,30,20,40])
arr.remove(20)
print(arr)

print("*"*30)

# 5).pop()-remove and return element
from array import array 

arr=array('i', [10,20,30,40])
x=arr.pop()
print("removed :", x)
print(arr)

print("*"*30)

# 6). index(x)-find index of element
from array import array

arr=array('i', [10,20,30,40])
print(arr.index(30))

print("*"*30)

# 7). count(x)-count occurrences
from array import array

arr=array('i', [10,20,30,20,40])
print(arr.count(20))

print("*"*30)

# 8). reverse()-reverse array
from array import array

arr=array('i', [10,20,30,40])
arr.reverse()
print(arr)