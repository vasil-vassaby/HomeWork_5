from tkinter import *
import random


window = Tk()
window.title("Игра: крестики - нолики")
window.geometry(f'380x510')
window.resizable(False, False)

players = ["Х", "О"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]


label = Label(text=player + " ходит", font=('mono', 40))
label.pack(side="top")

frame = Frame(window)
frame.pack()


def next_turn(x, y):
    global player

    if buttons[x][y]['text'] == "" and not check_winner():

        if player == players[0]:

            buttons[x][y]['text'] = player

            if not check_winner():
                player = players[1]
                label.config(text=(players[1] + " ходит"))

            elif check_winner() == "Ничья":
                label.config(text="Ничья!")

            elif check_winner():
                label.config(text=(players[0] + " победил!"))

        else:

            buttons[x][y]['text'] = player

            if not check_winner():
                player = players[0]
                label.config(text=(players[0] + " ходит"))

            elif check_winner() == "Ничья":
                label.config(text="Ничья!")

            elif check_winner():
                label.config(text=(players[1] + " победил!"))


for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('mono', 50), width=3, height=1,
                                      command=lambda x=row, y=column: next_turn(x, y))
        buttons[row][column].grid(row=row, column=column)


def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            buttons[i][0].config(bg="green")
            buttons[i][1].config(bg="green")
            buttons[i][2].config(bg="green")
            return True

    for j in range(3):
        if buttons[0][j]['text'] == buttons[1][j]['text'] == buttons[2][j]['text'] != "":
            buttons[0][j].config(bg="green")
            buttons[1][j].config(bg="green")
            buttons[2][j].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif not empty_spaces():

        for i in range(3):
            for j in range(3):
                buttons[i][j].config(bg="yellow")
        return "Ничья"

    else:
        return False


def empty_spaces():
    spaces = 9

    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)

    label.config(text=player + " ходит")

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="#F0F0F0")


reset_button = Button(text="Рестарт", font=('mono', 20), command=new_game)
reset_button.pack(expand=YES, fill=BOTH, side="top")


window.mainloop()
