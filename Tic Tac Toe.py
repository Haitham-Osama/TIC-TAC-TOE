from tkinter import *
import random
from PIL import Image,ImageTk
wX,wO=0,0

    
    
def next_turn(row,col):
    global player,wX,wO
    if buttons[row][col]['text']=="" and check_winner() is False:
        
        if player == players[0]:
            buttons[row][col]['text'] = player
            if check_winner() is False:
                player = players[1]
                turnLabel.config(text=(players[1])+" turn")
            elif check_winner() is True:
                turnLabel.config(text=(players[0]+ " Won!"))
                wX+=1
                xWinLabel.config(text=("X: "+ str(wX)))
            elif check_winner() is "tie":
                turnLabel.config(text=('Tie!'))

        elif player == players[1]:
            buttons[row][col]['text'] = player
            if check_winner() is False:
                player = players[0]
                turnLabel.config(text=(players[0])+" turn")
            elif check_winner() is True:
                turnLabel.config(text=(players[1]+ " Won!"))
                wO+=1
                oWinLabel.config(text=("O: "+ str(wO)))
            elif check_winner() is "tie":
                turnLabel.config(text=('Tie!'))
            
            
def check_winner():
    for row in range(3):
        if buttons[row][0]['text']== buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for col in range(3):
        if buttons[0][col]['text']== buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
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
    elif empty_spaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="yellow")
        return "Tie"
    else:return False
 
        
def empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != "":
                spaces-=1
    if spaces == 0:return False
    else:return True   


def new_game():
    global player
    player = random.choice(players)
    turnLabel.config(text=player + ' turn')
    for row in range(3):
            for col in range(3):
                buttons[row][col].config(text="",bg="#F0F0F0")


window = Tk()
window.geometry("400x600")
window.title("Tic Tac Toe")
window.minsize(400,600)
window.maxsize(400,600)
window.config(bg='white')
iconImage = Image.open("logo.png")
icon = ImageTk.PhotoImage(iconImage)
window.iconphoto(True, icon)

# launch in the middle
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x=int((screen_width/2) - (window_width/2))
y=int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

turnLabel = Label(text= player+ " turn",font =('Minecraft',40),pady=20,bg='white')
reset_button = Button(text="Restart",font =('Minecraft',40),command=new_game,bg='white',pady=20)
game_frame = Frame(window)

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(game_frame,text="",font =('Minecraft',45),width=3,height=1,
                                   command= lambda row=row,col = col:next_turn(row,col))
        buttons[row][col].grid(row=row,column=col)

xWinLabel = Label(text=("X: "+ str(wX)),font =('Minecraft',20),bg='white')
oWinLabel = Label(text=("O: "+ str(wO)),font =('Minecraft',20),bg='white')

turnLabel.pack()
reset_button.pack(side='bottom')
game_frame.pack()
xWinLabel.place(x=0,y=20)
oWinLabel.place(x=0,y=45)

window.mainloop()