import tkinter as tk
import random

# Dictionary for choices
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

def RPS(user):
    computer = random.randint(1, 3)

    user_label.config(text=f"User chose: {choices[user]}")
    computer_label.config(text=f"Computer chose: {choices[computer]}")

    if user == computer:
        result_label.config(text="Result: It's a Tie!")
    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):
        result_label.config(text="Result: You Win!")
    else:
        result_label.config(text="Result: Computer Wins!")


# ---- GUI Setup ----
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.resizable(False, False)

# Heading
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold")).pack(pady=10)

# Display Labels
user_label = tk.Label(root, text="User chose: ", font=("Arial", 12))
user_label.pack()

computer_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Buttons Frame
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(frame, text="Rock", width=10, command=lambda: RPS(1)).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper", width=10, command=lambda: RPS(2)).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissors", width=10, command=lambda: RPS(3)).grid(row=0, column=2, padx=5)

# Exit Button
tk.Button(root, text="Exit", width=10, command=root.destroy).pack(pady=10)

root.mainloop()
