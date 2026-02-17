import tkinter as tk
import random

# Choices with icons
choices = {
    1: "🪨 Rock",
    2: "📄 Paper",
    3: "✂️ Scissors"
}

user_score = 0
computer_score = 0
rounds_played = 0
MAX_ROUNDS = 5


def play(user):
    global user_score, computer_score, rounds_played

    if rounds_played == MAX_ROUNDS:
        result_label.config(text="Match Over! Reset to play again.", fg="red")
        return

    computer = random.randint(1, 3)
    rounds_played += 1

    user_label.config(text=f"User chose: {choices[user]}")
    computer_label.config(text=f"Computer chose: {choices[computer]}")

    if user == computer:
        result_label.config(text="It's a Tie!", fg="blue")
    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):
        user_score += 1
        result_label.config(text="You Win this round!", fg="green")
    else:
        computer_score += 1
        result_label.config(text="Computer Wins this round!", fg="red")

    score_label.config(
        text=f"Score → You: {user_score} | Computer: {computer_score} | Round: {rounds_played}/5"
    )

    if rounds_played == MAX_ROUNDS:
        if user_score > computer_score:
            final_label.config(text="🏆 You Won the Match!", fg="green")
        elif computer_score > user_score:
            final_label.config(text="💻 Computer Won the Match!", fg="red")
        else:
            final_label.config(text="🤝 Match Draw!", fg="blue")


def reset_game():
    global user_score, computer_score, rounds_played
    user_score = 0
    computer_score = 0
    rounds_played = 0

    user_label.config(text="User chose:")
    computer_label.config(text="Computer chose:")
    result_label.config(text="Result:", fg="black")
    final_label.config(text="")
    score_label.config(text="Score → You: 0 | Computer: 0 | Round: 0/5")


# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x500")
root.configure(bg="#f0f8ff")
root.resizable(False, False)

# Heading
tk.Label(
    root,
    text="🎮 Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="#f0f8ff"
).pack(pady=10)

# Labels
user_label = tk.Label(root, text="User chose:", font=("Arial", 12), bg="#f0f8ff")
user_label.pack()

computer_label = tk.Label(root, text="Computer chose:", font=("Arial", 12), bg="#f0f8ff")
computer_label.pack()

result_label = tk.Label(root, text="Result:", font=("Arial", 14, "bold"), bg="#f0f8ff")
result_label.pack(pady=10)

score_label = tk.Label(
    root,
    text="Score → You: 0 | Computer: 0 | Round: 0/5",
    font=("Arial", 12),
    bg="#f0f8ff"
)
score_label.pack(pady=10)

final_label = tk.Label(root, font=("Arial", 16, "bold"), bg="#f0f8ff")
final_label.pack(pady=10)

# Buttons Frame
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=20)

tk.Button(
    frame, text="🪨 Rock", width=12, font=("Arial", 11),
    bg="#d1e7dd", command=lambda: play(1)
).grid(row=0, column=0, padx=5)

tk.Button(
    frame, text="📄 Paper", width=12, font=("Arial", 11),
    bg="#cff4fc", command=lambda: play(2)
).grid(row=0, column=1, padx=5)

tk.Button(
    frame, text="✂️ Scissors", width=12, font=("Arial", 11),
    bg="#f8d7da", command=lambda: play(3)
).grid(row=0, column=2, padx=5)

# Control Buttons
tk.Button(
    root, text="🔄 Reset", width=12,
    bg="#fff3cd", font=("Arial", 11),
    command=reset_game
).pack(pady=5)

tk.Button(
    root, text="❌ Exit", width=12,
    bg="#f5c2c7", font=("Arial", 11),
    command=root.destroy
).pack(pady=5)

root.mainloop()
