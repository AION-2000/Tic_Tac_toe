from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pyfiglet

def show_banner():
    banner = pyfiglet.figlet_format("AION")
    print(banner)

show_banner()




def restart_button_click():
    global player_1, player_2, game_over
    player_1 = 1
    player_2 = 0
    game_over = 0
    player_turn_label['text'] = "   Player 1's turn!   "
    for button in buttons:
        button['text'] = ' '
        button.state(['!disabled'])

root = Tk()
root.title("Tic Tac Toe")

show_banner()

# Add Buttons
buttons = []
for i in range(3):
    for j in range(3):
        button = ttk.Button(root, text=' ')
        button.grid(row=i, column=j, sticky='snew', ipadx=40, ipady=40)
        button.config(command=lambda button=button: ButtonClick(button))
        buttons.append(button)

player_turn_label = ttk.Label(root, text="   Player 1's turn!   ")
player_turn_label.grid(row=3, column=0, sticky='snew', ipadx=40, ipady=40)

player_details_label = ttk.Label(root, text="    Player 1: X\n\n    Player 2: O")
player_details_label.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40)

restart_button = ttk.Button(root, text='Restart')
restart_button.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)
restart_button.config(command=restart_button_click)

player_1 = 1
player_2 = 0
game_over = 0

def disable_buttons():
    for button in buttons:
        button.state(['disabled'])

def ButtonClick(button):
    global player_1, player_2, game_over
    if button['text'] == ' ' and game_over == 0:
        if player_1 == 1:
            button['text'] = "X"
            player_1 = 0
            player_2 += 1
            player_turn_label['text'] = "   Player 2's turn!   "
        else:
            button['text'] = "O"
            player_1 = 1
            player_2 += 1
            player_turn_label['text'] = "   Player 1's turn!   "
    
        # Check for winner
        if (buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text'] != ' ' or
            buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text'] != ' ' or
            buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text'] != ' ' or
            buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text'] != ' ' or
            buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text'] != ' ' or
            buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text'] != ' ' or
            buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] != ' ' or
            buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] != ' '):
                disable_buttons()
                game_over = 1
                winner = "Player 1" if player_1 == 0 else "Player 2"
                tkinter.messagebox.showinfo("Tic Tac Toe", f"Winner is {winner}!")
        elif player_2 == 9:
            disable_buttons()
            game_over = 1
            tkinter.messagebox.showinfo("Tic Tac Toe", "Match is a Draw.")

root.mainloop()
