class user():
    count=0
    def __init__(s,name,gender,salary):
        s.name=name
        s.gender=gender
        s.salary=salary
        user.count+=1
    def  showdetails(s):
           
        print("name:",s.name)
        print("gender:",s.gender)
        print("salary:",s.salary)
        print(f"account no:{s.name[0:3]}1234")
class bank(user):

    def __init__(s,name,gender,salary):
        super().__init__(name,gender,salary)
        s.__balance = 0
      
            
    def  deposite(s,amount):
        s.__balance+=amount
        print(f"{amount} deposited in your account\naccount bal is RS",s.__balance)

    def withdraw(s,amount):
        if(amount>s.__balance):
            print("insufficient balance\nAvailable balance:",s.__balance)
        elif (amount>=100)and (amount<=s.__balance):
            s.__balance=s.__balance-amount
            print(f"{amount} is withdraw from your account\nCurrent balance:",s.__balance,"\nThank you for visiting")
        elif amount<100:
            print(f"you can not withdraw less than 100\nCurrent balance:",s.__balance)
    def viewbalance(s):
        print(s.showdetails())
        print("account balance:",s.__balance)
        

    def transfer(s, amount, user):
        if(amount>s.__balance):
            print("insufficient balance\nAvailable balance:",s.__balance)
        elif (amount>=1 and amount<=s.__balance):
            s.__balance=s.__balance-amount
            print(f"{amount} transfer to {user}")
            print("account balance:",s.__balance)
        elif amount<1:
            print("you can not transfer less then 1\nCurrent balance:",s.__balance)

        
name = input("Enter name :")
gender = input("Enter gender :")
salary = int(input("Enter salary :"))

rbi = bank(name,gender,salary)
print("Welcome to RBI Bank")
rbi.showdetails()
print("Type d for deposite")
print("Type w for withdraw")
print("Type t for transfer")
print("Type v for viewbalance")
print("Type e for exit")

while(True):
    move = input("Enter your move: ")
    if move.lower()=="d":
        amount = int(input("enter amount: "))
        rbi.deposite(amount)
    elif move.lower()=="w":
        amount = int(input("enter amount: "))
        rbi.withdraw(amount)
    elif move.lower()=="t":
        amount = int(input("enter amount: "))
        user = input("Enter name: ")
        rbi.transfer(amount,user)
    elif move.lower()=="v":
        rbi.viewbalance()
    



    
