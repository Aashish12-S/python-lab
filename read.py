# read

f = open("Read/one.txt", "r")
data=f.read()
print("file content : ",data)
f.close()

# reading specific number of characters

f = open("Read/one.txt", "r")
data=f.read(5)
print("file content : ",data)
f.close()

# read lines

f = open("Read/one.txt", "r")
line1=f.readline()
line2=f.readline()
print("line 1 : ",line1)
print("line 2 : ",line2)
f.close()

# read all lines

f = open("Read/one.txt", "r")
data=f.readlines()
print("file content : ",data)
print("Number of lines : ",len(data))
f.close()

# read specific lines

f = open("Read/one.txt", "r")
lines=f.readlines()
print(lines[1].strip())
f.close()

