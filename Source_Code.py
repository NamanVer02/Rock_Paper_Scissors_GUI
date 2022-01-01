import tkinter as tk
import random
import requests
from tkinter import messagebox
from PIL import ImageTk, Image

user = ''
choices = ['stone', 'paper', 'scissors']

window = tk.Tk()
label = tk.Label(text='Choose anyone and click play', background='black', foreground='white', width=500, height=5)
label.place(x=0, y=0, width=500)

label2 = tk.Label(background='black', width=500, height=495)
label2.place(x=0, y=80, width=500)
try:
    stone_img = ImageTk.PhotoImage(Image.open(requests.get('https://i.ibb.co/kXwB3Xb/stone.jpg', stream=True).raw))
    paper_img = ImageTk.PhotoImage(Image.open(requests.get('https://i.ibb.co/7tsM2qC/paper.jpg', stream=True).raw))
    scissors_img = ImageTk.PhotoImage(Image.open(requests.get('https://i.ibb.co/Vm9CMhr/scissors.jpg', stream=True).raw))
except:
    messagebox.showinfo('Connection Error', 'Please connect to the internet to play this game')
    window.destroy()

def stone():
    global user
    user = 'stone'
    canvas_user.create_image(67, 67, anchor='center', image=stone_img)

def paper():
    global user
    user = 'paper'
    canvas_user.create_image(67, 67, anchor='center', image=paper_img)

def scissors():
    global user
    user = 'scissors'
    canvas_user.create_image(67, 67, anchor='center', image=scissors_img)

def play():
    bot = random.choice(choices)

    if user == '':
        messagebox.showinfo('Error', 'Please chose an option before clicking play \nWe give the bot one point for your stupidity')

    def checkdraw():
        if user == bot:
            return True
        else:
            return False

    def checkwin():
        if user == 'stone' and bot == 'scissors':
            return True
        elif user == 'paper' and bot == 'stone':
            return True
        elif user == 'scissors' and bot == 'paper':
            return True
        else:
            return False

    if bot == 'stone':
        canvas_bot.create_image(67, 67, anchor='center', image=stone_img)
    elif bot == 'paper':
        canvas_bot.create_image(67, 67, anchor='center', image=paper_img)
    else:
        canvas_bot.create_image(67, 67, anchor='center', image=scissors_img)

    if not checkdraw():
        if checkwin():
            score_box1['text'] += 1
        else:
            score_box2['text'] += 1

    winner = tk.Label(text=f'Winner this round : {"Tied" if checkdraw() else("User" if checkwin() else "Bot ")}')
    winner.place(x=170, y=250)


def score():
    messagebox.showinfo('Score', f"User = {score_box1['text']} \nBot = {score_box2['text']}")

button1 = tk.Button(text='Stone', command=stone)
button2 = tk.Button(text='Paper', command=paper)
button3 = tk.Button(text='Scissors', command=scissors)
button4 = tk.Button(text='Play', command=play)
button5 = tk.Button(text='Check Score', command=score)

button1.place(x=95, y=100, width=50)
button2.place(x=215, y=100, width=50)
button3.place(x=335, y=100, width=50)
button4.place(x=145, y=150, width=190, height=40)
button5.place(x=145, y=200, width=190, height=40)



canvas_user = tk.Canvas(bg='black', width=130, height=130)
canvas_user.place(x=75, y=280)

canvas_bot = tk.Canvas(bg='black', width=130, height=130)
canvas_bot.place(x=270, y=280)

label3 = tk.Label(text='User', bg='black', fg='white')
label3.place(x=130, y=430)
label4 = tk.Label(text='Bot', bg='black', fg='white')
label4.place(x=330, y=430)

score_box1 = tk.Label(text=0, justify='center')
score_box1.place(x=125, y=460, width=40)
score_box2 = tk.Label(text=0, justify='center')
score_box2.place(x=322, y=460, width=40)

window.title('Stone Paper Scissors')
window.geometry('500x500')

window.mainloop()


