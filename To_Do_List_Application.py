import mysql.connector as mc
import prettytable

mydb = mc.connect(host="localhost", user="root", passwd="*************")
cursor = mydb.cursor()
cursor.execute("use to_do_list")
# Main problems in the code
# 1.sql injection vulnerability
# 2. Better to use user-friendly interface
# 3.do not show the passwords directly on the screen like above
# 4. it is Better to use slightly more error handling mechanisms in this code
# 5.Try to reduce code repetition which reduces efficiency
def user_detail_validation(x: str):
    a = ["yes", "no"]
    while True:
        if x.lower() in a:
            return x.lower()
        else:
            x = (input("Are you a new user (yes/no).Enter correctly :"))
# taking user_name from the user
def user_name(x: str):
    cursor.execute("select name from user")
    a = cursor.fetchall()
    b = [i[0] for i in a]
    while True:
        if x:
            if x not in b:
                return x
            else:
                print("the username you entered is already registered")
                x = input("enter a unique username for yourself :")
        else:
            x = input("enter the username correctly :")
def user_login():
    while True:
        user_name1 = input("enter your username :")
        while True:
            if user_name1:
                break
            else:
                user_name1 = input("This username field must not be empty :")
        user_password1 = input("enter the password :")
        while True:
            if user_password1:
                break
            else:
                user_password1 = input("This password field must not be empty :")
        cursor.execute("select name,password from user")
        c = cursor.fetchall()
        if user_name1 in [i[0] for i in c] and user_password1 in [j[1] for j in c]:
            print("Access Granted...")
            break
        else:
            print("Access Denied.Try again....")
    cursor.execute(f"select * from {user_name1}")
    a = cursor.fetchall()
    b = [i[0] for i in cursor.description]
    table = prettytable.PrettyTable(b)
    for i in a:
        table.add_row(i)
    print(table)
    while True:
        user = input("Do you want to edit the to do list (yes/no) :")
        while user.lower() not in ["yes","no"]:
            user = input("Do you want to edit the to do list (yes/no) :")
        if user.lower() == "yes":
            while True:
                print("Select one option from below")
                print("1.Add_Task\n2.Delete_Task\n3.Update_Task")
                user_choice = input("Option :- ")
                while True:
                    if user_choice in["1","2","3"]:
                        break
                    else:
                        user_choice = input("enter the option correctly :")
                if user_choice == "1":
                    task_name = input("enter the task name :")
                    while True:
                        if task_name:
                            break
                        else:
                            task_name = input("enter the task name correctly")
                    cursor.execute(f"insert into {user_name1} (task_name,status) values ('{task_name}','pending')")
                    mydb.commit()
                    cursor.execute(f"select * from {user_name1}")
                    a = cursor.fetchall()
                    b = [i[0] for i in cursor.description]
                    table = prettytable.PrettyTable(b)
                    for i in a:
                        table.add_row(i)
                    print(table)
                elif user_choice == "2":
                    task_id = input("Enter the task_id of the row you want to delete :")
                    while True:
                        if task_id.isdigit():
                            break
                        else:
                            task_id = input("Enter the task_id correctly of the row you want to delete :")

                    cursor.execute(f"delete from {user_name1} where task_id = '{task_id}'")
                    cursor.execute(f"select * from {user_name1}")
                    a = cursor.fetchall()
                    b = [i[0] for i in cursor.description]
                    table = prettytable.PrettyTable(b)
                    for i in a:
                        table.add_row(i)
                    print(table)
                else:
                    print("1.task_name\n2.task_status")
                    update = input("select an option from the above :")
                    while update not in ["1","2"]:
                        update = input("select an option correctly from the above :")
                    if update == "1":
                        new_task_name = input("enter the new task name  ")
                        while not new_task_name:
                            new_task_name = input("enter the new task name it must not be empty :")
                        cursor.execute(f"select task_id from {user_name1}")
                        new_task_id = input("Enter the corresponding task_id :")
                        z = cursor.fetchall()
                        while True:
                            if new_task_id:
                                if new_task_id in [i[0] for i in z]:
                                    break
                                else:
                                    new_task_id = input("Enter the valid corresponding task_id :")
                            else:
                                new_task_id = input("Enter the corresponding task_id correctly :")
                        cursor.execute(f"update task_name from {user_name1} where task_id={new_task_id}")
                        mydb.commit()
                        cursor.execute(f"select * from {user_name1}")
                        a = cursor.fetchall()
                        b = [i[0] for i in cursor.description]
                        table = prettytable.PrettyTable(b)
                        for i in a:
                            table.add_row(i)
                        print(table)
                    elif update == "2":
                        new_task_id = int(input("Enter the corresponding task_id to update status :"))
                        cursor.execute(f"select task_id from {user_name1}")
                        z = cursor.fetchall()
                        print(type(new_task_id))
                        print([type(i[0]) for i in z])
                        while True:
                            if new_task_id:
                                if new_task_id in [i[0] for i in z]:
                                    break
                                else:
                                    new_task_id = input("Enter the valid corresponding task_id :")
                            else:
                                new_task_id = input("Enter the corresponding task_id to update status :")
                        cursor.execute(f"update {user_name1} set status='completed' where task_id = {new_task_id}")
                        mydb.commit()
                        cursor.execute(f"select * from {user_name1}")
                        a = cursor.fetchall()
                        b = [i[0] for i in cursor.description]
                        table = prettytable.PrettyTable(b)
                        for i in a:
                            table.add_row(i)
                        print(table)

        else:
            break
def user_mail(x:str):
    import re
    pattern = re.compile("[a-zA-Z0-9]{5,}@gmail.com")
    cursor.execute("select mail from user")
    a = cursor.fetchall()
    b = [i[0] for i in a]
    while True:
        gmail = re.fullmatch(pattern, x)
        if gmail:
            if gmail.group() not in b:
                return gmail.group()
            else:
                print("the mail you entered is already registered")
                x = input("enter another mail for yourself :")
        else:
            x = input("enter the user mail in the form of example@gmail.com and the length needs to be greater than 5 :")
def user_password(password:str):
    while True:
        if (any(i.isalpha() for i in password) and any(i.isdigit() for i in password)
                and any((i in "@*_") for i in password)):
            return password
        else:
            password = input("password must contain A-Z,a-z,0-9,@*_ enter correctly :")


detail = user_detail_validation(input("Are you a new user (yes/no) :"))
if detail == "yes":
    name = user_name(input("enter the user name :"))
    mail = user_mail(input("Enter the mail in the form of example@gmail.com"))
    passwd = user_password(input("enter the password (it must contain A-Z,a-z,0-9,@*_) :"))
    sql = "insert into user (name,mail,password) values (%s,%s,%s)"
    values = (name,mail,passwd)
    cursor.execute(sql,values)
    sql1 = f"create table {name} (task_id int AUTO_INCREMENT PRIMARY KEY,task_name varchar(50),status varchar(50))"
    cursor.execute(sql1)
    mydb.commit()
    print("You are successfully registered.")
else:
    user_login()