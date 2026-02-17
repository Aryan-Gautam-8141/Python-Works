f = open("eg.txt")
data = f.read()
print(data)
f.close()

# Second Method
with open("eg.txt") as f:
   print(f.read())