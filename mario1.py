class charc():
    def __init__(self,name):
        self.name=name
        self.__life=3
        self.__score=0

    def kicked(self):
        self.__score+=10

    def punched(self):
        self.__score+=5

    def stabbed(self):
        self.__life-=1

    def displaylife(self):
        return self.__life

    def displayscore(self):
        return self.__score

    def intro(self):
        Print(f"name:{s.name}\nlife:{s.__life}\n:{s.__score}")
     
name=input("enter your name: ").title()
print(f"hii{name}\nwelcome to mario")
mario=charc(name)

print("k: for kicked\np:for punched\ns:for stabbed\nE:for Exit")

while(True):
    
    press=input("enter your move: ")
    if(press=="k"):
        mario.kicked()
        print("new score",mario.displayscore())
    elif(press=="p"):
        mario.punched()
        print("new score",mario.displayscore())
    elif(press=="s"):
        count=mario.displaylife()
        mario.stabbed()
        print("life remaining:",mario.displaylife())
        if  count>1:
            continue
        else:
            print("game over")
            break

    elif(press=="e"):
        a=input("want to quit?,(y/n)")
        if(a=="y"):
            break
        elif(a=="n"):
            continue
        else:
            print("invalid")
                
