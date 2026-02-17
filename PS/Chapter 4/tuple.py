a = (1,8956,656,55)       # this is a tuple with one element
                # -> Note the comma which is necessary to define a single-element tuple

a = (1)         # this will print <class 'int'> -> Because parentheses alone do not create a tuple
a = ("a")       # this is a string
print(type(a))  # printing latest assignment

a[0] = 5        # this will give an error because tuples are immutable
                # -> means once defined, their elements cannot be changed, added, or removed
print(a)        # printing the tuple