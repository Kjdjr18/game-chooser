from tkinter import *
from random import choice
import messagebox

game_list = []


def submit():
    if entry_box.get() != "":
        game_list.append(entry_box.get())
        game_label = Label(text=entry_box.get())
        game_label.pack()
        entry_box.delete(0, END)
    else:
        messagebox.showwarning(title="Warning", message="Please enter a game before pressing submit or Enter")


def choose():
    if len(game_list) > 1:
        chosen_game = choice(game_list)
        messagebox.showinfo(title="Your Winning Game", message=f"Congratulations, You are playing {chosen_game} today!")
    else:
        messagebox.showwarning(title="Warning", message="Please enter at least two games before you try and choose")


window = Tk()
window.title("Game Chooser")
window.minsize(width=500, height=500)
window.config(pady=20, padx=20)

input_label = Label(text="Input a game option here, then click submit or press Enter. Once you are done click 'CHOOSE'", pady=15)
input_label.pack()

entry_box = Entry(width=25)
entry_box.focus()
entry_box.pack()

submit_button = Button(text="Submit a game possibility", command=submit)
submit_button.pack()

list_label = Label(text="Here is the list of choices you have input", font=('', 18, "italic"), pady=15)
list_label.pack()

choose_button = Button(text="CHOOSE!", command=choose)
choose_button.pack(side="bottom")


window.bind('<Return>', lambda event: submit())


window.mainloop()