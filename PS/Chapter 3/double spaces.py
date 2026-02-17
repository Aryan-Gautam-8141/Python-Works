str = "Hello, World! this is a  sample  string."

# Find the first occurrence of double spaces
print(str.find("  "))
# print(f"Double space found at index : {str.find("  ")}")

# AI generated solution
# Find all occurrences of double spaces
i = 0
while i < len(str):
    i = str.find("  ", i)
    if i == -1:
        break
    print(f"Double space found at index : {i}")
    i += 1

# special recommendation
# for loop method 
for i in range(len(str) -1):    # -1 because we are checking two characters if it does not included the last character it will give index error
    if str[i:i+2]=="  ":        # there is a use of slicing  in which i+1 is not included because it is exclusive means end index is not included
        print(f"Double space found at index of {i}")