f = open("eg.txt")

# data = f.readlines()    # Reads all lines into a list

line1 = f.readline()    # Reads first line
print(line1, type(line1))

line2 = f.readline()    # Reads second line
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))   # Will return empty string if no more lines are present

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

# print(data,type(data))
f.close()