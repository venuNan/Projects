import mysql.connector
import hashlib


try:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="Venu", database="login")
    result = mydb.cursor()
except mysql.connector.Error as err:
    print("Error connecting to MySQL:", err)
    exit()

def register_user():
    print("REGISTER YOUR DETAILS ......")
    user_name = input("Enter your name (combination of alphabets and numbers): ")
    while True:
        if any(char.isalpha() for char in user_name) and any(char.isdigit() for char in user_name):
            break
        else:
            user_name = input("User name must contain alphabets and numbers: ")

    user_mail = input("Enter your email in the form of username@gmail.com: ")
    while True:
        if "@" in user_mail and user_mail.endswith("@gmail.com"):
            break
        else:
            user_mail = input("Enter your email correctly in the form of username@gmail.com: ")

    user_password = input("Enter the password (it must contain A-Z, a-z, 0-9, @*_: ")
    while True:
        if any(i.isalpha() for i in user_password) and \
           any(i.isdigit() for i in user_password) and \
           any(i in "@*_" for i in user_password):
            break
        else:
            user_password = input("Password must contain A-Z, a-z, 0-9, @*_: ")

    hashed_password = hashlib.sha256(user_password.encode()).hexdigest()

    try:
        sql = "INSERT INTO user (name, mail, password) VALUES (%s, %s, %s)"
        values = (user_name, user_mail, hashed_password)
        result.execute(sql, values)
        mydb.commit()
        print("You are successfully registered")
    except Exception as e:
        print("An error occurred:", e)


def login_user():
    print("LOGIN YOURSELF ........")
    user_name_mail = input("Enter your username or email: ")
    while True:
        if user_name_mail:
            break
        else:
            user_name_mail = input("This username or email field must not be empty: ")

    user_password = input("Enter the password: ")
    while True:
        if user_password:
            break
        else:
            user_password = input("This password field must not be empty: ")


    hashed_password = hashlib.sha256(user_password.encode()).hexdigest()

    result.execute("SELECT * FROM user")
    users = result.fetchall()

    if any(user_name_mail in user for user in users) and any(hashed_password in user for user in users):
        print("Access Granted...")
    else:
        print("Access Denied....")

if __name__ == "__main__":
    user_detail = input("Are you a new user? (yes/no): ").lower()
    while user_detail not in ['yes', 'no']:
        user_detail = input("Please enter 'yes' or 'no': ").lower()

    if user_detail == "yes":
        register_user()
    else:
        login_user()
