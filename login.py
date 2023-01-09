# KAMORI KAREN
# 10/01/2023

# Registration and login program
# information is stored in and retrieved from a csv file 
import os
import re
import csv
import time
import sys

def main():
    print("*****MENU*****")
    print("1). REGISTRATION")
    print("2). LOGIN")
    print("3). EXIT")
    choice = int(input("Choice: "))

    # match case
    match choice:
        case 1:
            registration()
        case 2:
            login()
        case 3:
            end()
            sys.exit()

def registration():
    end()
    print("*********REGISTRATION*********")
    # user input
    firstname = input("First Name: ").title()
    secondname = input("Second Name: ").title()
    surname = input("Surname: ").title()
    email = email_validation()
    password = password_validation()

    fields = ["firstname","secondname","surname","email","password"]
    row = {"firstname":firstname, "secondname":secondname,"surname":surname,"email":email,"password":password}

    # writing to an existing csv file
    if os.path.isfile("customers.csv"):
        with open("customers.csv", "a", newline="") as file:
            writer = csv.DictWriter(file,fieldnames= fields)
            writer.writerow(row)
    else:
        # writing to a csv file for the first time
        with open("customers.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerow(row)

def login():
    end()
    print("********LOGIN********")
    user_email = input("Email: ")
    user_password = input("Password: ")

    customers = []

    # Reading from a csv file and appending data to a list
    with open("customers.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append({"email":row["email"], "password":row["password"]})
    
    # sorting a list of dictionaries by email
    for customer in sorted(customers, key=lambda customer:customer["email"]):
        if user_email==customer["email"] and user_password==customer["password"]:
            print("**************************")
            print("SHOP FROM ITEMS BELOW")
        else:
            print("WRONG EMAIL OR PASSWORD!!!!!!\n")
            main()

def end():
    time.sleep(1)
    os.system("cls")

def email_validation():
    email = input("Email: ")

    # regular expressions to ensure correct email format entry
    if re.search("^\w+@(\w+\.)?\w+\.(edu|com|org|net|gov)$", email):
        return email
    else:
        email_validation() # recursion if user entry is incorrect 

def password_validation():
    password = input("Enter password: ")
    passwrd = input("Confirm password: ")
    if password == passwrd:
        return password
    else:
        print("incorrect password")
        password_validation() # Recursion

if __name__ == "__main__":
    main()