from tkinter import *
from time import *

counter = Tk()
counter.title("Munchkin counter")
counter.attributes("-fullscreen", True)
counter.config(bg="#fee0a8")

players = []

p1_level = 1
p2_level = 1
p3_level = 1
p4_level = 1
p5_level = 1
p6_level = 1

print('Set the players:')
for i in range(6):
    name = input("Name -> ")
    players.append(name)


def plus_1():
    global p1_level
    p1_level += 1
    p1_level_label.configure(text=p1_level)


def minus_1():
    global p1_level
    p1_level -= 1
    p1_level_label.configure(text=p1_level)


def plus_2():
    global p2_level
    p2_level += 1
    p2_level_label.configure(text=p2_level)


def minus_2():
    global p2_level
    p2_level -= 1
    p2_level_label.configure(text=p2_level)


def plus_3():
    global p3_level
    p3_level += 1
    p3_level_label.configure(text=p3_level)


def minus_3():
    global p3_level
    p3_level -= 1
    p3_level_label.configure(text=p3_level)


def plus_4():
    global p4_level
    p4_level += 1
    p4_level_label.configure(text=p4_level)


def minus_4():
    global p4_level
    p4_level -= 1
    p4_level_label.configure(text=p4_level)


def plus_5():
    global p5_level
    p5_level += 1
    p5_level_label.configure(text=p5_level)


def minus_5():
    global p5_level
    p5_level -= 1
    p5_level_label.configure(text=p5_level)


def plus_6():
    global p6_level
    p6_level += 1
    p6_level_label.configure(text=p6_level)


def minus_6():
    global p6_level
    p6_level -= 1
    p6_level_label.configure(text=p6_level)


def update_clock():
    time_text = strftime("%H:%M:%S")
    time.configure(text=time_text)
    counter.after(1000, update_clock)


p1_label = Label(counter, text=players[0], font=("Roboto", 40), bg="#fee0a8")
p1_label.place(relx=1/7, y=120, anchor=CENTER)

p1_level_label = Label(counter, text=p1_level, font=("Roboto", 40, "bold"), bg="#fee0a8")
p1_level_label.place(relx=1/7, y=260, anchor=CENTER)

p1_plus = Button(counter, text=" + ", command=plus_1, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p1_plus.place(relx=1/7, y=450, anchor=CENTER)

p1_minus = Button(counter, text=" - ", command=minus_1, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p1_minus.place(relx=1/7, y=570, anchor=CENTER)


p2_label = Label(counter, text=players[1], font=("Roboto", 40), bg="#fee0a8")
p2_label.place(relx=2/7, y=120, anchor=CENTER)

p2_level_label = Label(counter, text=p2_level, font=("Roboto", 40, "bold"), bg="#fee0a8")
p2_level_label.place(relx=2/7, y=260, anchor=CENTER)

p2_plus = Button(counter, text=" + ", command=plus_2, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p2_plus.place(relx=2/7, y=450, anchor=CENTER)

p2_minus = Button(counter, text=" - ", command=minus_2, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p2_minus.place(relx=2/7, y=570, anchor=CENTER)


p3_label = Label(counter, text=players[2], font=("Roboto", 40), bg="#fee0a8")
p3_label.place(relx=3/7, y=120, anchor=CENTER)

p3_level_label = Label(counter, text=p3_level, font=("Roboto", 40, "bold"), bg="#fee0a8")
p3_level_label.place(relx=3/7, y=260, anchor=CENTER)

p3_plus = Button(counter, text=" + ", command=plus_3, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p3_plus.place(relx=3/7, y=450, anchor=CENTER)

p3_minus = Button(counter, text=" - ", command=minus_3, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p3_minus.place(relx=3/7, y=570, anchor=CENTER)


p4_label = Label(counter, text=players[3], font=("Roboto", 40), bg="#fee0a8")
p4_label.place(relx=4/7, y=120, anchor=CENTER)

p4_level_label = Label(counter, text=p4_level, font=("Roboto", 40, "bold"), bg="#fee0a8")
p4_level_label.place(relx=4/7, y=260, anchor=CENTER)

p4_plus = Button(counter, text=" + ", command=plus_4, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p4_plus.place(relx=4/7, y=450, anchor=CENTER)

p4_minus = Button(counter, text=" - ", command=minus_4, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p4_minus.place(relx=4/7, y=570, anchor=CENTER)


p5_label = Label(counter, text=players[4], font=("Roboto", 40), bg="#fee0a8")
p5_label.place(relx=5/7, y=120, anchor=CENTER)

p5_level_label = Label(counter, text=p5_level, font=("Roboto", 40, "bold"), bg="#fee0a8")
p5_level_label.place(relx=5/7, y=260, anchor=CENTER)

p5_plus = Button(counter, text=" + ", command=plus_5, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p5_plus.place(relx=5/7, y=450, anchor=CENTER)

p5_minus = Button(counter, text=" - ", command=minus_5, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p5_minus.place(relx=5/7, y=570, anchor=CENTER)


p6_label = Label(counter, text=players[5], font=("Roboto", 40), bg="#fee0a8")
p6_label.place(relx=6/7, y=120, anchor=CENTER)

p6_level_label = Label(counter, text=p6_level, font=("Roboto", 40, "bold"), bg="#fee0a8")
p6_level_label.place(relx=6/7, y=260, anchor=CENTER)

p6_plus = Button(counter, text=" + ", command=plus_6, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p6_plus.place(relx=6/7, y=450, anchor=CENTER)

p6_minus = Button(counter, text=" - ", command=minus_6, font=("Roboto", 40), bg="#fee0a8", activebackground="#fedb9a")
p6_minus.place(relx=6/7, y=570, anchor=CENTER)


start = time()
time_text = None
time = Label(counter, text=time_text, font=("Roboto", 60), bg="#fee0a8")
time.place(relx=0.5, y=750, anchor=CENTER)

update_clock()

counter.mainloop()