import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="123456", database="itvdb")
cursor=con.cursor()
while True:
    I=int(input("1->Enter more employee details\n2->No\nEnter Choice : "))
    if I==2:
          break
    Id=int(input("Enter employee Id: "))
    name=input("Enter employee name: ")
    salary=float(input("Enter employee salary: "))
    age=int(input("Enter employee age: "))
    gender=input("Enter employee gender: ")
    city=input("Enter employee city: ")
    query="Insert into emp values({},'{}',{},{},'{}','{}')".format(Id,name,salary,age,gender,city)
    cursor.execute(query)
    con.commit()
    print("Data Inserted successfully..")

while True:
    U=int(input("3->Enter more to update\n4->No\nEnter Choice: "))
    if U==4:
        break        
    Id=int(input("Enter employee id: "))
    salary=float(input("Enter new salary: "))
    age=int(input("Enter new age: "))
    query="update emp set salary={},age={} where id={}".format(salary,age,Id)
    
    cursor.execute(query)
    con.commit()
    if cursor.rowcount>0:
        print("Data updated successfully...")
    else:
        print("No data found..")

while True:
    D=int(input("5->Enter employee id to delete \n6->No\nEnter choice: "))
    if D==6:
        break
    Id=int(input("Enter employee id to delete: "))
    query="delete from emp where id={}".format(Id)
    cursor.execute(query)
    con.commit()
    if cursor.rowcount>0:
        print("Deletion successfull...")
    else:
        print("No data found..")

while True:
    R=int(input("7->enter emp id to see record\n8->to see all employee records\n9->exit\nEnter choice: "))
    if R==7:
        Id=int(input("Enter employee id to see record:" ))
        query="select * from emp"
        cursor.execute(query)
        data=cursor.fetchone()
        print(data)
        
    elif R==8:
        query="select * from emp"
        cursor.execute(query)
        data=cursor.fetchall()
        print(data)
        print("Total Number of records=",cursor.rowcount)
    elif R==9:
        break
    else:
        print("No data found")
    


    
                                                        
