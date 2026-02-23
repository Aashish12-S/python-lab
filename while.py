# print 1 to 5 using while loop
i=1
while i<=5:
    print(i)
    i=i+1

print("*"*20)

# print 1 to 10 using while loop
i=1
while i<=10:
    print(i)
    i=i+1

print("*"*20)

# sum of natural numbers using while loop
n=int(input("Enter a number: "))
i=1
s=0
while i<=n:
    s=s+i
    i=i+1
print("Sum of natural numbers is:",s)

print("*"*20)

#table of number using while loop
n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1