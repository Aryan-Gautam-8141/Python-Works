d = {} # empty dictionary

for i in range(1, 6):
    key = input(f"Enter key {i}: ")
    value = input(f"Enter value for key '{key}': ")
    d[key] = value # add key-value pair to dictionary   # it is preferable method

    # update method use to update value if the prior key is already present
    # for example: if key is 'a' and value is '1' and later if we again add key 'a' with value '2'
    # then the value of key 'a' will be updated to '2'
    d.update({key: value}) # another method to add key-value pair to dictionary

print(d)