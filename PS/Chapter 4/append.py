fruits=[]

for i in range(1,8):
    str=input(f"Enter fruit Name {i} : ")
    fruits.append(str)

print("Fruits List : ",fruits)

# printing each fruit on a new line
print("Fruits List : ",*fruits,sep="\n")    #The *fruits unpacks the list.
                                            #sep="\n" tells print() to separate each item by a newline.