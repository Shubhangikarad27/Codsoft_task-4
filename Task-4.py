# Task No:4 Rock, Paper, Scissors Game
#CodSoft

import tkinter as tk
import random

root = tk.Tk()
root.minsize(width=300,height=450)
root.title("Rock, Paper, Scissors Game")
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 20))
title_label.pack(pady=10)
global a
a=0
uw=0
cw=0
temp=0


def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        global uw
        uw=uw+1
        return "You win!"
    else:
        global cw
        cw=cw+1
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}\n{result}")
        
    label=tk.Label(text="Your Points: "+str(uw),fg="green",font=("Helvetica 10 bold"))
    label.place(x=105,y=230)
    label2=tk.Label(text="Computer Points: "+str(cw),fg="green",font=("Helvetica 10 bold"))
    label2.place(x=90,y=250)
    
    lb=tk.Label(text="Total Points: 5",fg="red",font=("Helvetica 10 bold"))
    lb.place(x=90,y=270)
    
    global a
    a=uw+cw
    
    if(a==5):
        global temp
        temp=10
        if(uw>cw):
            lb2.config(text="You are the winner of this Round")
        elif(cw==uw): 
            lb2.config(text="Score is equal of this Round   ")
        else:
            lb2.config(text="Computer is winner of this Round   ")
        
        
    if(temp==10):
        rock_button.config(state=tk.DISABLED)
        paper_button.config(state=tk.DISABLED)
        scissors_button.config(state=tk.DISABLED)

def on_rock():
    play_game("Rock")

def on_paper():
    play_game("Paper")

def on_scissors():
    play_game("Scissors")
    

def reset():
    # tk.lb2.disable()
    global t
    t=1
    global cw
    cw=0
    global uw
    uw=0
    lb2.config(text="   ")
    result_label.config(text=" ")
    
    # lb=tk.Label()
    label=tk.Label(text="Your Points: "+str(uw),fg="green",font=("Helvetica 10 bold"))
    label.place(x=105,y=230)
    label2=tk.Label(text="Computer Points: "+str(cw),fg="green",font=("Helvetica 10 bold"))
    label2.place(x=90,y=250)
    lb=tk.Label(text="Total Points: 5",fg="red",font=("Helvetica 11 bold"))
    lb.place(x=80,y=270)
    
    global temp
    temp=0
    rock_button.config(state=tk.ACTIVE)
    paper_button.config(state=tk.ACTIVE)
    scissors_button.config(state=tk.ACTIVE)
    
# Create labels and buttons

lb2=tk.Label(text=" ",fg="green",font=("Helvetica 12 bold"))
lb2.place(x=28,y=60)

rock_button = tk.Button(root, text="Rock", width=10, command=on_rock)
paper_button = tk.Button(root, text="Paper", width=10, command=on_paper)
scissors_button = tk.Button(root, text="Scissors", width=10, command=on_scissors)

rock_button.place(x=105,y=120)
paper_button.place(x=105,y=160)
scissors_button.place(x=105,y=200)


result_label =tk.Label(root, text="", font=("Helvetica", 16))
result_label.place(x=30,y=285)

def exit():
    root.destroy()


bt=tk.Button(root,text="Play Again",command=reset ,bg="yellow",fg="black",font=("Helvetica 12 bold"))
bt.place(x=90,y=340)

bt=tk.Button(root,text="Exit Game",command=exit ,bg="red",fg="white",font=("Helvetica 12 bold"))
bt.place(x=95,y=390)

root.mainloop()
