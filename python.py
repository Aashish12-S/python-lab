Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hello world")
hello world
x=20
print(x)
20
x=20.5
print(x)
20.5
x=1j
print(x)
1j
x=["apple","banana","cherry"]
print(x)
['apple', 'banana', 'cherry']
x=("apple","banana","cherry")
print(x)
('apple', 'banana', 'cherry')
x={"orange","guavava","strawberry"}
print(x)
{'strawberry', 'orange', 'guavava'}
a=5 b=5
SyntaxError: invalid syntax
x=10,y=15
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=15
b=30
print(a+b)
45
print(a-b)
-15
print(a8b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(a8b)
NameError: name 'a8b' is not defined
print(a*b)
450
print(b/a)
2.0
print(a%b)
15

b = bytearray([65, 66, 67])
print(b)

SyntaxError: multiple statements found while compiling a single statement
b = bytearray([65, 66, 67])
print(b)

SyntaxError: multiple statements found while compiling a single statement


b = bytearray("cat", "utf-8")
print(b)

SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: invalid syntax


b = bytearray("cat", "utf-8")
print(b)

SyntaxError: multiple statements found while compiling a single statement

>>> b = bytearray("cat", "utf-8")
>>> print(b)
>>> b[0] = ord('b')
>>> print(b)

SyntaxError: invalid syntax
>>> b = bytearray("cat", "utf-8")
>>> print(b)
>>> b[0] = ord('b')
>>> print(b)