import sys
import random
import os
import time

print("Welcome To AnDRE Finance Bank\n1 Staff Login\n2 Close App")

def check():
    username = input("\nType In Your username : ")
    password = input("Type In Your password : ")

    flist = []
    file = open("staff.txt","r")
    fh = file.readlines()
    for line in fh:
        listI = (line.split(','))
        flist.append(listI)
    checkUSer(flist, username, password)

    file.close()

def checkUSer(arr, user , passwd):
    i = 0
    while i < len(arr):
        if arr[i][0] == user and arr[i][1] == passwd:
            return staffPAge()
        i+=1
    print("\nUser does not exist")


def menu():
    try:
        select = int(input("Select 1 or 2:  "))
        while True:
            if select == 1:
                check()
            elif select == 2:
                print("Thank You for Banking With Us.")
                sys.exit()
            elif select != 1 and select != 2:
                print("Invalid Selection")
    except ValueError:
        print("Invallid Entry\nTry Again")

def createsessionfile():
    with open("session.txt",'a+') as file:
        data = file.write("Session created in : " + time.asctime(time.localtime(time.time())))

def delsessionfile():
    if os.path.exists("session.txt"):
        os.remove("session.txt")
        print("File deleted")
    else:
        print("The file does not exist")

def staffPAge():
    createsessionfile()
    try:
        while True:
            print("\n1 Create new bank account\n2 Check Account Details\n3 Logout")
            selection = int(input('Enter Selection 1, 2 or 3 :  '))
            if selection == 1:
                createBankAcc()
            elif selection == 2:
                AccountDetails()
            elif selection == 3:
                delsessionfile()
                menu()
    except ValueError:
        print('Invalid Selection Try Again\n')


def writeMultipleToFileWithContent(filename, data):
    with open(filename, mode='a') as fh:
        fh.writelines(data)

def createBankAcc():
    filename2 = "customer.txt"
    print("Fill In The Right Details To Create New Account ")
    Account_name = input("Account name = ")
    Opening_Balance = input("Opening Balance = ")
    Account_Type = input("Account Type = ")
    Account_email = input("Account email = ")
    Numbers = '0123456789'
    mixin = "" .join(random.choice(Numbers.upper())for x in range(10))
    Account_Number = mixin
    print("YOUR ACCOUNT NUMBER IS :  " + Account_Number)
    data1 = [Account_name + ',',
             Opening_Balance + ',',
             Account_Type + ',',
             Account_email + ',',
             Account_Number + ',' + '\r']
    writeMultipleToFileWithContent(filename2, data1)



def AccountDetails():
    flist = []
    account_num = input("Account Number : ")
    file = open("customer.txt","r")
    file = file.readlines()
    for line in file:
        listl = line.split(',')
        flist.append(listl)
    print(checkArray1(flist, account_num))

def checkArray1(arr, account):
    i = 0
    while i < len(arr):
        if arr[i][4] == account:
            # print(i)
            return arr[i]
        i+=1
    return "Does not exist";

menu()