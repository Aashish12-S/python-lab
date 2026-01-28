

# 1. Calculate Simple Interest
p = input("Enter Principal: ")
r = input("Enter Rate: ")
t = input("Enter Time: ")
si = (p * r * t) / 100
print("Simple Interest =", si)

print("*" * 30)

# 2. Find maximum of 2 numbers
a = input("Enter first number: ")
b = input("Enter second number: ")
print("Maximum =", max(a, b))

print("*" * 30)

# 3. Print numbers 1 to 5
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

print("*" * 30)

# 4. Find length of a string
s = ("Enter a string: ")
print("Length of string =", len(s))

print("*" * 30)

# 5. Print a welcome message
print("Welcome to Python Programming!")

print("*" * 30)

# 6. Print first character of a string
s = input("Enter a string: ")
print("First character =", s[0])

print("*" * 30)

# 7. Print last character of a string
print("Last character =", s[-1])

print("*" * 30)

# 8. Check positive or negative number
num = input("Enter a number: ")
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

print("*" * 30)

# 9. Add three numbers
x = input("Enter first number: ")
y = input("Enter second number: ")
z = input("Enter third number: ")
print("Sum =", x + y + z)

print("*" * 30)

# 10. Take input from user and make a task (simple example)
task = input("Enter your task: ")
print("Your task is:", task)