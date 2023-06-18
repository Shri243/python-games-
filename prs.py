import tkinter as tk
import random

class RockPaperScissors(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
    # Create label to display computer choice
        self.computer_choice_label = tk.Label(self, text="Computer choice: ")
        self.computer_choice_label.grid(row=0, column=0, padx=10, pady=10)

        # Create label to display player choice
        self.player_choice_label = tk.Label(self, text="Player choice: ")
        self.player_choice_label.grid(row=1, column=0, padx=10, pady=10)

        # Create rock button
        rock_img = tk.PhotoImage(file="rock.png")
        self.rock_button = tk.Button(self, image=rock_img, width=200, height=200, command=lambda: self.play("rock"))
        self.rock_button.image = rock_img
        self.rock_button.grid(row=2, column=0, padx=10, pady=10)

        # Create paper button
        paper_img = tk.PhotoImage(file="paper.png")
        self.paper_button = tk.Button(self, image=paper_img, width=200, height=200, command=lambda: self.play("paper"))
        self.paper_button.image = paper_img
        self.paper_button.grid(row=3, column=0, padx=10, pady=10)

        # Create scissors button
        scissors_img = tk.PhotoImage(file="scissors.png")
        self.scissors_button = tk.Button(self, image=scissors_img, width=200, height=200, command=lambda: self.play("scissors"))
        self.scissors_button.image = scissors_img
        self.scissors_button.grid(row=4, column=0, padx=10, pady=10)

        # Create label to display result
        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=5, column=0, padx=10, pady=10)
    def play(self, player_choice):
        # Generate computer choice
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        # Update computer choice label
        self.computer_choice_label.config(text="Computer choice: " + computer_choice.title())

        # Update player choice label
        self.player_choice_label.config(text="Player choice: " + player_choice.title())

        # Determine winner
        if player_choice == computer_choice:
            result = "Tie"
            bg_color = "yellow"
        elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            bg_color = "green"
        else:
            result = "Computer wins!"
            bg_color = "red"

        # Update result label
        self.result_label.config(text=result, bg=bg_color)

root = tk.Tk()
app = RockPaperScissors(master=root)
app.mainloop()