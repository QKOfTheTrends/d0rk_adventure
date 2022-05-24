from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox

window = Tk()
window.geometry("200x300")
window.title("D0rk")

#### MODEL ####
# FRAMES - the diplays that the user sees. They contain all the widgets.
thinkfast = Frame(window, bg="white")

winner = Frame(window, bg="white")
three = Frame(window, bg="blue")
two = Frame(window, bg="orange")
one = Frame(window, bg="yellow")
map = Frame(window, bg="green")
intro = Frame(window, bg="black")

#thinkfastaft = Frame(window, bg)

# The variable frame will represent each element in the list. Each frame will be placed using the same x,y coordinates and dimensions
for frame in [intro, map, one, two, three,thinkfast, winner,]:
    frame.place(x=0, y=0, width=200, height=300)

# VARIABLES #
name = ""
frame = "map"

# IMAGES #
# JPG - Be sure to use the import statement on line 2
# img = Image.open("zork.jpg")
# zork = ImageTk.PhotoImage(img)

# PNGs
img = Image.open("zork.png")
zork = ImageTk.PhotoImage(img)

user = PhotoImage(file="user.png")

castle1_img = PhotoImage(file="castle1.png")
castle2_img = PhotoImage(file="castle2.png")
castle3_img = PhotoImage(file="castle3.png")
exitdoor1_img = PhotoImage(file="exitdoor.png")
exitdoor2_img = PhotoImage(file="exitdoor.png")
exitdoor3_img = PhotoImage(file="exitdoor.png")
goblin1_img = PhotoImage(file="goblinshadow1.png")
goblin2_img = PhotoImage(file="goblinface1.png")
goblin3_img = PhotoImage(file="goblin1.png")
winner_img = PhotoImage(file="winner1.png")
goblinthinking1_img = PhotoImage(file="goblinthinking1.png")

def countdown(count):
    print("count: " + str(count))
    if count > 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown, count-1)


# FUNCTIONS #
# INTRO FRAME #
def start(event):
    global name
    global frame
    global winner_label
    # Gets name from the entry box and stores the string in the name variable
    name = name_entry.get()
    print("Welcome " + name)
    winner_label.text = "YOU WIN " + name + "!"
    frame = "map"
    # Lifts the map frame to the top of the frame stack. The map frame is now visible.
    map.tkraise()


# MAP FRAME
# Checks to see if player is in the castle.
# If the the player is in the castle, it will raise the corresponding frame.
def is_in_a_castle():
    global frame
    castle_frames = [one, two, three]
    castles = [castle1, castle2, castle3]
    frames = ["one", "two", "three","thinkfast"]

    # Getting player's x and y coordinates
    playerX, playerY = canvas.coords(player)

    # Iterate across the list of castles
    for index in range(len(castles)):
        # Get the x and y coordinates for a castle
        castleX, castleY = canvas.coords(castles[index])
        # Calculating the boundaries of the castle
        castleLeft = castleX - 32
        castleRight = castleX + 32
        castleTop = castleY - 32
        castleBottom = castleY + 32
        # Determine if the player is located inside the boundaries of the castle
        if playerX > castleLeft and playerX < castleRight and playerY > castleTop and playerY < castleBottom:
            canvas.coords(player, 100, 123)
            # Assign frame the corresponding value as the frame
            if frames[index] == "three":
              if castle3_done == True:
                return()
              else:
                window.after(100, enter_castle3)
            elif frames[index] == "two":
              if castle2_done == True:
                return()
              else:
                window.after(100, enter_castle2)

            frame = frames[index]
            # Raise the frame that is associated with the castle that the player is in
            castle_frames[index].tkraise()



won_game = False

def is_winner():
  global won_game
  global name
  if castle1_done == True and castle2_done == True and castle3_done == True:
    won_game = True
    frame = "winner"
    winner_label.configure(text="YOU WIN " + name + "!")
    window.after(1000, winner.tkraise())
    print("You have won the game " + name)

def enter_castle3():
  global castle3_done
  global frame
  if castle3_done == True:
    frame = "map"
    map.tkraise()
  else:
    window.after(3000, castle3_complete)

def castle3_complete():
  global castle3_done
  global frame
  if player_alive == True:
    print("you did  it")
    castle3_done = True
    frame = "map"
    map.tkraise()
    window.after(1000, is_winner)


    
def enter_castle2():
  global castle2_done
  global frame
  if castle2_done == True:
    frame = "map"
    map.tkraise()

def castle2_complete():
  global castle2_done
  global frame
  print("Castle of False Exits complete")
  castle2_done = True
  frame = "map"
  map.tkraise()
  window.after(1000, is_winner)



one_done = False
two_done = False
three_done = False
castle1_done = False
castle2_done = False
castle3_done = False
thinkfast_done = False
player_alive = True

def move_player(event, deltaX, deltaY):
    global frame
    global castle1_done
    global castle2_done
    global castle3_done
    global player_alive

    if player_alive == False:
      print("The dead can't move")
      return()

    if frame == "map":
        playerX, playerY = canvas.coords(player)
        left = playerX - 10
        right = playerX + 10
        top = playerY - 10
        bottom = playerY + 10

        is_in_a_castle()
        # castleLeft, castleTop, castleRight, castleBottom=canvas.coords(castle)
        # Move player if it is in bounds
        if left > 0 and right < 190 and top > 0 and bottom < 250:
            # move(object, delta x, delta y), delta x is the amount that the object is moved left or right on the x axis. delta y is the amount that the object is moved up or down on the y axis
            canvas.move(player, deltaX, deltaY)
        else:
            canvas.config(bg="red")
            canvas.create_text(100, 100, text="You Die")
            question_restart(map)

    elif frame == "one":
        if castle1_done == False:
          stopmovinglist = [
            "No need to move around, just answer the questions",
            "No where to go",
            "What are you doing?",
            "Sigh..."
          ]
          stopmoving = random.choice(stopmovinglist)
          print(stopmoving)
        playerX, playerY = canvas1.coords(player1)
        left = playerX - 10
        right = playerX + 10
        top = playerY - 10
        bottom = playerY + 10
        #is_in_exitdoor()
        
        if left > 0 and right < 190 and top > 0 and bottom < 250:
            canvas1.move(player1, deltaX, deltaY)
        else:
            canvas1.config(bg="red")
            canvas1.create_text(100, 100, text="You Die")
            question_restart(one)
    elif frame == "two":
      player1X, player1Y = canvas2.coords(player1)

      playerX, playerY = canvas2.coords(player2)
      if playerX >= 95 and playerX <= 105 and playerY >= 115 and playerY <= 125:
        print("You chose wisely. You must be yourself to move forward.")
        castle2_complete()
      #print("coords: " + str(playerX) +  " " + str(playerY))

      left = playerX - 10
      right = playerX + 10
      top = playerY - 10
      bottom = playerY + 10
      if left > 0 and right < 190 and top > 0 and bottom < 250:
        canvas2.move(player2, deltaX, deltaY)
      else:
        canvas2.config(bg="red")
        canvas2.create_text(100, 100, text="You Die")
        question_restart(window)
    elif frame == "three":
      print("Your impatience has cost you your life")
      player_alive = False
      castle3_done = False
      player_is_dead()
      if castle3_done == True and player_alive == True:
        map.tkraise()
      else:
        canvas3.config(bg="red")
        canvas3.create_text(100, 100, text="You Die")
        #question_restart(three)
    elif frame == "thinkfast":
      # player2 is the goblin?
      # player4 is the unmoving player
      playerX, playerY = canvasthinkfast.coords(player2)
      #print("You moved to " + str(playerX) + ',' + str(playerY))

      if playerX >= 90 and playerX <= 120 and playerY >= 100 and playerY <= 130:
        print("Oh, you think fast and know goblins well!")
        thinkfast_complete()
      #print("coords: " + str(playerX) +  " " + str(playerY))

      left = playerX - 10
      right = playerX + 10
      top = playerY - 10
      bottom = playerY + 10
      if left > 0 and right < 190 and top > 0 and bottom < 250:
        canvasthinkfast.move(player2, deltaX, deltaY)
      else:
        canvasthinkfast.config(bg="red")
        canvasthinkfast.create_text(100, 100, text="You Die")
        question_restart(window)
    else:
        print("WHERE AM I?")



#### CONTROLLERS ####
# INTRO FRAME #
name_entry = Entry(intro)
name_entry.place(x=5, y=250, width=190, height=40)
name_entry.bind("<Return>", start)

#### VIEW ####
# INTRO FRAME #
intro_img = Label(intro, image=zork)
intro_img.place(x=0, y=0, width=200, height=200)

instructions = Label(intro,
                     text="Enter Your Name To Start Game",
                     bg="black",
                     fg="white",
                     wraplength=160)
instructions.place(x=5, y=205, width=190, height=40)



# MAP FRAME #
# label with instructions at the bottom of the map frame
map_instructions = Label(map,
                         text="Press Arrow Keys to Move Player",
                         bg="green",
                         fg="white",
                         wraplength=160)
map_instructions.place(x=5, y=255, width=190, height=40)




###################################
# MAP - canvas object on the map frame which the player navigates through
canvas = Canvas(map, bg="dark green")
canvas.place(x=5, y=5, width=190, height=250)
window.bind("<Left>", lambda event: move_player(event, -5, 0))
window.bind("<Right>", lambda event: move_player(event, 5, 0))
window.bind("<Up>", lambda event: move_player(event, 0, -5))
window.bind("<Down>", lambda event: move_player(event, 0, 5))
# window.bind("<Left>",lambda event: player_move(-5,0))
# window.bind("<Right>",lambda event: player_move(5,0))
# Create the player object on the canvas
player = canvas.create_image(100, 125, image=user)

# Add castle images to map
castle1 = canvas.create_image(50, 50, image=castle1_img)
castle2 = canvas.create_image(150, 190, image=castle2_img)
castle3 = canvas.create_image(50, 190, image=castle3_img)


###################################
# First castle - Castle of questions
canvas1 = Canvas(one, bg="orange")
canvas1.place(x=5, y=5, width=190, height=250)
player1 = canvas1.create_image(100, 125, image=user)
#exitdoor1 = canvas1.create_image(50, 50, image=exitdoor1_img)
goblin1 = canvas1.create_image(100,50, image=goblin1_img)

def restart_game():
  global window
  window.destroy()
  window = Tk()
  window.geometry("250x300")
  window.title("YOU'RE DEAD")
  img = PhotoImage(file='notalive_balloon.png')
  Label(window,image=img).pack()
  byebye = Label(window,
                text="The dead can't play games",
                bg="black",
                fg="white")
  byebye.place(x=0, y=255, width=300, height=40)
  print("☠☠☠☠☠☠☠☠ THIS IS THE END ☠☠☠☠☠☠☠☠")
  window.mainloop()
  
def question_restart(f):
  print("Do you want to restart?")                    
  question1 = Label(f,
                         text="☠☠☠☠☠☠☠☠",
                         bg="green",
                         fg="white",
                         wraplength=160, anchor=W)
  question1.place(x=5, y=255, width=190, height=60)
  qbutton1 = Button(question1, text= "Restart", command=restart_game)
  qbutton1.pack(side=RIGHT)


def answer_notalive():
  canvas1.config(bg="red")
  canvas1.create_text(100, 100, text="You Die")
  qbutton2.destroy()
  question1.configure(text="☠☠☠☠☠☠☠☠", anchor=NW)
  #qbutton2.pack_forget()
  qbutton1.configure(text="restart", command=restart_game)

#killerec1 = canvas1.create_rectangle(10,30,10,30)
#killerec2 = canvas1.create_rectangle(10,40,10,40)
canvasrec = Canvas(two, bg="pink") 

def rectangles():
  canvasthinkfast.create_rectangle(200,55,25,25,fill="blue")
  window.after(1500, create_rec2)

def create_rec2():
  canvasthinkfast.create_rectangle(15,250,60,75,fill="pink")
  window.after(1500, create_shape3)

def create_shape3():
  canvasthinkfast.create_oval(150,5,25,50,fill="red")
  window.after(1500, create_shape4)

def create_shape4():
  canvasthinkfast.create_oval(200,200,70,50,fill="black")
  window.after(1000, thinkfast_death)

def thinkfast_death():
  if frame == "thinkfast" and thinkfast_done == False:
    print("Oh no you think too slow and die")

    window.after(1000,player_is_dead())

  
def answer_leave():
  global frame
  global castle1_done
  global player1
  castle1_done = True
  question1.configure(text="Bye bye")
  qbutton2.destroy()
  if thinkfast_done == True:
    frame = "map"
    map.tkraise()
    window.after(300, map.tkraise())
  else:
    frame = "thinkfast"
    window.after(300, thinkfast.tkraise())
    thinkfast.config(bg="blue")
    question1.configure(text="MOVE TO THE MIDDLE NOW!!!!!", anchor=NW)
    window.after(1500, rectangles)
  window.after(1000, is_winner)


def answer_correct_color():
  global goblin_question
  canvas1.config(bg="green")
  canvas1.itemconfig(goblin1, image=goblin3_img)
  question1.configure(text=goblin_q3)
  qbutton1.configure(text="Leave", command=answer_leave)
  qbutton2.configure(text="Stay", command=answer_notalive)

def answer1_correct():
  global goblin_question
  canvas1.config(bg="brown")
  canvas1.itemconfig(goblin1, image=goblin2_img)
  question1.configure(text=goblin_q2)
  qbutton1.configure(text="Blue", command=answer_notalive)
  qbutton2.configure(text="Green", command=answer_correct_color)

goblin_question = StringVar()
goblin_q1 = "What is a goblins favorite item?"
goblin_q2 = "What is my favorite color?"
goblin_q3 = "Do you wish to stay or leave?"

question1 = Label(one,
                         text=goblin_q1,
                         bg="green",
                         fg="white",
                         wraplength=160)
question1.place(x=5, y=200, width=190, height=100)

qbutton1 = Button(question1, text= "Gold", command=answer1_correct,)
qbutton1.place(x=120,y=65)
qbutton2 = Button(question1, text= "Soup", command=answer_notalive)
qbutton2.place(x=10,y=65)



###################################
# Second castle  - Castle of false exits
# See move_player section for how to exit

canvas2 = Canvas(two, bg="pink")
canvas2.place(x=5, y=5, width=190, height=250)
playerexit = canvas2.create_image(100, 120, image=user)
player2 = canvas2.create_image(20, 25, image=user)
exitdoor2 = canvas2.create_image(150, 190, image=exitdoor2_img)
#exitdoor3 = canvas3.create_image(50, 190, image=exitdoor3_img)
exitdoor3 = canvas2.create_image(50, 190, image=exitdoor3_img)
exitdoor3 = canvas2.create_image(100, 35, image=exitdoor3_img)



###################################
# Castle 3 - don't move or die

def castle3_complete():
  global frame
  global castle3_done
  global player_alive
  if player_alive == False:
    player_is_dead()
  else:
    print("Through stillness we gain wisdom")
    print("Castle of Waiting complete")
    castle3_done = True
    frame = "map"
    map.tkraise()
    window.after(1000,is_winner)

canvas3 = Canvas(three, bg="grey")
canvas3.place(x=5, y=5, width=190, height=250)
player3 = canvas3.create_image(50, 15, image=user)
#exitdoor2 = canvas2.create_image(150, 190, image=exitdoor2_img)
#exitdoor3 = canvas3.create_image(50, 190, image=exitdoor3_img)
#exitdoor3 = canvas2.create_image(50, 190, image=exitdoor3_img)

nomove_label = Label(three,
                         text="DON'T MOVE!",
                         bg="green",
                         fg="white",
                         wraplength=100)
nomove_label.place(x=5, y=255, width=190, height=40)

def player_is_dead():
  global frame
  global player_alive
  global map_instructions
  player_alive == False
  frame = "map"
  map.tkraise()
  map_instructions.configure(text="YOU ARE DEAD")
  canvas.config(bg="red")
  canvas.create_text(100, 100, text="You Die")
  #qbutton2.destroy()
  #question1.configure(text="☠☠☠☠☠☠☠☠", anchor=NW)
  #qbutton2.pack_forget()
 # qbutton1.configure(text="restart", command=restart_game)


def poison_player(v):
    global player_alive
    l.config(text='Poisoned level ' + v)
    if int(float(v)) > 0:
      player_alive = False
      print("You have poisoned yourself")
    else:
      player_alive = True
      print("You are no longer poisoned")

    #window.after(2000, player_is_dead())

l = Label(three, bg='grey', fg='pink', width=20, text='empty')
l.pack()
s = Scale(three, label="Drink poison", from_=0, to=10, orient=HORIZONTAL, length=200, showvalue=1,tickinterval=2, resolution=0.01, bg="black", fg="pink", command=poison_player)
s.pack()


###################################
# Think fast canvas

def thinkfast_complete():
  global thinkfast_done
  global castle1_done
  global frame
  thinkfast_done = True
  castle1_done = True
  player_alive = True
  print("Castle of Questions complete")
  question1.configure(text='')
  frame = "map"
  map.tkraise()

canvasthinkfast = Canvas(thinkfast, bg="white")
canvasthinkfast.place(x=0,y=0, width=190, height=250)
thinkfast_goblin = canvasthinkfast.create_image(150,150,image=goblinthinking1_img)

thinkfast_instructions = Label(thinkfast,text="MOVE TO THE MIDDLE!",
                              bg="green",
                              fg="red",
                              wraplength=160)
thinkfast_instructions.place(x=5, y=270, width=190, height=40)
player4 = canvasthinkfast.create_image(100, 20, image=user)

###################################
# Winner canvas - You are the winner
canvaswinner = Canvas(winner, bg="white")
canvaswinner.place(x=0,y=0, width=190, height=250)
canvaswinner.pack(fill='both', expand = True)
winningsparkles = canvaswinner.create_image(0,0,image=winner_img)

#wintext = "YOU WIN " + name_entry + "!"
wintext = "YOU WIN!"
winner_label = Label(winner,
                         text=wintext ,
                         bg="green",
                         fg="white",
                         wraplength=160)
winner_label.place(x=5, y=255, width=190, height=40)



#############################
# Mainlooop

window.mainloop()



    
