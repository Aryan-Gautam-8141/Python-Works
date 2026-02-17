def rem(l, word):
    n=[]
    for item in l:
        if not(item==word):
           # n.append(item.strip(word))  # Strip only remove characters from the start and end
            n.append(item.replace(word, ""))  # Replace removes all occurrences
    return n

l=['apple', 'banana', 'orange', 'banana', 'grape']
print(rem(l, "a"))