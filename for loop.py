
#1. print number from 1 to 6
for i in range(1,7):
    print(i)

# 2. print even from 1 t0 12
for i in range(1,13) :
    if i % 2 ==0 :
        print(i)
            
# 3. print odd 1 to 15
for i in range(1,16) :
    if i % 2 !=0 :
        print(i)
        
# 4. print table of 5
for i in range(1,11) :
    print("5x",i,"=",5*i)

# 5. char of a string
name="atmiya"
for letter in name :
    print(letter)

# 6. sum of num from 1 to 5
Total=0
for i in range (1,6) :
    Total = Total + i
    print("sum is",Total)

# 7. print list elements
numbers=[10,20,30,40,50]
for n in numbers :
    print(n)

# 8. print from 1 to 5
for i in range(1,6) :
    print(i)

# 9. print message 3 times
for i in range(3) :
    print("Hello")