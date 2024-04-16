import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Venu")
result = mydb.cursor()
result.execute("use login")
user_detail = input("you are a new user(yes / no) :")
lst = ['yes', "no"]
while True:
    if user_detail.lower() in lst:
        break
    else:
        user_detail = input("you are a new user or not(yes / no).Enter correctly :")
if user_detail.lower() == "yes":
    print("REGISTER YOUR DETAILS ......")
    user_name = input("enter user your name(COMBINATION OF ALPHABETS AND NUMBERS) :")
    while True:
        if any(char.isalpha() for char in user_name) and any(char.isdigit() for char in user_name):
            break
        else:
            user_name = input("user name must contain alphabets and numbers :")
    user_mail = input("enter your mail in the form of username@gmail.com :")
    import re
    pattern = re.compile("[a-zA-Z0-9]{4,}@gmail.com")
    while True:
        if re.fullmatch(pattern, user_mail):
            break
        else:
            user_mail = input("enter your mail in the form of username@gmail.com correctly :")
    user_password = input("enter the password (it must contain A-Z,a-z,0-9,@*_) :")
    while True:
        if (any(i.isalpha() for i in user_password) and any(i.isdigit() for i in user_password)
                and any((i in "@*_") for i in user_password)):
            break
        else:
            user_password = input("password must contain A-Z,a-z,0-9,@*_ enter correctly :")
    try:
        sql = "insert into user (name,mail,password) values (%s,%s,%s)"
        values = (user_name,user_mail,user_password)
        result.execute(sql,values)
        mydb.commit()
        print("You are successfully registered")
    except Exception as e:
        print("An error Occurred : ",e)
else:
    print("LOGIN YOURSELF ........")
    user_name_mail = input("enter your username or mail :")
    while True:
        if user_name_mail:
            break
        else:
            user_name_mail = input("This username or mail field must not be empty :")
    user_password = input("enter the password :")
    while True:
        if user_password:
            break
        else:
            user_password = input("This password field must not be empty :")

    result.execute("select * from user")
    c = result.fetchall()
    if ((user_name_mail in [i[0] for i in c] or user_name_mail in [i[1] for i in c])
            and user_password in [j[2] for j in c]):
        print("Access Granted...")
    else:
        print("Access Denied....")