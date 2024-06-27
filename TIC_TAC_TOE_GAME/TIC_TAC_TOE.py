import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.create_board()
        self.reset_game()

    def create_board(self):
        self.board_frame = tk.Frame(self, bg='mediumorchid4')
        self.board_frame.pack(expand=True)

        self.cells = []
        for i in range(9):
            cell = tk.Button(self.board_frame, text='', font=('Arial', 24), width=10, height=4,
                             command=lambda idx=i: self.player_move(idx), bg='plum2', fg='plum4')
            cell.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.cells.append(cell)

        self.restart_button = tk.Button(self, text="Restart Game", font=('Arial', 15), bg='antiquewhite1', width=56, height=2, command=self.reset_game)
        self.restart_button.pack()

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for cell in self.cells:
            cell.config(text="", state=tk.NORMAL)

    def player_move(self, idx):
        row, col = idx // 3, idx % 3
        if self.board[row][col] == " ":
            self.cells[idx].config(text="X", state=tk.DISABLED)
            self.board[row][col] = "X"
            if self.check_winner("X"):
                messagebox.showinfo("Tic Tac Toe", "Player X wins!")
                self.reset_game()
            elif all(all(cell != " " for cell in row) for row in self.board):
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.computer_move()

    def computer_move(self):
        i, j = self.get_best_move()
        idx = i * 3 + j
        self.cells[idx].config(text="O", state=tk.DISABLED)
        self.board[i][j] = "O"
        if self.check_winner("O"):
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            self.reset_game()

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def get_empty_cells(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]

    def minimax(self, depth, is_maximizing):
        if self.check_winner("X"):
            return -10 + depth
        elif self.check_winner("O"):
            return 10 - depth
        elif len(self.get_empty_cells()) == 0:
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i, j in self.get_empty_cells():
                self.board[i][j] = "O"
                score = self.minimax(depth + 1, False)
                self.board[i][j] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i, j in self.get_empty_cells():
                self.board[i][j] = "X"
                score = self.minimax(depth + 1, True)
                self.board[i][j] = " "
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        best_move = None
        best_score = -math.inf
        for i, j in self.get_empty_cells():
            self.board[i][j] = "O"
            score = self.minimax(0, False)
            self.board[i][j] = " "
            if score > best_score:
                best_score = score
                best_move = (i, j)
        return best_move

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()