from tkinter import *
import random
from tkinter import messagebox
from math import cos, sin, pi
from PIL import Image, ImageTk


root = Tk()
root.title('game "15-puzzle"')

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2   #середина экрана
h = h // 2
w  = w - 200  #смещение от середины
h = h - 225
root.geometry('400x450+{}+{}'.format(w,h))
root.resizable(False, False)
root.configure(bg='#CCCCFF')

frame = Frame(root, bg='#CCCCFF', borderwidth=5, relief=GROOVE)
frame.pack(padx=20, pady=20)

size = 4
tile_size = 150
font_style =  ("Helvetica", 9, "bold")

numbers = list(range(1, size**2))
numbers.append(None)
random.shuffle(numbers)

empty_tile_pos = numbers.index(None)  #находим индекс нулевого элемента списка


def endd():
    global numbers
    numbers = list(range(1, size**2)) + [None]
    update_buttons()
    messagebox.showinfo("Game Over", "You have given up!")
    root.destroy()
    #show_image()


btn1 = Button(text='сдаюсь :(', background='#9999FF', width=15, height=1, command=endd)
btn1.pack(side=BOTTOM, pady=10, padx=10)


def move_tile(index):
    global empty_tile_pos                #делаем переменную глобальной, чтобы она изменилась не только внутри функции
    if (abs(empty_tile_pos - index) == 1 and empty_tile_pos // size == index // size) or abs(empty_tile_pos - index) == size:
        numbers[empty_tile_pos], numbers[index] = numbers[index], numbers[empty_tile_pos]     #меняем местами выбранную плитку с пустой
        empty_tile_pos = index
        update_buttons()

def update_buttons():
    for i, num in enumerate(numbers):
        if num is None:
            buttons[i].config(text='', state=DISABLED)
        else:
            buttons[i].config(text=str(num), state=NORMAL)

def check_win():
    if numbers == list(range(1, size**2)) + [None]:
        messagebox.showinfo("Congratulations!", "You have won the game!")

buttons = []
for i in range(size**2):
    btn = Button(frame, text=str(i+1), font=font_style, background='blueviolet', width=10, height=5, command=lambda i=i: move_tile(i))
    #btn.grid(row=i//size, column=i%size)
    buttons.append(btn)

#размещение кнопок в сетке
for i, btn in enumerate(buttons):
    row = i // size
    col = i % size
    btn.grid(row=row, column=col)


update_buttons()

root.mainloop()