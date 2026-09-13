import os
from cryptography.fernet import Fernet



def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd=input("What is the master password? ")
key = Fernet.generate_key()
fer = Fernet(key)


def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())
    except FileNotFoundError:
        print("No passwords stored yet. Please add a password first.")
        

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    
    with open ('passwords.txt','a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode()))[2:-1] + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view,add), press q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
    
