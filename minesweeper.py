import tkinter as tk
import random
from tkinter import messagebox

class Minesweeper:
    def __init__(self, master, num_rows=10, num_cols=10, num_mines=10):
        self.master = master
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_mines = num_mines
        self.minefield = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold the minefield
        minefield_frame = tk.Frame(self.master, padx=10, pady=10, bg="#212121")
        minefield_frame.pack()

        # Create buttons to represent the cells of the minefield
        self.buttons = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                button = tk.Button(minefield_frame, width=2, height=1, font=("Arial", 16, "bold"), bg="#424242", fg="#ffffff",
                                activebackground="#757575", activeforeground="#ffffff",
                                command=lambda i=i, j=j: self.click_cell(i, j))
                button.grid(row=i, column=j, padx=2, pady=2)
                row.append(button)
            self.buttons.append(row)

        # Place mines randomly on the minefield
        self.place_mines()

    def place_mines(self):
        # Generate a list of all possible cell coordinates
        all_coords = [(i, j) for i in range(self.num_rows) for j in range(self.num_cols)]

        # Randomly select cells to place mines in
        mine_coords = random.sample(all_coords, self.num_mines)

        # Place mines on the minefield
        for coord in mine_coords:
            self.minefield[coord[0]][coord[1]] = -1

    def click_cell(self, i, j):
    # Check if the cell contains a mine
        if self.minefield[i][j] == -1:
            self.buttons[i][j].config(text="*", bg="#ff0000")
            self.display_game_over()
        else:
            # Count the number of adjacent mines
            num_adjacent_mines = 0
            for r in range(i-1, i+2):
                for c in range(j-1, j+2):
                    if (r >= 0 and r < self.num_rows and c >= 0 and c < self.num_cols and
                        self.minefield[r][c] == -1):
                        num_adjacent_mines += 1

            # Update the button with the number of adjacent mines
            button = self.buttons[i][j]
            if num_adjacent_mines == 0:
                button.config(text="0", bg="#4444ff", state="disabled")
            elif num_adjacent_mines == 1:
                button.config(text=num_adjacent_mines, bg="#3333ff", state="disabled")
            elif num_adjacent_mines == 2:
                button.config(text=num_adjacent_mines, bg="#33ff33", state="disabled")
            elif num_adjacent_mines == 3:
                button.config(text=num_adjacent_mines, bg="#ff3333", state="disabled")
            elif num_adjacent_mines == 4:
                button.config(text=num_adjacent_mines, bg="#993399", state="disabled")
            else:
                button.config(text=num_adjacent_mines, bg="#ff9933", state="disabled")

            # Check if the game has been won
            if self.check_win():
                self.display_game_win()

    def check_win(self):
        # Check if all non-mine cells have been revealed
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.minefield[i][j] != -1 and self.buttons[i][j]["state"] != "disabled":
                    return False
        return True

    def display_game_over(self):
        # Disable all buttons
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.buttons[i][j].config(state="disabled")

        # Display a message indicating that the game is over
        messagebox.showinfo("Game Over", "You clicked a mine!")
    def display_game_over(self):
        # Disable all buttons
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.buttons[i][j].config(state="disabled")

        # Create a new window to display the game over message
        game_over_window = tk.Toplevel(self.master)
        game_over_window.title("Game Over")
        game_over_window.config(bg="#282828")

        # Create a label to display the game over message
        message_label = tk.Label(game_over_window, text="Game Over: You clicked a mine!", font=("Arial", 20), fg="#ff0000", bg="#282828")
        message_label.pack(padx=20, pady=20)

        # Create a button to close the window
        close_button = tk.Button(game_over_window, text="Close", font=("Arial", 16), bg="#555555", fg="#ffffff", command=game_over_window.destroy)
        close_button.pack(pady=20)
def main():
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, num_rows=10, num_cols=10, num_mines=10)
    root.mainloop()

if __name__ == "__main__":
    main()