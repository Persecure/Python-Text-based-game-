#!/usr/bin/env python
import random
import time
from datetime import datetime
class Unit:
    """
    This is class of units used in game: 
    Its attributes are:
    name,experience,rank,health,attack and defence
    function are:
    1) check alive
    2) take_damage
    3) attack_target
    4) increase_experience
    5) display

    """
    def __init__(self, name):
        """
        Initilializing the unit with given name and defalut stats
        """
        self.name = name
        self.experience=0
        self.rank=1
        self.health=100
        self.attack=0 # will base on profession
        self.defence=0 # will base on profession
    def check_alive(self):
        """
        Return True is unit has health greater the 0, else False
        """
        if self.health>0:
            return True
        else:
            return False

    def take_damage(self,damage):
        """
        Decrease health by given damage
        """
        if damage<0:
            pass
        else:
            self.health=self.health-damage

    def attack_target(self,target):
        """
        Return damage points bases on own attack and derget defence
        """
        random_number=random.randint(-5,10)
        damage=self.attack-target.defence+random_number
        return damage
    def increase_exprience(self,exp_points):
        """
        Increase experience by given exp_points. If experience reach 100, rank will increase by one and experience reset by 0.
        Attack and defence will also increase with Rank
        """
        if exp_points<0:
            pass
        else:
            self.experience+=int(exp_points)
        if self.experience>=100:
            self.experience=0
            self.rank+=1
            self.attack+=3
            self.defence+=1
    def display(self):
        """
        Return string of stats of unit
        """
        return self.name+" health="+str(self.health)+" rank = "+str(self.rank)+" atk="+str(self.attack)+" def="+str(self.defence)
        

class Warrior(Unit):
    """
    This is sub class of unit. It Has high Attack satus but moderate or low defence stats
    """
    def __init__(self,name):
        Unit.__init__(self,name)
        self.attack=random.randint(5, 20)
        self.defence=random.randint(1, 10)
    

class Tanker(Unit):
    """
    This is sub class of unit. It Has high Defence satus but moderate or low Attack stats
    """
    def __init__(self,name):
        Unit.__init__(self,name)
        self.attack=random.randint(1, 10)
        self.defence=random.randint(5, 20)


class Player:
    """
    This class is for players of game: human player and AI
    It contain two parameters:
    1) unit: list of units
    2)  coins: coins earned by player during match
    Functions are:
    1) remove_unit
    2) check_defeat
    3) update
    4) earn_coins
    """
    def __init__(self):
        """
        Initilize with default valuse
        """
        self.unit=[]
        self.coins=0

    def remove_unit(self,r_unit):
        """
        Remove unit from list
        """
        new_unit=[]
        for i in self.unit:
            if i.name==r_unit.name:
                pass
            else:
                new_unit.append(i)
        self.unit=new_unit

    def check_defeat(self):
        """
        return True if all the units are dead, else False
        """
        if len(self.unit)==0:
            return True
        else:
            return False

    def update(self,update_unit):
        """
        Update the units of player
        """
        new_unit=[]
        for i in self.unit:
            if i.name==update_unit.name:
                new_unit.append(update_unit)
            new_unit.append(i)

    def earn_coins(self,damage):
        """
        Increase the player coins based on damage done to opposite player
        """
        self.coins+=int(damage/2)
        return int(damage/2)


class Game_Controller:
    """
    This class will control the game play
    Attributes are:
    1) player: A Player class object 
    2) AI: A player class object
    3) Attacker: unit of player / AI
    4) target: unit of player/ AI
    """
    def __init__(self):
        """
        Initilize class of with defalut values
        """
        self.player=Player()
        self.ai=Player()
        self.attacker=None
        self.target=None

    def log(self,file_name,s):
        """
        This function record the log in text file
        """
        file=open(str(file_name+".txt"),'a')
        file.write(s+'\n')
        file.close()

    def player_choice(self,unit):
        """
        This fucntion is use to select targer or attacker of player
        """
        count=1
        while(True):
            for i in unit:
                print("Press ",count,"for ",i.name," health=",i.health," atk=",i.attack," def=",i.defence," rank = ",i.rank," exp=",i.experience)
                count+=1
            try:
                selected=int(input("select= "))
                count=1
                for i in unit:
                    if count==selected:
                        return i
                    count+=1
                else:
                    print("wrong input! please enter carefully")
                    count=1
            except:
                print("Please chose carefully")
                count=1

    def ai_choice(self,unit):
        """
        This function is use to select target or attacker of AI
        """
        choice=random.randint(1,len(unit))
        return unit[choice-1]

    def target_experience(self,damage):
        """
        Calculate the experience of target according to damage taken
        """
        if damage>10:
            exp=self.target.defence+.2*self.target.defence
            return exp
        elif damage<=0:
            exp=self.target.defence+.5*self.target.defence
            return exp
        else:
            return damage

    def set_player(self):
        """
        This function is used to set the player units
        """
        count=1
        while (count<4):
            same_name=False
            print("Select your",count," Unit")
            unit=input("Press w warrior and t for Tanker: ").lower()
            if unit == "w":
                name=input("Enter name of unit: ")
                for i in self.player.unit:
                    if i.name==name:
                        print("This Name already exist! choose another name")
                        same_name=True
                if same_name:
                    continue
                self.player.unit.append(Warrior(name))
                count+=1
            elif unit == "t":
                name=input("Enter name of unit: ")
                for i in self.player.unit:
                    if i.name==name:
                        print("This Name already exist! choose another name")
                        same_name=True
                if same_name:
                    continue
                self.player.unit.append(Tanker(name))
                count+=1
            else:
                print("Wrong Input! select carefully")
    def set_ai(self):
        """
        This function is used to set the AI units
        """
        count=1
        while (count<4):
            same_name=False
            
            AI_Number=random.randint(10,99)
            AI_Name="AI"+str(AI_Number)
            for i in self.ai.unit:
                if AI_Name==i.name:
                    same_name=True
            if same_name:
                continue
            AI_Profession=random.randint(1,2)
            if AI_Profession==1:
                self.ai.unit.append(Warrior(AI_Name))
                count+=1
            else:
                self.ai.unit.append(Tanker(AI_Name))
                count+=1

    def game_setup(self):
        """
        This function is responsibe for game play
        """
        now = datetime.now()
        # file name for each game play : based on time and date 
        file_name = now.strftime("%d_%m_%Y_%H-%M-%S")
        self.log(file_name,"------New Game ------\n")
        game_log="Game started on "+str(time.ctime())
        
        
        self.log(file_name,game_log)
        self.set_player()
        self.log(file_name,"Player Team")
        for i in self.player.unit:
            self.log(file_name,i.display())
        self.set_ai()
        self.log(file_name,"AI Team")
        for i in self.ai.unit:
            self.log(file_name,i.display())
        turn=random.randint(1,2)
        while(not self.player.check_defeat() and not self.ai.check_defeat()):
            if turn==1:
                print("----------------Player Turn--------------------")
                print("                Player coins=",str(self.player.coins))
                print("Choose Your Attacker")
                self.attacker=self.player_choice(self.player.unit)
                self.log(file_name,"Player choose Attacker :"+self.attacker.name)
                print()
                print("Choose Your Traget")
                self.target=self.player_choice(self.ai.unit)
                self.log(file_name,"Player choose Target :"+self.target.name)
                print()
                damage=self.attacker.attack_target(self.target)
                self.target.take_damage(damage)
                if damage<0:
                    damage=0
                coins=self.player.earn_coins(damage)
                game_message="[Game Message] "+self.attacker.name +" attack "+self.target.name+" with damage "+str(damage)+":+"+str(damage)+"EXP"+ " Coins earns :"+str(coins)
                print(game_message)
                self.log(file_name,game_message)
                self.attacker.increase_exprience(damage)
                self.target.increase_exprience(self.target_experience(damage))
                self.player.update(self.attacker)
                if self.target.check_alive():
                    self.ai.update(self.target)
                else:
                    self.ai.remove_unit(self.target)
                    print("\n",self.target.name+" is dead")
                    self.log(file_name,self.target.name+" is dead")
                    
                turn=2

                print()
                self.log(file_name,"Player Coins :"+str(self.player.coins))
            else:
                print("----------------AI TURN--------------------")
                print("        AI coins=",str(self.ai.coins))
                self.attacker=self.ai_choice(self.ai.unit)
                print("AI Attacker = ",end="")
                print(self.attacker.display())
                self.log(file_name,"AI choose Attacker :"+self.attacker.name)
                print()
                self.target=self.ai_choice(self.player.unit)
                print("AI Traget = ",end="")
                print(self.target.display())
                self.log(file_name,"AI choose Target :"+self.attacker.name)
                print()
                damage=self.attacker.attack_target(self.target)
                self.target.take_damage(damage)
                if damage<0:
                    damage=0
                self.attacker.increase_exprience(damage)
                coins=self.ai.earn_coins(damage)
                game_message="[Game Message] "+self.attacker.name +" attack "+self.target.name+" with damage "+str(damage)+":+"+str(damage)+"EXP"+ " Coins earns :"+str(coins)
                print(game_message)
                self.log(file_name,game_message)
                self.target.increase_exprience(self.target_experience(damage))
                self.ai.update(self.attacker)
                if self.target.check_alive():
                    self.player.update(self.target)
                else:
                    self.player.remove_unit(self.target)
                    print("\n",self.target.name+" is dead")
                    self.log(file_name,self.target.name+" is dead")
                turn=1
                print()
                self.log(file_name,"AI Coins: "+str(self.ai.coins))
        if self.player.check_defeat():
            print("AH! YOU LOSE ...")
            self.log(file_name,"AI WON THE BATTLE")
        else:
            print("congratulations! You Won The Battle")
            self.log(file_name,"You Won the Battle")
        self.log(file_name,"Game End on "+ time.ctime())

def main():
    """
    Main function for menu
    """
    while(True):
        print("-------MENU---------")
        print("Press 1 to play game")
        print("Press 0 to exit")
        choice=input("Input: ")
        if choice=="1":
            game=Game_Controller()
            game.game_setup()
        elif choice=="0":
            print("EXITING GAME...")
            break
        else:
            print("Wrong input! please enter carefully")


if __name__==main():
    main()
