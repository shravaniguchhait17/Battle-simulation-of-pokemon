import random
from tkinter import *
import time

import pygame
from pygame import mixer

window=Tk()
my_canvas=Canvas(window,width=1500,height=800)
my_canvas.pack(fill="both",expand=True)


#define background image
bg=PhotoImage(file='background1.png')
my_canvas.create_image(0,0, image=bg,anchor=NW)


#initializing the pygame.mixer module
pygame.mixer.init()

#background sound
mixer.music.load('pokemon-opening-sound.mp3')
mixer.music.play(-1)

#entry sound
entry_sound=mixer.Sound('pokemon_sound3.mp3')

#weapon sounds
weapons_sound=mixer.Sound('weapons.mp3')
pound_sound=mixer.Sound('Pound_sound.mp3')
scratch_sound=mixer.Sound('Scratch_sound.mp3')
tackle_sound=mixer.Sound('Tackle_sound.mp3')
heal_sound=mixer.Sound('Heal-sound(1).mp3')

#finishing sounds
victory_sound=mixer.Sound('Victory.mp3')
lose_sound=mixer.Sound('Lose.mp3')



moves = {"Pound": range(11,26),
         "Razor leaf": range(23,26), 
         "Scratch": range(13,26),
         "Ember": range(16,26),
         "Tackle": range(18,26),
         "Watergun": range(13,26),
         "Heal": range(10,20) }

#declaring 2 integer variables for storing the value of radio buttons
global var_atk

var_pok=IntVar()
var_atk=IntVar()



def battle1():
    pok1=var_pok.get()
    disable_move_radio()
    attack=var_atk.get()

    if attack==1:
        choice='Scratch'
    elif attack==2:
        choice='Ember'
    elif attack==3:
        choice='Pound'
    elif attack==4:
        choice='Razor leaf'
    elif attack==5:
        choice='Tackle'
    elif attack==6:
        choice='Watergun'
    elif attack==7:
        choice='Heal' 
        
    if enemy.health > 0 and player.health > 0:
        player.attack(enemy,choice)
        label_health_enemy=Label(window,text="Health Enemy =  "+str(enemy.health),font="Comic 16 bold", bg="pink")
        label_health_enemy.config(width=16)
        my_canvas.create_window(140,600,window=label_health_enemy)

        #delaying enemy's attack for 5 secs
        window.after(5000,battle2)                                                                                      
        outcome()
        
 
########################################################################
def battle2():
    
    pok1=var_pok.get()
    disable_move_radio()
    attack=var_atk.get()
    
    if attack==1:
        choice='Scratch'
    elif attack==2:
        choice='Ember'
    elif attack==3:
        choice='Pound'
    elif attack==4:
        choice='Razor leaf'
    elif attack==5:
        choice='Tackle'
    elif attack==6:
        choice='Watergun'
    elif attack==7:
        choice='Heal'   

    if enemy.health>0:
        enemy.attack(player,choice) 
        label_health_player=Label(window,text="Health Player =  "+str(player.health),font="Comic 16 bold", bg="pink")
        label_health_player.config(width=16)
        my_canvas.create_window(1400,600,window=label_health_player)
    
        enable_move_radio()
        select_move()   
        outcome()


def outcome():
     if player.health <= 0:
        label_outcome=Label(window,text="You were defeated by Gary! GAME OVER!!!",font="Comic 32 bold", bg="pink")
        my_canvas.create_window(750,700,window=label_outcome)
        lose_sound.play()
        disable_move_radio()
     if enemy.health <= 0:
        label_outcome=Label(window,text="You defeated Gary! GAME OVER!!!",font="Comic 32 bold", bg="pink")
        my_canvas.create_window(750,700,window=label_outcome)
        victory_sound.play()
        disable_move_radio()




class Pokemon:
    """ Define our general Character which we base our player and enemy off """
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class Player(Pokemon):
    """ The player, they start with 100 health and have the choice of three moves """
    def __init__(self, health=100):
       global label_health_player
       label_health_player=Label(window,text="Health Player = "+str(health),font="Comic 16 bold", bg="pink")
       label_health_player.config(width=16)
       my_canvas.create_window(1400,600,window=label_health_player)
       super().__init__(health)

    def attack(self, other, choice):
        global photo_image_ember_right, my_image_ember_right, photo_image_watergun_right
        global my_image_watergun_right, photo_image_razor_right, my_image_razor_right
        
        if choice == "Heal":
            heal_sound.play()
            hp = int(random.choice(moves[choice]))
            self.health += hp
            label_attack_player=Label(window,text="You chose heal gaining " + str(hp) + " HP.",font="Comic 12", bg="white")
            label_attack_player.config(width=50)
            my_canvas.create_window(1300,750,window=label_attack_player)
            label_health_player=Label(window,text="Health Player = "+str(self.health),font="Comic 16 bold", bg="pink")
            label_health_player.config(width=16)
            my_canvas.create_window(1400,600,window=label_health_player)
            
        if choice == "Scratch" or choice == "Ember":
            if choice == "Scratch":
                scratch_sound.play()
            if choice == "Ember":
                weapons_sound.play()
                my_image_ember_right = my_canvas.create_image(350,750,image=photo_image_ember_right,anchor=SW)
                move_ember_right()
            damage = int(random.choice(moves[choice]))
            other.health -= damage
            label_attack_player=Label(window,text="Charmander attacks with " + choice + " dealing " + str(damage) + " damage.",font="Comic 12", bg="white")
            label_attack_player.config(width=50)
            my_canvas.create_window(1300,750,window=label_attack_player)
            
        if choice == "Tackle" or choice == "Watergun":
            if choice == "Tackle":
                tackle_sound.play()
            if choice == "Watergun":
                weapons_sound.play()
                my_image_watergun_right = my_canvas.create_image(350,750,image=photo_image_watergun_right,anchor=SW)
                move_watergun_right()
            damage = int(random.choice(moves[choice]))
            other.health -= damage
            label_attack_player=Label(window,text="Squirtle attacks with " + choice + " dealing " + str(damage) + " damage.",font="Comic 12", bg="white")
            label_attack_player.config(width=50)
            my_canvas.create_window(1300,750,window=label_attack_player)
            
        if choice == "Pound" or choice == "Razor leaf":
            if choice == "Pound":
                pound_sound.play()
            if choice == "Razor leaf":
                weapons_sound.play()
                my_image_razor_right = my_canvas.create_image(350,650,image=photo_image_razor_right,anchor=SW)
                move_razor_right()
            damage = int(random.choice(moves[choice]))
            other.health -= damage
            label_attack_player=Label(window,text="Bulbasaur attacks with " + choice + " dealing " + str(damage) + " damage.",font="Comic 12", bg="white")
            label_attack_player.config(width=50)
            my_canvas.create_window(1300,750,window=label_attack_player)
        
            
       
class Enemy(Pokemon):
    """ The enemy, also starts with 100 health and chooses moves at random """
    def __init__(self, health=100):
        if health > 0:
            label_health_enemy=Label(window,text="Health Enemy = "+str(health),font="Comic 16 bold", bg="pink")
            label_health_enemy.config(width=16)
            my_canvas.create_window(140,600,window=label_health_enemy)
        else:
            label_faint=Label(window,text="The pokemon fainted",font="Comic 16 bold", bg="pink")
            label_faint.config(width=16)
            my_canvas.create_window(140,600,window=label_faint)
            
        super().__init__(health)
   
    def attack(self, other,choice):
        global photo_image_watergun_left, my_image_watergun_left, photo_image_ember_left, my_image_ember_left, photo_image_razor_left, my_image_razor_left 
        
        pok1=var_pok.get()
        enable_move_radio()
        
        if pok1==1:
           pokemon2="squirtle"
        elif pok1==2:
           pokemon2="charmander"
        elif pok1==3:
           pokemon2="bulbasaur"
   
        if pokemon2 == 'charmander':
            if self.health <= 35:
                # increasing probability of heal when under 35 health
                moves_1 = ["Scratch", "Ember", "Heal", "Heal"]
                cpu_choice = random.choice(moves_1)
            else:
                moves_2= ["Scratch", "Ember"]
                cpu_choice = random.choice(moves_2)
            if cpu_choice == "Scratch" or cpu_choice == "Ember":
                if cpu_choice == "Scratch":
                    scratch_sound.play()
                if cpu_choice == "Ember":
                    weapons_sound.play()
                    my_image_ember_left = my_canvas.create_image(350,750,image=photo_image_ember_left,anchor=SW)
                    move_ember_left()
                damage = int(random.choice(moves[cpu_choice]))
                other.health -= damage
                label_attack_enemy=Label(window,text="Charmander attacks with " + cpu_choice + " dealing " + str(damage) + " damage.",font="Comic 12", bg="white")
                label_attack_enemy.config(width=50)
                my_canvas.create_window(240,750,window=label_attack_enemy)
            if cpu_choice == "Heal":
                heal_sound.play()
                hp = int(random.choice(moves[cpu_choice]))
                self.health += hp
                label_attack_enemy=Label(window,text="Charmander uses heal and it gains " + str(hp) + "HP.",font="Comic 12", bg="white")
                label_attack_enemy.config(width=50)
                my_canvas.create_window(240,750,window=label_attack_enemy)
                label_health_enemy=Label(window,text="Health Enemy = "+str(self.health),font="Comic 16 bold", bg="pink")
                label_health_enemy.config(width=16)
                my_canvas.create_window(140,600,window=label_health_enemy)

    
        if pokemon2 == 'squirtle':
            if self.health <= 35:
                # increasing probability of heal when under 35 health
                moves_1 = ["Tackle", "Watergun", "Heal", "Heal"]
                cpu_choice = random.choice(moves_1)
            else:
                moves_2= ["Tackle", "Watergun"]
                cpu_choice = random.choice(moves_2)
            if cpu_choice == "Tackle" or cpu_choice == "Watergun":
                if cpu_choice == "Tackle":
                    tackle_sound.play()
                if cpu_choice=="Watergun":
                    weapons_sound.play()
                    my_image_watergun_left = my_canvas.create_image(350,750,image=photo_image_watergun_left,anchor=SW)
                    move_watergun_left()
                
                damage = int(random.choice(moves[cpu_choice]))
                other.health -= damage
                label_attack_enemy=Label(window,text="Squirtle attacks with " + cpu_choice + " dealing " + str(damage) + " damage.",font="Comic 12", bg="white")
                label_attack_enemy.config(width=50)
                my_canvas.create_window(240,750,window=label_attack_enemy)
            if cpu_choice == "Heal":
                heal_sound.play()
                hp = int(random.choice(moves[choice]))
                self.health += hp
                label_attack_enemy=Label(window,text="Squirtle uses heal and its health is now " + str(self.health),font="Comic 12", bg="white")
                label_attack_enemy.config(width=50)
                my_canvas.create_window(240,750,window=label_attack_enemy)
                label_health_enemy=Label(window,text="Health Enemy = "+str(self.health),font="Comic 16 bold", bg="pink")
                label_health_enemy.config(width=16)
                my_canvas.create_window(140,600,window=label_health_enemy)

        if pokemon2 == 'bulbasaur':
            if self.health <= 35:
                # increasing probability of heal when under 35 health
                moves_1 = ["Pound", "Razor leaf", "Heal", "Heal"]
                cpu_choice = random.choice(moves_1)
            else:
                moves_2= ["Pound", "Razor leaf"]
                cpu_choice = random.choice(moves_2)
            if cpu_choice == "Pound" or cpu_choice == "Razor leaf":
                if cpu_choice == "Pound":
                    pound_sound.play()
                if cpu_choice == "Razor leaf":
                    weapons_sound.play()
                    my_image_razor_left = my_canvas.create_image(350,650,image=photo_image_razor_left,anchor=SW)
                    move_razor_left()
                damage = int(random.choice(moves[cpu_choice]))
                other.health -= damage
                label_attack_enemy=Label(window,text="Bulbasaur attacks with " + cpu_choice + " dealing " + str(damage) + " damage.",font="Comic 12", bg="white")
                label_attack_enemy.config(width=50)
                my_canvas.create_window(240,750,window=label_attack_enemy)
            if cpu_choice == "Heal":
                heal_sound.play()
                hp = int(random.choice(moves[choice]))
                self.health += hp
                label_attack_enemy=Label(window,text="Bulbasaur uses heal and its health is now " + str(self.health),font="Comic 12", bg="white")
                label_attack_enemy.config(width=50)
                my_canvas.create_window(240,750,window=label_attack_enemy)
                label_health_enemy=Label(window,text="Health Enemy = "+str(self.health),font="Comic 16 bold", bg="pink")
                label_health_enemy.config(width=16)
                my_canvas.create_window(140,600,window=label_health_enemy)


#############################        
player=Player()
enemy=Enemy()
#############################

#defining images for pokemon
photo_image1 = PhotoImage(file='charmander_bg.png')
my_image1 = my_canvas.create_image(1550,700,image=photo_image1,anchor=SW)

photo_image2 = PhotoImage(file='Bulbasaur_bg_right.png')
my_image2 = my_canvas.create_image(1550,700,image=photo_image2,anchor=SW)

photo_image3 = PhotoImage(file='squirtle_bg.png')
my_image3 = my_canvas.create_image(1425,700,image=photo_image3,anchor=SW)


photo_image11 = PhotoImage(file='Squirtle_bg_left.png')
my_image11 = my_canvas.create_image(-500,700,image=photo_image11,anchor=SW)

photo_image22 = PhotoImage(file='Charmander_bg_left.png')
my_image22 = my_canvas.create_image(-500,700,image=photo_image22,anchor=SW)

photo_image33 = PhotoImage(file='bulbasaur_left_bg.png')
my_image33 = my_canvas.create_image(-350,700,image=photo_image33,anchor=SW)


#defining images for attack
photo_image_watergun_left = PhotoImage(file='watergun-bg.png')
photo_image_ember_right = PhotoImage(file='Ember_right_bg.png')
photo_image_watergun_right = PhotoImage(file='watergun-bg.png')
photo_image_ember_left = PhotoImage(file='Ember_left_bg.png')
photo_image_razor_right = PhotoImage(file='razor_leaf_right_bg.png')
photo_image_razor_left = PhotoImage(file='razor_leaf_left_bg.png')
###############




#defining the value of radiobuttons according to the pokemons 
radio1=Radiobutton(window,text="Charmander", font="Comic 12", bg="white",variable=var_pok,value=1)
radio2=Radiobutton(window,text="Bulbasaur",font="Comic 12", bg="white",variable=var_pok,value=2)
radio3=Radiobutton(window,text="Squirtle",font="Comic 12", bg="white",variable=var_pok,value=3)



radio4=Radiobutton(window,text="Scratch", font="Comic 12", bg="white",variable=var_atk,value=1)
radio5=Radiobutton(window,text="Ember", font="Comic 12", bg="white",variable=var_atk,value=2)
radio6=Radiobutton(window,text="Pound", font="Comic 12", bg="white",variable=var_atk,value=3)
radio7=Radiobutton(window,text="Razor leaf", font="Comic 12", bg="white",variable=var_atk,value=4)
radio8=Radiobutton(window,text="Tackle", font="Comic 12", bg="white",variable=var_atk,value=5)
radio9=Radiobutton(window,text="Watergun", font="Comic 12", bg="white",variable=var_atk,value=6)
radio10=Radiobutton(window,text="Heal", font="Comic 12", bg="white",variable=var_atk,value=7)



#Giving the label
label1=Label(window,text="Ash chooses", font="Comic 16 bold", bg="pink")
my_canvas.create_window(1100,20,window=label1)
label_move=Label(window,text="Choose your move",font="Comic 16 bold", bg="pink",)




my_canvas.create_window(1100,60,window=radio1)
my_canvas.create_window(1250,60,window=radio2)
my_canvas.create_window(1400,60,window=radio3)

#function for moving charmander on the right(player)
def move_fun1():
    coordinates=my_canvas.coords(my_image1)
    if(coordinates[0]>900):
        
        my_canvas.move(my_image1, -3, 0)
        window.after(20,move_fun1)


#function for moving bulbasaur on the right(player)
def move_fun2():
    coordinates=my_canvas.coords(my_image2)
    if(coordinates[0]>900):
        my_canvas.move(my_image2, -3, 0)
        window.after(20,move_fun2)


#function for moving squirtle on the right(player)
def move_fun3():
    coordinates=my_canvas.coords(my_image3)
    if(coordinates[0]>800):
        my_canvas.move(my_image3, -3, 0)
        window.after(20,move_fun3)


#function for moving charmander on the left(opponent)
def move_fun11():
    coordinates=my_canvas.coords(my_image11)
    if(coordinates[0]<250):
        my_canvas.move(my_image11, 3, 0)
        window.after(20,move_fun11)


#function for moving bulbasaur on the left(opponent)
def move_fun22():
    coordinates=my_canvas.coords(my_image22)
    if(coordinates[0]<250):
        my_canvas.move(my_image22, 3, 0)
        window.after(20,move_fun22)


#function for moving squirtle on the left(opponent)
def move_fun33():
    coordinates=my_canvas.coords(my_image33)
    if(coordinates[0]<250):
        my_canvas.move(my_image33, 3, 0)
        window.after(20,move_fun33)
        

#######################################################################
#function for moving the weapons(attack)
def move_watergun_left():
    coordinates=my_canvas.coords(my_image_watergun_left)
    if(coordinates[0]<1500):
        my_canvas.move(my_image_watergun_left, 4, 0)
        window.after(20,move_watergun_left)


def move_watergun_right():
    coordinates=my_canvas.coords(my_image_watergun_right)
    if(coordinates[0]<1500):
        my_canvas.move(my_image_watergun_right, -4, 0)
        window.after(20,move_watergun_right)
        

def move_ember_right():
    coordinates=my_canvas.coords(my_image_ember_right)
    if(coordinates[0]<1500):
        my_canvas.move(my_image_ember_right, -4, 0)
        window.after(20,move_ember_right)


def move_ember_left():
    coordinates=my_canvas.coords(my_image_ember_left)
    if(coordinates[0]<1600):
        my_canvas.move(my_image_ember_left, 4, 0)
        window.after(20,move_ember_left)


def move_razor_right():
    coordinates=my_canvas.coords(my_image_razor_right)
    if(coordinates[0]<1500):
        my_canvas.move(my_image_razor_right, -4, 0)
        window.after(20,move_razor_right)


def move_razor_left():
    coordinates=my_canvas.coords(my_image_razor_left)
    if(coordinates[0]<1500):
        my_canvas.move(my_image_razor_left, 4, 0)
        window.after(20,move_razor_left)
        

#######################################################################
#disabling the radiobuttons after the pokemon is selected
def disable_Poke_radio():
    radio1.configure(state=DISABLED) 
    radio2.configure(state=DISABLED) 
    radio3.configure(state=DISABLED)
    but1.configure(state=DISABLED )



def disable_move_radio():
    radio4.configure(state=DISABLED) 
    radio5.configure(state=DISABLED) 
    radio6.configure(state=DISABLED)
    radio7.configure(state=DISABLED) 
    radio8.configure(state=DISABLED) 
    radio9.configure(state=DISABLED)
    radio10.configure(state=DISABLED)
    but_attack.configure(state=DISABLED)
    


def enable_move_radio():
    radio4.configure(state=NORMAL) 
    radio5.configure(state=NORMAL) 
    radio6.configure(state=NORMAL)
    radio7.configure(state=NORMAL) 
    radio8.configure(state=NORMAL) 
    radio9.configure(state=NORMAL)
    radio10.configure(state=NORMAL)
    
    but_attack.configure(state=NORMAL)
    
        


#function for displaying the pokemon and their moves on the screen
def select_poke():
    #declaring radiobuttons for attacks
 
    if var_pok.get()==1:
        move_fun1()  
        move_fun11()
        entry_sound.play()
        label2=Label(window,text="Gary chooses Squirtle",font="Comic 16 bold", bg="pink")
        my_canvas.create_window(150,20,window=label2)
        my_canvas.create_window(1100,200,window=label_move)
        select_move()
       
        

    elif var_pok.get()==2:
        move_fun2() 
        move_fun22()
        entry_sound.play()
        label2=Label(window,text="Gary chooses Charmander",font="Comic 16 bold", bg="pink")
        my_canvas.create_window(150,20,window=label2)
        my_canvas.create_window(1100,200,window=label_move)
        select_move()
       

    elif var_pok.get()==3:
        move_fun3()
        move_fun33()
        entry_sound.play()
        pokemon2 = 'bulbasaur'
        label2=Label(window,text="Gary chooses Bulbasaur",font="Comic 16 bold", bg="pink")
        my_canvas.create_window(150,20,window=label2)
        my_canvas.create_window(1100,200,window=label_move)
        select_move()
        
    disable_Poke_radio()
    
    



def select_move():
    if var_pok.get()==1:
        my_canvas.create_window(1130,150,window=label_move)
        my_canvas.create_window(1100,190,window=radio4)
        my_canvas.create_window(1250,190,window=radio5)
        my_canvas.create_window(1400,190,window=radio10)
        my_canvas.create_window(1250,230,window=but_attack)
       
        

    elif var_pok.get()==2:
        my_canvas.create_window(1130,150,window=label_move)
        my_canvas.create_window(1100,190,window=radio6)
        my_canvas.create_window(1250,190,window=radio7)
        my_canvas.create_window(1400,190,window=radio10)
        my_canvas.create_window(1250,230,window=but_attack)
        
        

    elif var_pok.get()==3:
        my_canvas.create_window(1130,150,window=label_move)
        my_canvas.create_window(1100,190,window=radio8)
        my_canvas.create_window(1250,190,window=radio9)
        my_canvas.create_window(1400,190,window=radio10)
        my_canvas.create_window(1250,230,window=but_attack)
        

    

 
 

#When the button 'select' is clicked, the function select_poke will be called
but1=Button(window,text="select",font="Comic 12", bg="pink",command=select_poke)

but_attack=Button(window,text="Attack",font="Comic 12", bg="pink",command=battle1)

my_canvas.create_window(1200,100,window=but1)





window.mainloop()

###########################################################################
