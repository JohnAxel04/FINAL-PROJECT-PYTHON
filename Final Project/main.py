import os
from dictionary import *
from floop import *
from ifelif import *
from list import *
from math import *
from print import *
from wloop import *


print(" -------------------------------") 
print("|\t Hello Welcome To\t|")
print("|\t  My FIle System\t|")             #Not belong to the while loop so that, if the user want to go back to menu the welcome something wont show again and will directed to the menu options
print(" -------------------------------")
main = input("Want to proceed(y/n): ").lower()
os.system('cls')

while True:
    
    if main == "y":
        print(f"user input --> {main}")
        print(" -------------------------------")
        print("|\t      MENU\t\t|")
        print(" -------------------------------")
        print(" -------------------------------")
        print("| \to\t\to\t|")
        print("| \t\t\t\t|")
        print("|  P - Print Activity\t\t|")
        print("|  A - Arithmetic Activity\t|")
        print("|  I - If/Else Statement\t|")
        print("|  F - For loop Activity\t|")
        print("|  W - While loop Activity\t|")
        print("|  L - List Activity\t\t|")
        print("| \t\t\t\t|")
        print("|  E - Exit\t\t\t|")
        print(" -------------------------------")
        print("Choose ")
        menu = input("Typing... ").lower()
        os.system('cls')
        if menu == "p":
            print(f"user input --> {menu} = PRINT ACTIVITY")
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity1\t\t|")
            print("|  \t2 - Activity2\t\t|")
            print("|  \t3 - Activity3\t\t|")
            print("|  \t4 - Activity4\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower()
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")
        elif menu == "a":
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity5\t\t|")
            print("|  \t2 - Activity6\t\t|")
            print("|  \t3 - Activity7\t\t|")
            print("|  \t4 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower() 
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")   
        elif menu == "i":
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity5\t\t|")
            print("|  \t2 - Activity6\t\t|")
            print("|  \t3 - Activity7\t\t|")
            print("|  \t4 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------") 
            print("Choose ")
            menus = input("Typing... ").lower() 
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")
        elif menu == "f":
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity5\t\t|")
            print("|  \t2 - Activity6\t\t|")
            print("|  \t3 - Activity7\t\t|")
            print("|  \t4 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower()  
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")
        elif menu == "w":
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity5\t\t|")
            print("|  \t2 - Activity6\t\t|")
            print("|  \t3 - Activity7\t\t|")
            print("|  \t4 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower()
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")
        elif menu == "l":
            print(" -------------------------------")
            print("| \to\t\to\t|")
            print("| \t\t\t\t|")
            print("|  \t1 - Activity5\t\t|")
            print("|  \t2 - Activity6\t\t|")
            print("|  \t3 - Activity7\t\t|")
            print("|  \t4 - Activity8\t\t|")
            print("| \t\t\t\t|")
            print("| \tE - Exit\t\t|")
            print(" -------------------------------")
            print("Choose ")
            menus = input("Typing... ").lower()
            os.system('cls')
            if menus == "e".lower():
                print("Exiting.....")
                print("(E - Exit or C - Continue to Menu)")
                ex = input("Typing... ").lower()
                if ex == "c":
                    continue
                elif ex == "e":
                    print("Thank You For Using my Ai")
                    print("Bye bye")
                    break
                else:
                    print("Error Input.... ")
        elif menu == "e":
            print("Thank You For Using my System")
            print("Bye bye")
            break   
        else:
            print("Unfortunate Not in the Options")  
            print("Try Again")
            continue
    elif main == "n":
        print("Thank you very much")
        break