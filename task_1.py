# 1).print number 1 to 5

print("\nPrint number 1 to 5")

i=1
while i<=5:
    print(i)
    i=i+1

print("*"*30)

# 2).sum of numbers take user input

print("\nSum of numbers")

n=int(input("Enter a number: "))
i=1
s=0
while i<=n:
    s=s+i
    i=i+1
print("Sum of natural numbers :",s)

print("*"*30)

# 3). print odd number between 1 to 20

print("\nPrint odd number between 1 to 20")

i=1
while i<=20:
    if i%2!=0:
        print(i)
    i=i+1

print("*"*30)

# 4).print table of for user input

print("\nPrint table of for user input")

n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1

print("*"*30)

# 5).print reverse number

print("\nPrint reverse number")

n=int(input("Enter a number: "))
i=n
while i>=1:
    print(i)
    i=i-1

print("*"*30)

# 6). print largest number in list

print("\nPrint largest number in list")

num=[10,20,5,15,25]
largest=max(num)
print("Largest number in list is:",largest)

print("*"*30)

# 7). print even number between 1 to 20

print("\nPrint even number between 1 to 20")

i=1
while i<=20:
    if i%2==0:
        print(i)
    i=i+1
