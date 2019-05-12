#Medieval Demon Lord
from random import *
import os
from subprocess import *
import tkinter as tk
import copy

#Classes
class Stats: #Player/NPC class
    def __init__(self, name, hp, sp, strength, speed, defense, fed, dead):
        self.name = name
        self.hp = hp
        self.sp = sp
        self.strength = strength
        self.speed = speed
        self.defense = defense
        self.fed = fed
        self.dead = dead

class Resources: #Top level class for all resources
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Basic(Resources): #Just wood stuff
    def __init__(self, amount, fire, lastfire):
        Resources.__init__(self, "Wood", amount)
        self.fire = fire
        self.daysince = lastfire
    
class Metal(Resources): #Ore resources that are mineable
    def __init__(self, name, amount, obtain):
        Resources.__init__(self, name, amount)
        self.obtain = obtain

class Minion(Resources): #Different kinds of minions
    def __init__(self, name, amount, firepower, fed, demon):
        Resources.__init__(self, name, amount)
        self.firepower = firepower
        self.fed = fed
        self.demon = demon

class Food(Resources): #How much food?
    def __init__(self, amount):
        Resources.__init__(self, "Food Rations", amount)

class Time(Resources): #Time tracking
    def __init__(self, amount, actions):
        Resources.__init__(self, "Time", amount)
        self.actions = actions
        self.x = actions
            
class Combat(): #Combat checker
    def __init__(self, bandits, brigands, demons, baal):
        self.bandits = bandits
        self.brigands = brigands
        self.demons = demons
        self.baal = baal
    
class Game(): #all the values
    def __init__(self):
        self.Wood = Basic(1, False, -1)
        self.FoodRations = Food(1)
        self.Days = Time(7, 7)
        self.Player = Stats("Kevin", 200, 100, 1, 1, 1, True, False)
        self.Iron = Metal("Iron", 0, False)
        self.Steel = Metal("Steel", 0, False)
        self.Unobtainium = Metal("Unobtainium", 0, False)
        self.Bandits = Minion("Bandits", 0, 20, False, False)
        self.Brigands = Minion("Brigands", 0, 50, False, False)
        self.Demons = Minion("Demons", 0, 100, False, True)
        self.Baal = Minion("Baal", 0, 9999, False, True)
        self.Enemy1 = Stats("Bandit", 100, 50, 1, 1, 1, True, False)
        self.Enemy2 = Stats("Brigand", 200, 100, 3, 3, 3, True, False)
        self.Enemy3 = Stats("Demon", 500, 250, 10, 10, 10, True, False)
        self.Enemy4 = Stats("Baal", 500000, 250000, 5000, 5000, 5000, True, False)
        self.WoodenSword = Resources("Wooden Sword", 0)
        self.IronSword = Resources("Iron Sword", 0)
        self.SteelSword = Resources("Steel Sword", 0)
        self.UnobtainiumSword = Resources("Unobtainium Sword", 0)
        self.WoodArmor = Resources("Wood Armor", 0)
        self.IronArmor = Resources("Iron Armor", 0)
        self.SteelArmor = Resources("Steel Armor", 0)
        self.UnobtainiumArmor = Resources("Unobtainium Armor", 0)
        self.CurrEquipment = Stats("Equipment", 0, 0, 0, 0, 0, False, False)
        self.Temp1 = "CL4PTR4P"
        self.Temp2 = "Wall Sphinkters"
        self.Combats = Combat(False, False, False, False)
        self.ActionCap = Combat(10,10,10,50)
        self.Hero = Stats("Hero", 10000, 2500, 300, 300, 300, True, False)

def main():
    program = GUI()
    print("""You are the offspring of a demon lord. In this medieval world, everyone's claim to land is determined by one thing alone: Power.
However, your mother has disappeared and your father has been ill for quite some time. At one point, your father commanded many minions.
Due to his sickness, his minions have abandoned him, and you alone are left with quite a task: A hero is coming to take your land from you.
You must defend your homeland, rebuild your father's army, and defeat the coming threat!
          """)
    program.window.mainloop()

class GUI:
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Medieval Demon Lord")
        self.game = Game()
        self.victory = False

        def unbind(event):
            return

        def DeathCheck():
            if self.victory == True:
                changeBackground(self.victory)
            if self.game.Player.dead == True:
                if self.victory == True:
                    changeBackground(self.victory)
                else:
                    changeBackground(self.death)
                    self.f1b1['command'] = lambda:unbind2()
                    self.f1b2['command'] = lambda:unbind2()
                    self.f1b3['command'] = lambda:unbind2()
                    self.f1b4['command'] = lambda:unbind2()
                    self.f1b5['command'] = lambda:unbind2()
                    self.f1b6['command'] = lambda:unbind2()
                    self.f1b7['command'] = lambda:unbind2()
                    self.f1b8['command'] = lambda:unbind2()
                    self.f1b9['command'] = lambda:unbind2()
                    self.f1b10['command'] = lambda:unbind2()
                    self.console['text'] += "\n\nQuit and reopen the file to play again"
                    self.window.bind("y",end)
                    self.window.bind("n",end)

        def unbind2():
            return
                
        def end(event):
            key = event.char
            if key == "y":
                main()
            elif key == "n":
                os._exit(0)
                
        def NightSequence():
            if self.game.Wood.fire == False:
                self.console['text'] ="Don't forget the torches. You fell to your deat while wandering the castle in the dark..."
                self.game.Player.dead = True
                DeathCheck()
                return
            if self.game.Wood.daysince == 3:
                self.game.Wood.fire = False
                self.console['text'] +="\n\nYour torches have gone out!"
            if self.game.FoodRations.amount >=1+self.game.Bandits.amount+self.game.Brigands.amount+self.game.Demons.amount+self.game.Baal.amount:
                self.game.FoodRations.amount -= 1+self.game.Bandits.amount+self.game.Brigands.amount+self.game.Demons.amount+self.game.Baal.amount
                changeBackground(self.startPic)
                self.game.Player.fed = True
                self.game.Bandits.fed = True
                self.game.Brigands.fed = True
                self.game.Demons.fed = True
                self.game.Baal.fed = True
                self.console['text'] += "\n\nEveryone in your castle ate a days worth of food. You now have "+str(self.game.FoodRations.amount)+" ration(s) of food left."
            else:
                if self.game.Bandits.amount+self.game.Brigands.amount+self.game.Demons.amount+self.game.Baal.amount == 0:
                    self.console['text'] ="You're not sure why, but going hungry for a day drove you mad. You died wandering the castle at night"
                    self.game.Player.dead = True
                    DeathCheck()
                    return
                else:
                    self.console['text'] ="Because you didn't feed all your minions, they staged a mutiny and killed you..."
                    self.game.Player.dead = True
                    DeathCheck()
                    return
            self.game.Days.actions = self.game.Days.x
            if self.game.Bandits.amount+self.game.Brigands.amount+self.game.Demons.amount+self.game.Baal.amount != 0:
                if self.game.Bandits.amount*3 < self.game.ActionCap.bandits:
                    self.game.Days.actions += self.game.Bandits.amount*3
                else:
                    self.game.Days.actions += self.game.ActionCap.bandits
                if self.game.Brigands.amount*2 < self.game.ActionCap.brigands:
                    self.game.Days.actions += self.game.Brigands.amount*2
                else:
                    self.game.Days.actions += self.game.ActionCap.brigands
                if self.game.Demons.amount < self.game.ActionCap.demons:
                    self.game.Days.actions += self.game.Demons.amount
                else:
                    self.game.Days.actions += self.game.ActionCap.demons
                self.game.Days.actions += self.game.Baal.amount*50
            if self.game.Days.amount == -1:
                changeBackground(self.heroPic)
                finalFight()
            else:
                self.console['text'] += "\n\nIt is the next day! You have "+str(self.game.Days.actions)+" actions left in this day and "+str(self.game.Days.amount)+" day(s) left." 

        def timePass():
            countAll()
            if self.game.Days.actions != 0:
                self.game.Days.actions -= 1
            if self.game.Days.actions > 0:
                self.console['text'] +="\n\nYou have "+str(self.game.Days.actions)+" action(s) left in this day and "+str(self.game.Days.amount)+" day(s) left."
            if self.game.Days.actions == 0:
                self.game.Days.amount -= 1
                self.game.Wood.daysince += 1
                NightSequence()
                
        def getWood():
            changeBackground(self.cut)
            x = randrange(1,5)
            if self.game.Bandits.amount > 0:
                x += randrange(0, self.game.Bandits.amount*2)
            if self.game.Brigands.amount > 0:
                x += randrange(0, self.game.Brigands.amount*4)
            if self.game.Demons.amount > 0:
                x += randrange(0, self.game.Demons.amount)
            x += self.game.Baal.amount*100
            self.game.Wood.amount += x
            self.console['text'] = "You got "+str(x)+" Wood. You now have "+str(self.game.Wood.amount)+" Wood."
            timePass()

        def getFood():
            changeBackground(self.hunt)
            x = randrange(0,7)+self.game.Bandits.amount+self.game.Brigands.amount+self.game.Demons.amount+self.game.Baal.amount*1000
            self.game.FoodRations.amount += x
            self.console['text'] = "You hunted "+str(x)+" ration(s) worth of food. You now have "+str(self.game.FoodRations.amount)+" ration(s)."
            timePass()

        def lightTorches():
            self.console['text'] = ""
            if self.game.Wood.fire == False and self.game.Wood.amount > 0:
                changeBackground(self.lightPic)
                self.game.Wood.amount -= 1
                self.game.Wood.fire = True
                self.console['text'] = "You use one wood to light the torches in your castle."
                self.game.Wood.daysince = 0
                timePass()
            elif self.game.Wood.amount == 0:
                self.console['text'] = "You don't have enough wood to light your torches!"
            else:
                self.console['text'] = "Your torches are already lit!"

        def train():
            self.console['text'] =\
"""
What would you like to train?
(a) HP
(b) SP
(c) Strength
(d) Defense
(e) Speed
"""
            for i in ['a','b','c','d','e']:
                self.window.bind(i,train2)

        def train1(stats,num,num2):
            self.console['text'] = "You increase your "+stats+" from "+str(num)+" to "+str(num2)
        def train2(event):
            for i in ['a','b','c','d','e']:
                self.window.bind(i,unbind)
            key = event.char
            if key == 'a':
                changeBackground(self.trainPic)
                x = randrange(10,50+self.game.Bandits.amount*20+self.game.Brigands.amount*50+self.game.Demons.amount*100+self.game.Baal.amount*10000)
                a = self.game.Player.hp
                self.game.Player.hp += x
                train1("HP",a,self.game.Player.hp)
            elif key == 'b':
                changeBackground(self.trainPic)
                x = randrange(5,30+self.game.Bandits.amount*15+self.game.Brigands.amount*35+self.game.Demons.amount*50+self.game.Baal.amount*5000)
                a = self.game.Player.sp
                self.game.Player.sp += x
                train1("SP",a,self.game.Player.sp)
            elif key == 'c':
                changeBackground(self.trainPic)
                x = randrange(1,5+self.game.Bandits.amount*2+self.game.Brigands.amount*4+self.game.Demons.amount*8+self.game.Baal.amount*100)
                a = self.game.Player.strength
                self.game.Player.strength += x
                train1("strength",a,self.game.Player.strength)
            elif key == 'd':
                changeBackground(self.trainPic)
                x = randrange(1,5+self.game.Bandits.amount*2+self.game.Brigands.amount*4+self.game.Demons.amount*8+self.game.Baal.amount*100)
                a = self.game.Player.defense
                self.game.Player.defense += x
                train1("defense",a,self.game.Player.defense)
            elif key == 'e':
                changeBackground(self.speedPic)
                x = randrange(1,5+self.game.Bandits.amount*2+self.game.Brigands.amount*4+self.game.Demons.amount*8+self.game.Baal.amount*100)
                a = self.game.Player.speed
                self.game.Player.speed += x
                train1("speed",a,self.game.Player.speed)
            timePass()
        def CheckInv():
            self.console['text'] = "Food: "+str(self.game.FoodRations.amount)+\
                                   "\nWood: "+str(self.game.Wood.amount)+" / Wooden Sword: "+str(self.game.WoodenSword.amount)+" / Wood Armor: "+str(self.game.WoodArmor.amount)+\
                                   "\nIron: "+str(self.game.Iron.amount)+" / Iron Sword: "+str(self.game.IronSword.amount)+" / Iron Armor: "+str(self.game.IronArmor.amount)+\
                                   "\nSteel: "+str(self.game.Steel.amount)+" / Steel Sword: "+str(self.game.SteelSword.amount)+" / Steel Armor: "+str(self.game.SteelArmor.amount)+\
                                   "\nUnobtainium: "+str(self.game.Unobtainium.amount)+" / Unobtainium Sword: "+str(self.game.UnobtainiumSword.amount)+" / Unobtainium Armor: "+str(self.game.UnobtainiumArmor.amount)
        def CheckStats():
            self.console['text'] = "HP: "+str(self.game.Player.hp)+\
                                   "\nSP: "+str(self.game.Player.sp)+\
                                   "\nStrength: "+str(self.game.Player.strength+self.game.CurrEquipment.strength)+\
                                   "\nDefense: "+str(self.game.Player.defense+self.game.CurrEquipment.defense)+\
                                   "\nSpeed: "+str(self.game.Player.speed)

        def craft():
            self.console['text'] =\
                                 """
        If you have the right resources, you can craft...
        
        (a) Wooden Pickaxe: 3 Wood
        (b) Steel Ingot: 2 Wood, 2 Iron
        (c) Sword: 3 of one resource
        (d) Armor: 8 of one resource
                                """
            for i in ['a','b','c','d']:
                self.window.bind(i,craft2)

        def craft2(event):
            for i in ['a','b','c','d']:
                self.window.bind(i,unbind)
            key = event.char
            if key == 'a':
                if self.game.Iron.obtain == True:
                    self.console['text'] = "You already crafted a wooden pickaxe!"
                elif self.game.Wood.amount >= 3:
                    changeBackground(self.craftPic)
                    self.game.Wood.amount -= 3
                    self.game.Iron.obtain = True
                    self.console['text'] = "You crafted a wooden pickaxe. You now have "+str(self.game.Wood.amount)+" wood. You might be able to obtain iron..."
                    timePass()
                else:
                    self.console['text'] = "You don't have enough wood to craft that!"
            elif key == 'b':
                if self.game.Wood.amount >= 2 and self.game.Iron.amount >= 2:
                    changeBackground(self.smithPic)
                    self.game.Wood.amount -= 2
                    self.game.Iron.amount -= 2
                    self.game.Steel.amount += 1
                    self.console['text'] = "Your further refined iron into steel. You now have "+str(self.game.Wood.amount)+" wood, "+str(self.game.Iron.amount)+" iron, and "+str(self.game.Steel.amount)+" steel."
                    timePass()
                else:
                    self.console['text'] = "You don't have enough materials to craft that!"
            elif key == 'c':
                for i in ['a','b','c','d']:
                    self.window.bind(i,craft3)
                self.console['text'] = """
                What would you like to make a sword out of?
                (a) Wood
                (b) Iron
                (c) Steel
                (d) Unobtainium
                                """
            elif key == 'd':
                for i in ['a','b','c','d']:
                    self.window.bind(i,craft4)
                self.console['text'] = """
                What would you like to make armor out of?
                (a) Wood
                (b) Iron
                (c) Steel
                (d) Unobtainium
                                """
                
        def craft3(event):
            key = event.char
            if key == 'a':
                if self.game.Wood.amount >= 3:
                    changeBackground(self.craftPic)
                    self.game.Wood.amount -= 3
                    self.game.WoodenSword.amount += 1
                    self.console['text'] = "You made a Wooden Sword."
                    timePass()
                else:
                    self.console['text'] = "You don't have enough materials to craft that!"
            elif key == 'b':
                if self.game.Iron.amount >= 3:
                    changeBackground(self.smithPic)
                    self.game.Iron.amount -= 3
                    self.game.IronSword.amount += 1
                    self.console['text'] = "You made an Iron Sword."
                    timePass()
                else:
                    self.console['text'] = "You don't have enough materials to craft that!"
            elif key == 'c':
                if self.game.Steel.amount >= 3:
                    changeBackground(self.smithPic)
                    self.game.Steel.amount -= 3
                    self.game.SteelSword.amount += 1
                    self.console['text'] = "You made a Steel Sword."
                    timePass()
                else:
                    self.console['text'] = "You don't have enough materials to craft that!"
            elif key == 'd':
                if self.game.Unobtainium.amount >= 3:
                    changeBackground(self.smithPic)
                    self.game.Unobtainium.amount -= 3
                    self.game.UnobtainiumSword.amount += 1
                    self.console['text'] = "You made an Unobtainium Sword."
                    timePass()
                else:
                    self.console['text'] = "You don't have enough materials to craft that!"
            for i in ['a','b','c','d']:
                self.window.bind(i,unbind)

        def craft4(event):
            key = event.char
            if key == 'a':
                if self.game.Wood.amount >= 8:
                    changeBackground(self.craftPic)
                    self.game.Wood.amount -= 8
                    self.game.WoodenArmor.amount += 1
                    self.console['text'] = "You made Wood Armor."
                    timePass()
                else:
                    self.console['text'] = "You don't have enough materials to craft that!"
            elif key == 'b':
                if self.game.Iron.amount >= 8:
                    changeBackground(self.smithPic)
                    self.game.Iron.amount -= 8
                    self.game.IronArmor.amount += 1
                    self.console['text'] = "You made Iron Armor."
                    timePass()
                else:
                    self.console['text'] = "You don't have enough materials to craft that!"
            elif key == 'c':
                if self.game.Steel.amount >= 8:
                    changeBackground(self.smithPic)
                    self.game.Steel.amount -= 8
                    self.game.SteelArmor.amount += 1
                    self.console['text'] = "You made Steel Armor."
                    timePass()
                else:
                    self.console['text'] = "You don't have enough materials to craft that!"
            elif key == 'd':
                if self.game.Unobtainium.amount >= 8:
                    changeBackground(self.smithPic)
                    self.game.Unobtainium.amount -= 8
                    self.game.UnobtainiumArmor.amount += 1
                    self.console['text'] = "You made Unobtainium Armor."
                    timePass()
                else:
                    self.console['text'] = "You don't have enough materials to craft that!"
            for i in ['a','b','c','d']:
                self.window.bind(i,unbind)

        def equip():
            for i in ['a','b','c','d','e','f','g','h']:
                self.window.bind(i,equip2)
                self.console['text'] = """
                What would you like to equip?
                Wooden (a) Sword / (b) Armor
                Iron (c) Sword / (d) Armor
                Steel (e) Sword / (f) Armor
                Unobtainium (g) Sword / (h) Armor
                                """
        def equip2(event):
            key = event.char
            if key == 'a' and self.game.WoodenSword.amount >= 1:
                self.game.CurrEquipment.strength = 10
                self.console['text'] = "You equipped a Wooden Sword!"
            elif key == 'b' and self.game.WoodArmor.amount >= 1:
                self.game.CurrEquipment.defense = 20
                self.console['text'] = "You equipped Wood Armor!"
            elif key == 'c' and self.game.IronSword.amount >= 1:
                self.game.CurrEquipment.strength = 50
                self.console['text'] = "You equipped an Iron Sword!"
            elif key == 'd' and self.game.IronArmor.amount >= 1:
                self.game.CurrEquipment.defense = 100
                self.console['text'] = "You equipped Iron Armor!"
            elif key == 'e' and self.game.SteelSword.amount >= 1:
                self.game.CurrEquipment.strength = 300
                self.console['text'] = "You equipped a Steel Sword!"
            elif key == 'f' and self.game.SteelArmor.amount >= 1:
                self.game.CurrEquipment.defense = 600
                self.console['text'] = "You equipped Steel Armor!"
            elif key == 'g' and self.game.UnobtainiumSword.amount >= 1:
                self.game.CurrEquipment.strength = 2500
                self.console['text'] = "You equipped an Unobtainium Sword!"
            elif key == 'h' and self.game.UnobtainiumArmor.amount >= 1:
                self.game.CurrEquipment.defense = 5000
                self.console['text'] = "You equipped Unobtainium Armor!"
            else:
                self.console['text'] = "You don't have that piece of equipment."
            for i in ['a','b','c','d','e','f','g','h']:
                self.window.bind(i,unbind)

        def getIron():
            if self.game.Iron.obtain == True:
                changeBackground(self.minePic)
                x = randrange(1,3)
                if self.game.Bandits.amount > 0:
                    x += randrange(0, self.game.Bandits.amount*2)
                if self.game.Brigands.amount > 0:
                    x += randrange(0, self.game.Brigands.amount*4)
                if self.game.Demons.amount > 0:
                    x += randrange(0, self.game.Demons.amount)
                x += self.game.Baal.amount*100
                self.game.Iron.amount += x
                self.console['text'] = "You mined and processed "+str(x)+" piece(s) of iron ore. You now have "+str(self.game.Iron.amount)+" iron ingot(s)."
                timePass()
            else:
                self.console['text'] = "You don't have the tools to mine iron yet."

        def combatSequence(x):
            self.game.Temp1 = copy.deepcopy(self.game.Player)
            self.game.Temp1.strength += self.game.CurrEquipment.strength
            self.game.Temp1.defense += self.game.CurrEquipment.defense
            if x == 1:
                changeBackground(self.banditPic)
                self.game.Temp2 = copy.deepcopy(self.game.Enemy1)
                self.console['text'] = "Initiating combat sequence with a Bandit... Press (x) to continue."
            elif x == 2:
                changeBackground(self.brigandPic)
                self.game.Temp2 = copy.deepcopy(self.game.Enemy2)
                self.console['text'] = "Initiating combat sequence with a Brigand... Press (x) to continue."
            elif x == 3:
                changeBackground(self.demonPic)
                self.game.Temp2 = copy.deepcopy(self.game.Enemy3)
                self.console['text'] = "Initiating combat sequence with a Demon... Press (x) to continue."
            elif x == 4:
                self.game.Temp2 = copy.deepcopy(self.game.Enemy4)
                self.console['text'] = "Initiating combat sequence with Baal... Press (x) to continue."
                changeBackground(self.baalPic)
            self.window.bind('x',combatLoop)

        def combatLoop(event):
            key = event.char
            if key == 'x':
                self.window.bind('x',combatTurn)

        def combatTurn(event):
            key = event.char
            hit = self.game.Temp1.strength*4-self.game.Temp2.defense*2
            hit2 = self.game.Temp2.strength*4-self.game.Temp1.defense*2
            if hit < 0:
                hit = 0
            if hit2 < 0:
                hit2 = 0
            if key == 'x':
                if self.game.Temp1.speed >= self.game.Temp2.speed:
                    self.game.Temp2.hp -= hit
                    self.console['text'] = "You hit the enemy for "+str(hit)+" points of damage."
                    combatCheck2()
                    if self.game.Temp2.hp > 0:
                        self.game.Temp1.hp -= hit2
                        self.console['text'] += "\n\nThe enemy hit you for "+str(hit2)+" points of damage."
                        combatCheck()
                        self.console['text'] += "\n\nYou have "+str(self.game.Temp1.hp)+" hit points. The enemy has "+str(self.game.Temp2.hp)+" hit points."
                else:
                    self.game.Temp1.hp -= hit2
                    self.console['text'] = "The enemy hit you for "+str(hit2)+" points of damage."
                    combatCheck()
                    if self.game.Temp1.hp > 0:
                        self.game.Temp2.hp -= hit
                        self.console['text'] += "\n\nYou hit the enemy for "+str(hit)+" points of damage."
                        combatCheck2()
                    if self.game.Temp2.hp > 0:
                        self.console['text'] += "\n\nYou have "+str(self.game.Temp1.hp)+" hit points. The enemy has "+str(self.game.Temp2.hp)+" hit points."

        def finalFight():
            self.game.Temp1 = copy.deepcopy(self.game.Player)
            self.game.Temp1.strength += self.game.CurrEquipment.strength
            self.game.Temp1.defense += self.game.CurrEquipment.defense
            self.game.Temp2 = copy.deepcopy(self.game.Hero)
            if self.game.Baal.amount == 1:
                self.console['text'] = "Baal annihilates the hero, and ensures your family, for generations to come, will survive...\n\nThe end."
                self.game.Player.dead = True
                DeathCheck()
            else:
                self.console['text'] = "The hero approaches the castle."
                if self.game.Bandits.amount+self.game.Brigands.amount+self.game.Demons.amount+self.game.Baal.amount != 0:
                    self.game.Temp2.hp = self.game.Temp2.hp*5
                    self.game.Temp2.strength = self.game.Temp2.strength*5
                    self.game.Temp2.defense = self.game.Temp2.defense*5
                    self.game.Temp2.speed = self.game.Temp2.speed*5
                    weaken = self.game.Bandits.firepower*self.game.Bandits.amount + self.game.Brigands.firepower*self.game.Brigands.amount + self.game.Demons.firepower*self.game.Demons.amount
                    self.game.Temp2.hp -= weaken/100
                    self.game.Temp2.strength -= weaken/1000
                    self.game.Temp2.defense -= weaken/1000
                    self.game.Temp2.speed -= weaken/1000
                    self.console['text'] += " Your minions take him on, weakening him, but are ultimately no match..."
                else:
                    self.console['text'] += " You alone stand against the hero... Will your training be sufficient?"
                self.console['text'] +=  "\nTime for one final fight... \nPress x to continue..."
                self.window.bind('x',combatLoop)

        def combatCheck():
            if self.game.Temp1.hp <= 0:
                self.game.Player.dead = True
                self.console['text'] = "You died in combat."
                self.window.bind('x', unbind)
                DeathCheck()
                
        def combatCheck2():
            if self.game.Temp2.hp <= 0:
                weaken = self.game.Bandits.firepower*self.game.Bandits.amount + self.game.Brigands.firepower*self.game.Brigands.amount + self.game.Demons.firepower*self.game.Demons.amount
                if self.game.Temp2.defense == self.game.Enemy1.defense:
                    self.game.Bandits.amount += 1
                    self.console['text'] += "\n\nYou successfully recruited a bandit."
                    self.game.Combats.bandits = True
                if self.game.Temp2.defense == self.game.Enemy2.defense:
                    self.game.Brigands.amount += 1
                    self.console['text'] += "\n\nYou successfully recruited a brigand."
                    self.game.Combats.brigands = True
                if self.game.Temp2.defense == self.game.Enemy3.defense:
                    self.game.Demons.amount += 1
                    self.console['text'] += "\n\nYou successfully recruited a demon."
                    self.game.Combats.demons = True
                if self.game.Temp2.defense == self.game.Enemy4.defense:
                    self.game.Baal.amount += 1
                    self.console['text'] += "\n\nYou successfully recruited Baal."
                    self.game.Combats.baal = True
                if self.game.Temp2.defense == self.game.Hero.defense or self.game.Temp2.defense == self.game.Hero.defense*5 - weaken/1000:
                    self.victory = True
                    changeBackground(self.heroPic)
                    self.console['text'] = "You have defeated the hero in place of your father!\nBut he was only the first of many...\nHow long will your legacy continue?\n\nThe end?"
                    self.game.Player.dead = True
                    DeathCheck()
                self.window.bind('x', unbind)

        def Recruit():
            self.console['text'] = "Who would you like to recruit? \n\n(a)Bandits: "+str(self.game.Bandits.amount)+"\n(b)Brigands: "+str(self.game.Brigands.amount)+"\n(c)Demons: "+str(self.game.Demons.amount)+"\n(d)Baal: "+str(self.game.Baal.amount)
            for i in ['a','b','c','d']:
                self.window.bind(i,Recruit2)

        def Recruit2(event):
            for i in ['a','b','c','d']:
                self.window.bind(i,unbind)
            key = event.char
            if key == 'a':
                if self.game.Combats.bandits == True:
                    changeBackground(self.banditPic)
                    self.game.Bandits.amount += 1
                    self.console['text'] = "You successfully recruited a bandit."
                    timePass()
                else:
                    combatSequence(1)
                    timePass()
            elif key == 'b':
                if self.game.Combats.brigands == True:
                    changeBackground(self.brigandPic)
                    self.game.Brigands.amount += 1
                    self.console['text'] = "You successfully recruited a brigand."
                    timePass()
                else:
                    combatSequence(2)
                    timePass()
            elif key == 'c':
                if self.game.Combats.demons == True:
                    changeBackground(self.demonPic)
                    self.game.Demons.amount += 1
                    self.console['text'] = "You successfully recruited a demon."
                    timePass()
                else:
                    combatSequence(3)
                    timePass()
            elif key == 'd':
                if self.game.Combats.baal == True:
                    self.console['text'] = "You've already recruited Baal!"
                else:
                    combatSequence(4)
                    timePass()

        # Pictures

        self.wood = tk.PhotoImage(file = "wood.png")
        self.background = tk.PhotoImage(file = "background.png")
        self.nothing = tk.PhotoImage(file="nothing.png")
        self.food = tk.PhotoImage(file="food.png")
        self.iron = tk.PhotoImage(file="iron.png")
        self.steel= tk.PhotoImage(file="steel.png")
        self.bandit = tk.PhotoImage(file="bandit.png")
        self.deamon = tk.PhotoImage(file="deamon.png")
        self.brigand = tk.PhotoImage(file="brigand.png")
        self.Str = tk.PhotoImage(file="Strength.png")
        self.Def = tk.PhotoImage(file="Defence.png")
        self.Hp = tk.PhotoImage(file="Hitpoints.png")
        self.Spd = tk.PhotoImage(file="Speed.png")
        self.SP = tk.PhotoImage(file="Magic.png")
        self.hunt1 = tk.PhotoImage(file="hunt1.png")
        self.hunt2 = tk.PhotoImage(file="hunt2.png")
        self.hunt3 = tk.PhotoImage(file="hunt3.png")
        self.hunt4 = tk.PhotoImage(file="hunt4.png")
        self.cut1 = tk.PhotoImage(file="cut1.png")
        self.cut2 = tk.PhotoImage(file="cut2.png")
        self.cut3 = tk.PhotoImage(file="cut3.png")
        self.cut4 = tk.PhotoImage(file="cut4.png")
        self.cut5 = tk.PhotoImage(file="cut5.png")
        self.cut6 = tk.PhotoImage(file="cut6.png")
        self.cut7 = tk.PhotoImage(file="cut7.png")
        self.speed1 = tk.PhotoImage(file="speed1.png")
        self.speed2 = tk.PhotoImage(file="speed2.png")
        self.speed3 = tk.PhotoImage(file="speed3.png")
        self.speed4 = tk.PhotoImage(file="speed4.png")
        self.train1 = tk.PhotoImage(file="train1.png")
        self.train2 = tk.PhotoImage(file="train2.png")
        self.train3 = tk.PhotoImage(file="train3.png")
        self.train4 = tk.PhotoImage(file="train4.png")
        self.mining1 = tk.PhotoImage(file="mining1.png")
        self.mining2 = tk.PhotoImage(file="mining2.png")
        self.mining3 = tk.PhotoImage(file="mining3.png")
        self.mining4 = tk.PhotoImage(file="mining4.png")
        self.smith1 = tk.PhotoImage(file="smith.png")
        self.smith2 = tk.PhotoImage(file="smith2.png")
        self.bandit1 = tk.PhotoImage(file="bandit1.png")
        self.bandit2 = tk.PhotoImage(file="bandit2.png")
        self.brigand1 = tk.PhotoImage(file="brigand1.png")
        self.brigand2 = tk.PhotoImage(file="brigand2.png")
        self.demon1 = tk.PhotoImage(file="demon1.png")
        self.end = tk.PhotoImage(file="end.png")
        self.end2 = tk.PhotoImage(file="end2.png")
        self.hero = tk.PhotoImage(file="hero.png")
        self.Craft = tk.PhotoImage(file="craft.png")
        self.baal = tk.PhotoImage(file="baal.png")
        self.light = tk.PhotoImage(file="light.png")
        self.start = tk.PhotoImage(file="start.png")

        self.lightPic = [self.light]
        self.baalPic = [self.baal]
        self.craftPic = [self.Craft]
        self.heroPic = [self.hero]
        self.victory = [self.end]
        self.death = [self.end2]
        self.startPic = [self.start]
        self.hunt = [self.hunt1,self.hunt2,self.hunt3,self.hunt4]
        self.trainPic = [self.train1,self.train2,self.train3,self.train4]
        self.speedPic = [self.speed1,self.speed2,self.speed3,self.speed4]
        self.cut = [self.cut1,self.cut2,self.cut3,self.cut4,self.cut5,self.cut6,self.cut7]
        self.minePic=[self.mining1,self.mining2,self.mining3,self.mining4]
        self.smithPic = [self.smith1,self.smith2]
        self.banditPic=[self.bandit1,self.bandit2]
        self.brigandPic = [self.brigand1,self.brigand2]
        self.demonPic = [self.demon1]
        self.woke = [self.background]

        def changeBackground(List):
            Len = len(List)
            num = randrange(Len)
            file = List[num]
            self.canvas.itemconfig(self.background,image=file)

       # Display Frames

        self.f3 = tk.LabelFrame(self.window)
        self.f3.grid(column=3,row=0,rowspan=3,sticky='n'+'s'+'e'+'w')

        self.f3a = tk.LabelFrame(self.f3,relief="ridge")
        self.f3a.grid(column=1,row=1,sticky='n'+'s'+'e'+'w')

        self.f3b = tk.LabelFrame(self.f3,relief="ridge")
        self.f3b.grid(column=1,row=2,sticky='n'+'s'+'e'+'w')

        self.f3c = tk.LabelFrame(self.f3,relief="ridge")
        self.f3c.grid(column=1,row=3,sticky='n'+'s'+'e'+'w',ipady=30)

        # Resource Displays 

        self.frameT = tk.LabelFrame(self.window,relief="ridge")
        self.frameT.grid(column=1,row=0,columnspan=2,sticky='w'+'e'+'s'+'n')

        self.labelT1 = tk.Label(self.f3b,image=self.wood)
        self.labelT1.grid(column=1,row=1)
        
        self.labelT2 = tk.Label(self.f3b,text="1",font="courier 30")
        self.labelT2.grid(column=2,row=1,sticky=tk.E)

        self.labelT3 = tk.Label(self.f3b,image=self.food)
        self.labelT3.grid(column=1,row=2)

        self.labelT4 = tk.Label(self.f3b,text="1",font="courier 30")
        self.labelT4.grid(column=2,row=2)

        self.labelT5 = tk.Label(self.f3b,image=self.iron)
        self.labelT5.grid(column=1,row=3)
        
        self.labelT6 = tk.Label(self.f3b,text="0",font="courier 30")
        self.labelT6.grid(column=2,row=3)

        self.labelT7 = tk.Label(self.f3b,image=self.steel)
        self.labelT7.grid(column=1,row=4)

        self.labelT8 = tk.Label(self.f3b,text="0",font="courier 30")
        self.labelT8.grid(column=2,row=4)

        # Minions Display

        self.labelT9 = tk.Label(self.f3c,image=self.bandit)
        self.labelT9.grid(column=1,row=1)

        self.labelT10 = tk.Label(self.f3c,text="0",font="courier 30")
        self.labelT10.grid(column=2,row=1,ipady=3)

        self.labelT11 = tk.Label(self.f3c,image=self.brigand)
        self.labelT11.grid(column=1,row=2,ipady=3)

        self.labelT12 = tk.Label(self.f3c,text="0",font="courier 30")
        self.labelT12.grid(column=2,row=2,ipady=3)

        self.labelT13 = tk.Label(self.f3c,image=self.deamon)
        self.labelT13.grid(column=1,row=3,ipady=3)

        self.labelT14 = tk.Label(self.f3c,text="0",font="courier 30")
        self.labelT14.grid(column=2,row=3,ipady=3)
        
        # Stats Display

        self.labelT15 = tk.Label(self.f3a,image=self.Hp)
        self.labelT15.grid(column=1,row=1)

        self.labelT16 = tk.Label(self.f3a,text="200",font="courier 30")
        self.labelT16.grid(column=2,row=1)

        self.labelT17 = tk.Label(self.f3a,image=self.SP)
        self.labelT17.grid(column=1,row=2)

        self.labelT18 = tk.Label(self.f3a,text="100",font="courier 30")
        self.labelT18.grid(column=2,row=2)

        self.labelT19 = tk.Label(self.f3a,image=self.Def)
        self.labelT19.grid(column=1,row=3)

        self.labelT20 = tk.Label(self.f3a,text="1",font="courier 30")
        self.labelT20.grid(column=2,row=3)

        self.labelT21 = tk.Label(self.f3a,image=self.Spd)
        self.labelT21.grid(column=1,row=4)

        self.labelT22 = tk.Label(self.f3a,text="1",font="courier 30")
        self.labelT22.grid(column=2,row=4)

        self.labelT23 = tk.Label(self.f3a,image=self.Str)
        self.labelT23.grid(column=1,row=5)

        self.labelT24 = tk.Label(self.f3a,text="1",font="courier 30")
        self.labelT24.grid(column=2,row=5)
        

        def countAll():
            self.labelT2['text'] = str(self.game.Wood.amount)
            self.labelT4['text'] = str(self.game.FoodRations.amount)
            self.labelT6['text'] = str(self.game.Iron.amount)
            self.labelT8['text'] = str(self.game.Steel.amount)
            self.labelT10['text'] = str(self.game.Bandits.amount)
            self.labelT12['text'] = str(self.game.Brigands.amount)
            self.labelT14['text'] = str(self.game.Demons.amount)
            self.labelT16['text'] = str(self.game.Player.hp)
            self.labelT18['text'] = str(self.game.Player.sp)
            self.labelT20['text'] = str(self.game.Player.defense)
            self.labelT22['text'] = str(self.game.Player.speed)
            self.labelT24['text'] = str(self.game.Player.strength)
            
       

       # Frame1 (buttons)
        self.f1 = tk.LabelFrame(self.window,relief = "ridge")
        self.f1.grid(row=1,column=1,sticky='n'+'s'+'e'+'w')

        # Creating Buttons 
        self.f1b1 = tk.Button(self.f1,text="GetWood")
        self.f1b2 = tk.Button(self.f1,text="Light")
        self.f1b3 = tk.Button(self.f1,text="Train")
        self.f1b4 = tk.Button(self.f1,text="GetFood")
        self.f1b5 = tk.Button(self.f1,text="CheckStats")
        self.f1b6 = tk.Button(self.f1,text="CheckInv")
        self.f1b7 = tk.Button(self.f1,text="GetIron")
        self.f1b8 = tk.Button(self.f1,text="Craft")
        self.f1b9 = tk.Button(self.f1,text="Recruit")
        self.f1b10 = tk.Button(self.f1,text="Equip")

        self.f1b1['command'] = lambda:getWood()
        self.f1b2['command'] = lambda:lightTorches()
        self.f1b3['command'] = lambda:train()
        self.f1b4['command'] = lambda:getFood()
        self.f1b5['command'] = lambda:CheckStats()
        self.f1b6['command'] = lambda:CheckInv()
        self.f1b7['command'] = lambda:getIron()
        self.f1b8['command'] = lambda:craft()
        self.f1b9['command'] = lambda:Recruit()
        self.f1b10['command'] = lambda:equip()

        # Gridding Buttons 
        r = 1
        for i in [self.f1b1,self.f1b2,self.f1b3,
              self.f1b4,self.f1b5,self.f1b6,
              self.f1b7,self.f1b8,self.f1b9,
              self.f1b10]:
            i['width'] = 8
            i['height'] = 2
            i.grid(row=r,column=1,ipady=15)
            r+=1

        # Frame2 (Canvas and Label)
        self.f2 = tk.LabelFrame(self.window,relief="ridge")
        self.f2.grid(row=1,column=2,sticky='n'+'s'+'e'+'w')

        # Creating and Gridding Label 
        self.console = tk.Label(self.f2,text="Welcome to Medieval Demon Lord ver 1.0! Check the shell for lore!"
                                ,relief="ridge",height=9,width=76)
        self.console.grid(row=2,column=1,sticky='n'+'s'+'e'+'n',ipady=5)
        #All the Pictures

        self.canvas = tk.Canvas(self.f2,width=680,height=500)
        self.canvas.grid(row=1,column=1)

        self.start = tk.PhotoImage(file = "start.png")
        self.cutting=tk.PhotoImage(file="cutting.png")
        self.mining = tk.PhotoImage(file="mining.png")

        self.background = self.canvas.create_image(340,250,image=self.start)
                    

if __name__ == "__main__":
    main()