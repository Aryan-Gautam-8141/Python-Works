n = int(input("Enter the Number : "))

product = 1
# print(f"The factorial of {n} is : ")
for i in range (1,n+1):
    product *= i
    # print(product)

print(f"The factorial of {n} is {product}")