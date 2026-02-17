from datetime import date

n=input("Enter your name: ").capitalize()
# today's date
d=date.today()

letter = '''Dear <|Name|>,
You are selected! 
<|Date|>''' 

# by using replace function next to replace function is called chaining method
# it is necessary to convert date into string using str() function
print(letter.replace("<|Name|>",n).replace("<|Date|>",str(d)))