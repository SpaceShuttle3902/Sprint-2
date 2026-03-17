import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from game_logic import PegSolitaireGame


def main():

    root = tk.Tk()
    root.title("Peg Solitaire Game")
    root.geometry("650x550")

    game = PegSolitaireGame()

    title = ttk.Label(root,text="Peg Solitaire",font=("Segoe UI",16))
    title.pack(pady=10)

    top_frame = ttk.Frame(root)
    top_frame.pack()

    board_var = tk.StringVar(value="English")

    board_type_frame = ttk.LabelFrame(top_frame,text="Board Type")
    board_type_frame.grid(row=0,column=0,padx=20)

    ttk.Radiobutton(board_type_frame,text="English",variable=board_var,value="English").pack(anchor="w")
    ttk.Radiobutton(board_type_frame,text="Hexagon",variable=board_var,value="Hexagon").pack(anchor="w")
    ttk.Radiobutton(board_type_frame,text="Diamond",variable=board_var,value="Diamond").pack(anchor="w")

    size_var = tk.IntVar(value=7)

    size_frame = ttk.Frame(top_frame)
    size_frame.grid(row=0,column=1)

    ttk.Label(size_frame,text="Board size").pack(side="left")

    ttk.Entry(size_frame,textvariable=size_var,width=5).pack(side="left")

    board_frame = ttk.Frame(root)
    board_frame.pack(pady=20)

    buttons = []
    selected = [None,None]


    def click_cell(r,c):

        if game.board[r][c] == 1 and selected[0] is None:

            selected[0] = r
            selected[1] = c
            buttons[r][c].config(bg="yellow")
            return

        if selected[0] is not None:

            r1,c1 = selected

            success = game.make_move(r1,c1,r,c)

            buttons[r1][c1].config(bg=root.cget("bg"))

            selected[0] = None
            selected[1] = None

            if success:
                draw_board()


    def draw_board():
        for r in range(game.size):
            for c in range(game.size):

                if buttons[r][c] is None:
                    continue

                if game.board[r][c] == 1:
                    buttons[r][c].config(text="●")
                else:
                    buttons[r][c].config(text="")

        if game.is_game_over():
            messagebox.showinfo("Game over","No more valid moves!")


    def build_board():

        for widget in board_frame.winfo_children():
            widget.destroy()

        buttons.clear()

        center = game.size // 2
        board_type = game.board_type

        for r in range(game.size):

            row = []

            for c in range(game.size):

                show_cell = True

                # ENGLISH BOARD (cross shape)
                if board_type == "English":
                    if (r < 2 or r > game.size-3) and (c < 2 or c > game.size-3):
                        show_cell = False

                # DIAMOND BOARD
                elif board_type == "Diamond":
                    if abs(r-center) + abs(c-center) > center:
                        show_cell = False

                # HEXAGON BOARD
                elif board_type == "Hexagon":
                    if abs(r-center) + abs(c-center) > center +1:
                        show_cell = False


                if not show_cell:
                    label = tk.Label(board_frame,text=" ",width=4)
                    label.grid(row=r,column=c)
                    row.append(None)

                else:
                    btn = tk.Button(board_frame,width=4,
                                    command=lambda r=r,c=c: click_cell(r,c))
                    btn.grid(row=r,column=c)

                    row.append(btn)

            buttons.append(row)


    def start_new_game():

        size = size_var.get()
        board_type = board_var.get()

        game.size = size
        game.board_type = board_type

        game.initialize_board()

        print("Board type selected:",board_type)
        print("Board size:",size)

        build_board()
        draw_board()


    ttk.Button(root,text="New Game",command=start_new_game).pack()

    build_board()
    draw_board()

    root.mainloop()


if __name__ == "__main__":
    main()