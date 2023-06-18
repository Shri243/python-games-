import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")
        self.board = [[0 for j in range(9)] for i in range(9)]
        self.create_widgets()

    def create_widgets(self):
    # Set the font and color scheme for the GUI
        font = ("Arial", 16)
        bg_color = "#ffffff"
        fg_color = "#000000"
        highlight_color = "#00c2ff"

        # Create a frame to hold the Sudoku board
        board_frame = tk.Frame(self.master, padx=20, pady=20, bg=bg_color)
        board_frame.pack()

        # Create 81 entry widgets to represent the cells of the Sudoku board
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(board_frame, width=3, font=font, bg=bg_color, fg=fg_color, highlightcolor=highlight_color, highlightthickness=2)
                entry.grid(row=i, column=j, padx=3, pady=3)
                row.append(entry)
            self.cells.append(row)

        # Create a button to check the current state of the board
        check_button = tk.Button(self.master, text="Check Solution", font=font, bg=highlight_color, fg=bg_color,
                                activebackground=highlight_color, activeforeground=bg_color,
                                command=self.check_board)
        check_button.pack(pady=10)

        # Create a button to clear the board
        clear_button = tk.Button(self.master, text="Clear Board", font=font, bg="#ff6b6b", fg=bg_color,
                                activebackground="#ff6b6b", activeforeground=bg_color,
                                command=self.clear_board)
        clear_button.pack(pady=10)

        # Add a label to explain how to use the GUI
        instructions_label = tk.Label(self.master, text="Enter numbers in the cells and click 'Check Solution' to see if you solved the puzzle!", font=("Arial", 14), bg=bg_color, fg=fg_color)
        instructions_label.pack(pady=20)

    def check_board(self):
        # Update the board with the values entered in the entry widgets
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].get():
                    self.board[i][j] = int(self.cells[i][j].get())
                else:
                    self.board[i][j] = 0

        # Check if the board is valid
        valid = self.is_valid_board()

        # Display a message indicating whether the board is valid or not
        if valid:
            message = "Valid board!"
            self.display_celebration()
        else:
            message = "Invalid board."
        message_box = tk.messagebox.showinfo("Result", message)

    def is_valid_board(self):
        # Check each row, column, and 3x3 sub-grid for validity
        for i in range(9):
            row = set()
            col = set()
            subgrid = set()
            for j in range(9):
                # Check the row
                if self.board[i][j] != 0:
                    if self.board[i][j] in row:
                        return False
                    row.add(self.board[i][j])
                # Check the column
                if self.board[j][i] != 0:
                    if self.board[j][i] in col:
                        return False
                    col.add(self.board[j][i])
                # Check the 3x3 sub-grid
                r = 3 * (i // 3) + j // 3
                c = 3 * (i % 3) + j % 3
                if self.board[r][c] != 0:
                    if self.board[r][c] in subgrid:
                        return False
                    subgrid.add(self.board[r][c])
        return True
    def clear_board(self):
        # Clear the entry widgets and reset the board
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.board[i][j] = 0
    def display_celebration(self):
    # Find all empty cells in the board
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    empty_cells.append((i, j))

    # Change the background color of each empty cell and display a celebration sticker
        for i, j in empty_cells:
            self.cells[i][j].config(bg="#f5d742")
            sticker = tk.PhotoImage(file="celebration.gif")
            self.cells[i][j].image = sticker
            self.cells[i][j].create_image(20, 20, image=sticker)
root = tk.Tk()
game = SudokuGUI(root)
root.mainloop()