def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    # return result

n = int(input("Enter the Number : "))
print(f"The factorial of {n} is {factorial(n)}")