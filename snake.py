from tkinter import *
from tkinter import colorchooser
import random
import pickle
import os

gmwidth = 700
gmheight = 620
alive = True
spd = 150
spcsize = 50
snklen = 3
retries = 0
snkcolor = "#00FF00"
foodcolor = "#FF0000"
bgcolor = "#000000"


class Snake():
    
    def __init__(self):
        global snake

        self.bodylen = snklen
        self.coordinates = []
        self.squares = []

        for i in range(0, snklen):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = gamescreen.create_rectangle(x, y, x + spcsize, y + spcsize, fill=snkcolor, tag="snake")
            self.squares.append(square)

        

class Food():
    
    def __init__(self):
        global food
        global foods_eaten

        x = random.randint(0, (gmwidth/spcsize) -1 ) * spcsize
        y = random.randint(0, 550/spcsize - 1) * spcsize

        self.coordinates = [x, y]

        

        gamescreen.create_oval(x, y, x + spcsize, y + spcsize, fill=foodcolor, tag="food")

def play(snakex):
    global direction
    global retries
    global score
    global snake
    global food
    title.pack_forget()
    playb.pack_forget()
    setting.pack_forget()
    stats.pack_forget()

    direction = 'down'
    scoreindic.pack()
    gamescreen.pack()
    if retries > 0:
        retries += 1
        snakex.coordinates.clear()
        snake = Snake()
        food = Food()
        score = 0
        scoreindic.config(text=f"Score: {score}")
    next_turn(snake, food)

def bgclr():
    global bgcolor

    user_color = colorchooser.askcolor()
    colorhex = user_color[1]

    bgcolor = colorhex

    title.config(bg=colorhex)
    clrtitle.config(bg=colorhex)
    gamescreen.config(bg=colorhex)
    statslbl.config(bg=colorhex)
    highscrlbl.config(bg=colorhex)
    foodseatenlbl.config(bg=colorhex)
    windows.config(bg=colorhex)
def snkclr():
    global snkcolor

    user_color1 = colorchooser.askcolor()
    colorhex1 = user_color1[1]
    
    snkcolor = colorhex1
def foodclr():
    global foodcolor

    user_color2 = colorchooser.askcolor()
    colorhex2 = user_color2[1]

    foodcolor = colorhex2

def backbutton():

    clrtitle.pack_forget()
    newsnkclr.pack_forget()
    newbgclr.pack_forget()
    newfoodclr.pack_forget()
    backbtn.pack_forget()

    statslbl.pack_forget()
    highscrlbl.pack_forget()
    foodseatenlbl.pack_forget()

    

    title.pack(pady=20)
    playb.pack(pady=10)
    setting.pack(pady=10)
    stats.pack(pady=10)

def settings():

    title.pack_forget()
    playb.pack_forget()
    setting.pack_forget()
    stats.pack_forget()

    
    clrtitle.pack(pady=20)
    newbgclr.pack(pady=10)
    newsnkclr.pack(pady=10)
    newfoodclr.pack(pady=10)
    backbtn.pack(pady=20)

def statistics():
    global foods_eaten
    global highscore
    if os.path.exists('foodseaten.dat'):
        with open('foodseaten.dat', 'rb') as file:
            foods_eaten = pickle.load(file)
    if os.path.exists("hiscore.dat"):
        with open('hiscore.dat', 'rb') as file:
            highscore = pickle.load(file)
    title.pack_forget()
    playb.pack_forget()
    setting.pack_forget()
    stats.pack_forget()

    statslbl.pack(pady=50)
    highscrlbl.pack(pady=20)
    foodseatenlbl.pack(pady=20)
    backbtn.pack(pady=40)

    highscrlbl.config(text=f"Your current highscore is: {highscore}")
    foodseatenlbl.config(text=f"You ate a total of {foods_eaten} foods.")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'right':
        x += spcsize
    elif direction == 'left':
        x -= spcsize
    elif direction == 'up':
        y -= spcsize
    elif direction == 'down':
        y += spcsize

    snake.coordinates.insert(0, (x, y))
    square = gamescreen.create_rectangle(x, y, x + spcsize, y + spcsize, fill=snkcolor)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score
        global foods_eaten

        score += 1
        foods_eaten += 1
        scoreindic.config(text="Score: {}".format(score))
        gamescreen.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]
        gamescreen.delete(snake.squares[-1])
        del snake.squares[-1]

    for bodypart in snake.coordinates[1:]:
            if x == bodypart[0] and y == bodypart[1]:
                gamescreen.delete("food")
                food.coordinates.clear()
                food = Food()

    if check_collisions(snake):
        game_over()
    else:
        windows.after(spd, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= gmwidth:
        return True
    elif y < 0 or y >= 550:
        return True

    for bodypart in snake.coordinates[1:]:
        if x == bodypart[0] and y == bodypart[1]:
            return True

    return False

def game_over():
    global foods_eaten
    global retries
    global score
    global highscore

    if score > highscore:
        highscore = score
        with open('hiscore.dat', 'wb') as file:
            pickle.dump(highscore, file)

    with open("foodseaten.dat", "wb") as file:
        pickle.dump(foods_eaten, file)


    gamescreen.delete(ALL)
    gamescreen.create_text(gamescreen.winfo_width()/2, gamescreen.winfo_height()/2,
                           font=('consolas', 70), text="GAME OVER", fill="red", tag='gameover')
    retries += 1
    windows.after(1000, gameover2)

def gameover2():
    gamescreen.delete(ALL)
    gamescreen.pack_forget()
    scoreindic.pack_forget()

    retryb.pack(pady=30)
    tomainmenub.pack(pady=30)
    quitgmb.pack(pady=30)

def retry(snakex):
    global direction
    global retries
    global score
    global snake
    global food

    retryb.pack_forget()
    tomainmenub.pack_forget()
    quitgmb.pack_forget()

    retries += 1
    snakex.coordinates.clear()
    snake = Snake()
    food = Food()
    score = 0
    scoreindic.config(text=f"Score: {score}")

    direction = 'down'
    scoreindic.pack()
    gamescreen.pack()
    next_turn(snake, food)

def tomainmenu():
    retryb.pack_forget()
    tomainmenub.pack_forget()
    quitgmb.pack_forget()

    main_menu()

windows = Tk()
windows.title("Snek Gaem")
windows.geometry(f"{gmwidth}x{gmheight}")
windows.resizable(False, False)
windows.config(bg=bgcolor)

def main_menu():
    retryb.pack_forget()
    tomainmenub.pack_forget()
    quitgmb.pack_forget()

    title.pack(pady=20)
    playb.pack(pady=10)
    setting.pack(pady=10)
    stats.pack(pady=10)

highscore = 0
foods_eaten = 0
score = 0
direction = 'down'


windows.bind("<Up>", lambda event: change_direction('up'))
windows.bind("<Down>", lambda event: change_direction('down'))
windows.bind("<Left>", lambda event: change_direction('left'))
windows.bind("<Right>", lambda event: change_direction('right'))

windows.bind("<w>", lambda event: change_direction('up'))
windows.bind("<s>", lambda event: change_direction('down'))
windows.bind("<a>", lambda event: change_direction('left'))
windows.bind("<d>", lambda event: change_direction('right'))


# pre-made widgets
title = Label(windows, text="Snek Gaem", fg="green", font=("sawasdee", 70), bg=bgcolor)
playb = Button(windows, text="PLAY", fg="green", font=("sawasdee", 50),
                  command=lambda: play(snake))
setting = Button(windows, text="SETTINGS", fg="green", font=("sawasdee", 50),
                     command=lambda: settings())
stats = Button(windows, text="STATS", fg="green", font=("sawasdee", 50), 
                   command=lambda: statistics())
scoreindic = Label(windows, text="Score: {}".format(score) , font=("consolac", 40))
gamescreen = Canvas(windows, bg=bgcolor, width=gmwidth, height=gmheight)
clrtitle = Label(windows, text="Choose your color!", fg="green", font=("sawasdee", 55), bg=bgcolor)
newbgclr = Button(windows, text="Background color", fg="green", font=("sawasdee", 50),
                  command=lambda: bgclr())
newsnkclr = Button(windows, text="Snake color", fg="green", font=("sawasdee", 50),
                     command=lambda: snkclr())
newfoodclr = Button(windows, text="Food color", fg="green", font=("sawasdee", 50), 
                   command=lambda: foodclr())
backbtn = Button(windows, text="BACK", fg="green", font=("sawasdee", 25),
                     command=lambda: backbutton())
statslbl = Label(windows, text="Your current statistics:", font=("sawasdee", 50), bg=bgcolor, fg="green")
highscrlbl = Label(windows, text=f"Your current highscore is: {highscore}", font=("sawasdee", 30), bg=bgcolor, fg="green")
foodseatenlbl = Label(windows, text=f"You ate a total of {foods_eaten} foods.", font=("sawasdee", 30), bg=bgcolor, fg="green")
retryb = Button(windows, text="RETRY", font=("sawasdee", 50), fg="green", command=lambda: retry(snake))
tomainmenub = Button(windows, text="TO MAIN MENU", font=("sawasdee", 50), fg="green", command=lambda: tomainmenu())
quitgmb = Button(windows, text="QUIT", font=("sawasdee", 50), fg="green", command=lambda: windows.destroy())

windows.update()

ww = windows.winfo_width()
wh = windows.winfo_height()
sw = windows.winfo_screenwidth()
sh = windows.winfo_screenheight()

x = int((sw/2) - (ww/2))
y = int((sh/2) - (wh/2))
windows.geometry(f"{ww}x{wh}+{x}+{y}")

snake = Snake()
food = Food()
main_menu()


windows.mainloop()