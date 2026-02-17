list = ["apple", "banana", "cherry", 50, 10.59, True]

list.append("date") # adding an item to the end of the list :- last me date add hua
list[2] = "orange"  # changing an item in the list :- cherry ko orange se replace kia
list.reverse()      # reversing the list    :- list ka order ulta kar dia
                    # agar pehle reverse kiya hota fir replace kia to cherry ke badle 10.59 replace ho jata
                    # -> Beacuse python executes code line by line

# print(len(list))    # lists are mutable
# print(list)         # any further changes will be change the original list

l1=[1,52,98,35,55,62,12,14,36,55]
# l1.reverse()
# l1.sort()

print(l1.pop(2))    # removes and returns the item at the given index (2 here)
print(l1)