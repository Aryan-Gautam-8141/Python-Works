n = int(input("Enter the Number : "))

for i in range (2,n):                           # loop from 2 to n-1
    if n%i==0:                                  # n number loop of i se divide ho raha hai
        print(f"{n} is not a prime number")     # suppose n 13 hai to 2 se 12 tak divide nahi hoga (n-1)
        break                                   # agr divide ho jata hai to ye prime nahi hai
    else:                                       # last me else wala print hoga jo prime hone ka condition hai
        print(f"{n} is a prime number.")
        break
    

# for i in range (2,n):
#     if n%i!=0:
#         print(f"{n} is a prime number.")
#         break