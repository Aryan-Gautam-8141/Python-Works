import ast

a = input("Enter your text : ")
# b = float(a)
print(type(a))

# AI generated note: The code takes an input from the user and attempts to evaluate it as a Python literal using ast.literal_eval. If the evaluation fails due to a ValueError or SyntaxError, it retains the original string input. Finally, it prints the type of the evaluated result.
try:
    evaluated = ast.literal_eval(a)
except (ValueError, SyntaxError):
    evaluated = a

print(type(evaluated))