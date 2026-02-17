def avg():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    # print("The average is:", (a+b)/2)  # Direct print statement but does not stored the value in variable
    return (a + b) / 2                   # Return the average instead of printing it directly 
                                         # which means the value wiil be stored in c 

c = avg()
print("The average is:", c)