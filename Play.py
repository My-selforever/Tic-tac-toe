from tkinter import *
import tkinter.messagebox
import os

os.system('cls')

tk = Tk()
tk.title("Tic-Tac-Toe")

playerA = StringVar()
playerB = StringVar()

a = StringVar()
b = StringVar()


# p1n = player 1 name

p1n = Entry(tk, textvariable=a, bd=4)
p2n = Entry(tk, textvariable=b, bd=4)
p1n.grid(row=1, column=1, columnspan=8)
p2n.grid(row=2, column=1, columnspan=8)
Bclicked = True

flag = 0


def disableButton():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)


def clicked(btn):
    global Bclicked, flag, p1n, p2n, a, b, playerA, playerB
    if(btn["text"] == ' ' and Bclicked == True):
        btn["text"] = 'X'
        Bclicked = False
        refree()
        playerA = a.get() + " wins!"
        playerB = b.get() + " wins!"
        flag += 1

    elif(btn["text"] == ' ' and Bclicked == False):
        btn["text"] = 'O'
        Bclicked = True
        refree()
        flag += 1

    else:
        tkinter.messagebox.showinfo("Error", "Please select an empty slot")


def refree():
    if(b1["text"] == 'X' and b2["text"] == 'X' and b3["text"] == 'X' or
       b4["text"] == 'X' and b5["text"] == 'X' and b6["text"] == 'X' or
       b7["text"] == 'X' and b8["text"] == 'X' and b9["text"] == 'X' or
       b1["text"] == 'X' and b4["text"] == 'X' and b7["text"] == 'X' or
       b2["text"] == 'X' and b5["text"] == 'X' and b8["text"] == 'X' or
       b3["text"] == 'X' and b6["text"] == 'X' and b9["text"] == 'X' or
       b1["text"] == 'X' and b5["text"] == 'X' and b9["text"] == 'X' or
       b3["text"] == 'X' and b5["text"] == 'X' and b7["text"] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Won", playerA)
    elif(b1["text"] == 'O' and b2["text"] == 'O' and b3["text"] == 'O' or
         b4["text"] == 'O' and b5["text"] == 'O' and b6["text"] == 'O' or
         b7["text"] == 'O' and b8["text"] == 'O' and b9["text"] == 'O' or
         b1["text"] == 'O' and b4["text"] == 'O' and b7["text"] == 'O' or
         b2["text"] == 'O' and b5["text"] == 'O' and b8["text"] == 'O' or
         b3["text"] == 'O' and b6["text"] == 'O' and b9["text"] == 'O' or
         b1["text"] == 'O' and b5["text"] == 'O' and b9["text"] == 'O' or
         b3["text"] == 'O' and b5["text"] == 'O' and b7["text"] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Won", playerB)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tie", "The Match Has Ended In A Tie")


buttons = StringVar()
label = Label(tk, text="Player-1 ", font="courier-new",
              bg="black", fg="lime", height=1, width=8)
label.grid(row=1, column=0)

label = Label(tk, text="Player-2 ", font="courier-new",
              bg="black", fg="lime", height=1, width=8)
label.grid(row=2, column=0)


b1 = Button(tk, text=' ', font="courier-new",
            bg="black", fg="white", height=4, width=8, command=lambda: clicked(b1))
b1.grid(row=3, column=0)

b2 = Button(tk, text=' ', font="courier-new",
            bg="black", fg="white", height=4, width=8, command=lambda: clicked(b2))
b2.grid(row=3, column=1)

b3 = Button(tk, text=' ', font="courier-new",
            bg="black", fg="white", height=4, width=8, command=lambda: clicked(b3))
b3.grid(row=3, column=2)

b4 = Button(tk, text=' ', font="courier-new",
            bg="black", fg="white", height=4, width=8, command=lambda: clicked(b4))
b4.grid(row=4, column=0)

b5 = Button(tk, text=' ', font="courier-new",
            bg="black", fg="white", height=4, width=8, command=lambda: clicked(b5))
b5.grid(row=4, column=1)

b6 = Button(tk, text=' ', font="courier-new",
            bg="black", fg="white", height=4, width=8, command=lambda: clicked(b6))
b6.grid(row=4, column=2)

b7 = Button(tk, text=' ', font="courier-new",
            bg="black", fg="white", height=4, width=8, command=lambda: clicked(b7))
b7.grid(row=5, column=0)

b8 = Button(tk, text=' ', font="courier-new",
            bg="black", fg="white", height=4, width=8, command=lambda: clicked(b8))
b8.grid(row=5, column=1)

b9 = Button(tk, text=' ', font="courier-new",
            bg="black", fg="white", height=4, width=8, command=lambda: clicked(b9))
b9.grid(row=5, column=2)

tk.mainloop()
