import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Initialize board state
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'  # Shruti is 'X', computer is 'O'
        self.buttons = []

        # Create buttons for the board
        for i in range(9):
            button = tk.Button(self.root, text=' ', font='Arial 20', width=5, height=2, command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.status_label = tk.Label(self.root, text="Shruti's Turn", font='Arial 12 bold')
        self.status_label.grid(row=3, column=0, columnspan=3)

    def player_move(self, index):
        if self.board[index] == ' ' and self.current_player == 'X':
            self.board[index] = 'X'
            self.buttons[index].config(text='X', state='disabled')
            if self.check_winner('X'):
                self.highlight_winner('X')
                self.status_label.config(text="Shruti Wins!")
                self.show_winner("Shruti")
                self.disable_buttons()
            elif ' ' not in self.board:
                self.status_label.config(text="It's a tie!")
                self.show_winner("Tie")
            else:
                self.current_player = 'O'
                self.status_label.config(text="Computer's Turn")
                self.root.after(1000, self.computer_move)

    def computer_move(self):
        available_moves = [i for i in range(9) if self.board[i] == ' ']
        if available_moves:
            index = random.choice(available_moves)
            self.board[index] = 'O'
            self.buttons[index].config(text='O', state='disabled')
            if self.check_winner('O'):
                self.highlight_winner('O')
                self.status_label.config(text="Computer Wins!")
                self.show_winner("Computer")
                self.disable_buttons()
            elif ' ' not in self.board:
                self.status_label.config(text="It's a tie!")
                self.show_winner("Tie")
            else:
                self.current_player = 'X'
                self.status_label.config(text="Shruti's Turn")

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                self.winning_combo = combo  # Store the winning combo
                return True
        return False

    def highlight_winner(self, player):
        # Change the color of the winning buttons to green
        for index in self.winning_combo:
            self.buttons[index].config(bg='light green')

    def show_winner(self, winner):
        if winner == "Tie":
            messagebox.showinfo("Game Over", "It's a Tie!")
        else:
            messagebox.showinfo("Game Over", f"{winner} Wins!")

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
