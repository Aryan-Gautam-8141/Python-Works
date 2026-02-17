s = set()   #create an empty set

#Take 5 numbers as input from the user and add them to the set
#set does not allow duplicate values
for i in range (1,6):
    n = int(input(f"Enter a number {i} : ")) #take input from user in each iteration
    s.add(n)    #add number to set using add() method
   
print(s)