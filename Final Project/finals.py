import os #to use the cls command
import time #to add some delay in showing some data
from dictionary import *
from floop import *
from ifelif import *
from list import *
from art import * #different file for every topic
from print import *
from deff import *
from ccode import *
from fnction import *

lagayan = {'a1': Activity1,'a2':Activity2,'a3': Activity3,'a4':Activity4,'a5': activity5,'a6':Activity6,'a7': Activity7,'a8':Activity8,'a9': Activity9,'a10':Activity10,'a11': Activity11,'a12':Activity12,'a13': Activity13,'a14':Activity14,'a15': Activity15,'a16':Activity16,'a17': Activity17,'a18':Activity18,'a19': Activity19,'a20':Activity20,'a22':Activity22,'a23': Activity23,'a21': Activity21,'a24': act24,'a25': Activity25,'a26': Activity26,'a27': Activity27,'a28': Activity28,'c1':cchal1,'c2':cchal2,'c3':cchal3,'c4':cchal4,'c5':cchal5,'c6':cchal6,'c7':cchal7,'c8':cchal8,'c9':cchal9,'c10':cchal10,'c11':cchal11,'c12':cchal12,'c13':cchal13,'c14':cchal14,'c15':cchal15,'c16':cchal16}#The list for the Search section so that its easy to locate files compare using if/else statement  

a2 = ("Q.System: Hi There🖐")
for text in a2:
    print(text,end="", flush=True)
    time.sleep(.03)
time.sleep(1)
a3 =("\nQ.System: WELCOME TO MY SYSTEM")
for text in a3:
    print(text,end="", flush=True)
    time.sleep(.03)
time.sleep(1)
a4 =("\nQ.System: Whats your Name: ")
for text in a4:
    print(text,end="", flush=True)
    time.sleep(.03)
time.sleep(1)
nn = input("\nUser1: typing... ").upper()
time.sleep(1.2)
os.system('cls')
a5 = (f"WELCOME TO THE Q.SYSTEM {nn}\n") #Introduction
for text in a5:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(1.2)
a6 = ("\nLoading System...")
for text in a6:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(1.2)
os.system('cls')
a1 = ("...")
for text in a1:
    print(text, flush=True)
    time.sleep(1)
time.sleep(.3)
os.system('cls')
print("<>--------------------------------------------------------<>") 
time.sleep(.1)
print("||                WELCOME TO Q.SYSTEM                     ||")
time.sleep(.1)
print("<>--------------------------------------------------------<>")             #Not belong to the while loop so that, if the user want to go back to menu the welcome something wont show again and will directed to the menu options
time.sleep(.2)
while True:
    a6 = ("\nQ.System: Want to proceed(y/n): ")
    for text in a6:
        print(text,end="", flush=True)
        time.sleep(.03)
    time.sleep(.1)
    main = input(f"\n{nn}: Typing.... ").lower()

    if main == "y":
        os.system('cls')
        time.sleep(1.2)
        a7 = ("Loading Menu Options....\n")
        for text in a7:
            print(text,end="", flush=True)
            time.sleep(.03)
        time.sleep(1.2)
        os.system('cls')
        
        a1 = ("...")
        for text in a1:
            print(text, flush=True)
            time.sleep(1)
        time.sleep(1.2)
        os.system('cls')
        print("┌────────────────────────────────────────────────────────────────────┐")
        time.sleep(.1)
        print("│                                MENU                                │")
        time.sleep(.1)
        print("│────────────────────────────────────────────────────────────────────│")
        time.sleep(.1)
        print("│   1 - Print Statement                                              │")
        time.sleep(.1)
        print("│   2 - Variables                                                    │")
        time.sleep(.1)
        print("│   3 - Operators                                                    │")
        time.sleep(.1)
        print("│   4 - Conditional Statement                                        │")
        time.sleep(.1)
        print("│   5 - Looping (For / While)                                        │")
        time.sleep(.1)
        print("│   6 - List / Dictionary                                            │")
        time.sleep(.1)
        print("│   7 - Function                                                     │")
        time.sleep(.1)
        print("│   8 - Code Challenge and Activity                                  │")
        time.sleep(.1)
        print("│   9 - Search Section                                               │")
        time.sleep(.1)
        print("│                                                                    │")
        time.sleep(.1)
        print("│   0 - Exit                                                         │")
        print("└────────────────────────────────────────────────────────────────────┘")
        time.sleep(.7)
        l1 = (f"  Q.System: Hello {nn} this is my MAIN MENU, where you\n  can find some topics for learning python. \n")
        for text in l1:
            print(text,end="", flush=True)
            time.sleep(.03)
        time.sleep(.2)
        l2 = (f"\n  Q.System: Choose among the options: ")
        for text in l2:
            print(text,end="", flush=True)
            time.sleep(.03)
        menu = input(f"\n  {nn}: Typing... ").lower()
        os.system('cls')
        time.sleep(2)
        def codelist():
            while True:
                os.system('cls')
                time.sleep(1)
                l1 = ("Code Challenge\n")
                for text in l1:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(1)    
                print("\n┌───────────────────────────────────────────────┐ ┌───────────────────────────────────────────────┐")
                time.sleep(.1)
                print("│            Code Challenge(1-8)                │ │            Code Challenge(1-8)                │")
                time.sleep(.1)
                print("│───────────────────────────────────────────────│ │───────────────────────────────────────────────│ ")
                time.sleep(.1)
                print("│                                               │ │                                               │")
                time.sleep(.1)
                print("│    C1 -  Name at the middle of triangle       │ │    C9 -  Countdown Simulator(For Loop)        │")
                time.sleep(.1)
                print("│    C2 -  Money Withdraw Bill Counter          │ │    C10 -  Pyramid(Nested For loop)            │")
                time.sleep(.1)
                print("│    C3 -  Login(Email & Password)              │ │    C11 -  (Nested For loop)                   │")
                time.sleep(.1) 
                print("│    C4 -  Number Checker(Odd or Even)          │ │    C12 -  Triangle Numbers(Nested For loop)   │")
                time.sleep(.1)
                print("│    C5 -  Anime Library(anime recommendation)  │ │    C13 -  Christmas Tree(Nested For loop)     │")
                time.sleep(.1)
                print("│    C6 -  Factorial(For Loop)                  │ │    C14 -  Odd Calculator(While Loop)          │")
                time.sleep(.1)
                print("│    C7 -  Odd Counter(For Loop)                │ │    C15 -  Anime List(List & While Loop)       │")
                time.sleep(.1)
                print("│    C8 -  Multiplication Table(For Loop)       │ │    C16 -  Student Information(Functions)      │")
                time.sleep(.1)
                print("│                                               │ │                                               │")
                time.sleep(.1)
                print("│    S -  Search      N - Next(Activities)      │ │    E - Exit                                   │")
                time.sleep(.1)
                print("└───────────────────────────────────────────────┘ └───────────────────────────────────────────────┘")   
                time.sleep(1)
                lba = ("\nQ.System: Enter your choice: ")
                for text in lba:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                menu = input(f"\nTyping... ").lower()
                time.sleep(1)
                if menu == "e".lower():
                    l16= ("Q.System: Going back to Menu...")
                    for text in l16:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    os.system('cls')
                    break
                if menu == "s".lower():
                    rhs()
                    break
                elif menu == "n":
                    while True:
                        os.system('cls')
                        time.sleep(1)
                        l1 = ("Code Activity\n")
                        for text in l1:
                            print(text,end="", flush=True)
                            time.sleep(.03) 
                        print("\n ┌──────────────────────────────────┐ ┌──────────────────────────────────┐ ┌──────────────────────────────────┐ ┌──────────────────────────────────┐")
                        time.sleep(.1)
                        print(" │           Activity1-7            │ │          Activity8-14            │ │          Activity15-21           │ │          Activity22-28           │")
                        time.sleep(.1)
                        print(" │──────────────────────────────────│ │──────────────────────────────────│ │──────────────────────────────────│ │──────────────────────────────────│")
                        time.sleep(.1)
                        print(" │                                  │ │                                  │ │                                  │ │                                  │")
                        time.sleep(.1)
                        print(" │         a1 - Activity1           │ │         a8 - Activity8           │ │         a15 - Activity15         │ │         a22 - Activity22         │")
                        time.sleep(.1)
                        print(" │         a2 - Activity2           │ │         a9 - Activity9           │ │         a16 - Activity16         │ │         a23 - Activity23         │")
                        time.sleep(.1)
                        print(" │         a3 - Activity3           │ │         a10 - Activity10         │ │         a17 - Activity17         │ │         a24 - Activity24         │")
                        time.sleep(.1) 
                        print(" │         a4 - Activity4           │ │         a11 - Activity11         │ │         a18 - Activity18         │ │         a25 - Activity25         │")
                        time.sleep(.1)
                        print(" │         a5 - Activity5           │ │         a12 - Activity12         │ │         a19 - Activity19         │ │         a26 - Activity26         │")
                        time.sleep(.1)
                        print(" │         a6 - Activity6           │ │         a13 - Activity13         │ │         a20 - Activity20         │ │         a27 - Activity27         │")
                        time.sleep(.1)
                        print(" │         a7 - Activity1           │ │         a14 - Activity14         │ │         a21 - Activity21         │ │         a28 - Activity28         │")
                        time.sleep(.1)
                        print(" │                                  │ │                                  │ │                                  │ │                                  │")
                        time.sleep(.1)
                        print(" │         S - Search               │ │         C - Code Challenge       │ │                                  │ │                                  │")
                        time.sleep(.1)
                        print(" └──────────────────────────────────┘ └──────────────────────────────────┘ └──────────────────────────────────┘ └──────────────────────────────────┘")
                        lb9 = ("Q.System: Enter your choice(s/c): ").lower()
                        for text in lb9:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        menu = input(f"\nTyping... ").lower()
                        time.sleep(1)
                        if menu == "s".lower():
                            rhs()  
                            break
                        elif menu == "c":
                            l1 = ("Q.System: Going back to Code challenge...")
                            for text in l1:
                                print(text,end="", flush=True)
                                time.sleep(.2)
                            time.sleep(1) 
                            os.system('cls')
                            break
                        else:
                            l16 = ("Q.System: Unfortunate Not in the Options")
                            for text in l16:
                                print(text,end="", flush=True)
                                time.sleep(.03) 
                            time.sleep(0.2)
                            os.system('cls')
                            continue 
                elif menu == "e":
                        l1 = ("Q.System: Going back to Main Menu")
                        for text in l1:
                                print(text,end="", flush=True)
                                time.sleep(.2)
                        time.sleep(1) 
                        os.system('cls')
                        break
                else:
                    l16 = ("Q.System: Unfortunate Not in the Options")
                    for text in l16:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    os.system('cls')
                    continue 
        def rhs():
            while True: 
                l1 = ("WELCOME TO SEARCH SECTION\n")
                for text in l1:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1)
                l92 = ("\nQ.System: Key of the Activity(L - Code Challenge List E-Exit): ")
                for text in l92:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(.2)
                srch = input(f"\n Typing... ").lower()
                time.sleep(1)
                if srch in lagayan.keys():
                    l1 = ("Record Found")
                    for text in l1:
                        print(text,end="", flush=True)
                        time.sleep(.03)
                    time.sleep(1)
                    print("\n--------------------------\n")
                    time.sleep(.1)
                    lagayan[srch]() 
                    time.sleep(.1)   
                    print("\n--------------------------\n")
                    time.sleep(.1)
                    l2 = ("Q.System: Search Again(y/n)? ")
                    for text in l2:
                        print(text,end="", flush=True)
                        time.sleep(.03)
                    time.sleep(.2)
                    sq = input(f"\nTyping... ").lower()
                    os.system('cls')
                    if sq == "y":
                        l1 = ("Q.System: Repeating... ")
                        for text in l1:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(1)
                        os.system('cls')
                        continue
                    elif sq == "n":
                        l14 = ("Q.System: Going back to Main Menu")
                        for text in l14:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(0.1)
                        l15 = ("...")    
                        for text in l15:
                            print(text,end="", flush=True)
                            time.sleep(.03) 
                        time.sleep(0.2)
                        return
                    else:
                        l16 = ("\nQ.System: Unfortunate Info not Found")
                        for text in l16:
                            print(text,end="", flush=True)
                            time.sleep(.03) 
                        time.sleep(0.2)
                        os.system('cls')
                        continue  
                elif srch == "l":
                    l1 = ("\nGoing to the List")
                    for text in l1:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    os.system('cls')
                    codelist()
                    break
                elif srch == "e":
                    l1 = ("Q.System: Going back to Main Menu")
                    for text in l1:
                            print(text,end="", flush=True)
                            time.sleep(.02)
                    time.sleep(1) 
                    os.system('cls')
                    return
                else:
                    l99 = ("\nQ.System: Unfortunate Info not Found")
                    for text in l99:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    os.system('cls')
                    continue 
        if menu == "1": #print
            while True:
                time.sleep(1)
                l5 = ("Print Statement\n")
                for text in l5:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1)
                l3 = ("\nA print statement is a command used to display text or the value of variables on the screen.")
                for text in l3:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1.2)
                l4 = ("\nIt is how Python outputs information to the user\n")
                for text in l4:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(.2)
                l01 = ("\nQ.System: Want to see some Examples(Y - YES/N - NO)? ")
                for text in l01:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(0.2)
                bago = input(f"\n{nn} Typing... ").lower()
                if bago == "y":
                    while True:
                        os.system('cls')
                        a7 = ("Loading Activity Examples....\n")
                        for text in a7:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(1.2)
                        os.system('cls')
                        
                        a1 = ("...")
                        for text in a1:
                            print(text, flush=True)
                            time.sleep(1)
                        time.sleep(1.2)
                        os.system('cls')
                        print("┌──────────────────────────────────────────────────────────┐")
                        time.sleep(.1)
                        print("│                   Print Statement                        │")
                        time.sleep(.1)
                        print("│──────────────────────────────────────────────────────────│")
                        time.sleep(.1)
                        print("│   1 - Simple Printing                                    │")
                        time.sleep(.1)
                        print("│   2 - Ask for Your Name                                  │")
                        time.sleep(.1)
                        print("│   3 - Name Counter                                       │")
                        time.sleep(.1)
                        print("│   4 - Type of Input                                      │")
                        time.sleep(.1)
                        print("│   E - Exit                                               │")
                        time.sleep(.1)
                        print("└──────────────────────────────────────────────────────────┘")
                        la3 = ("\nQ.System: Enter your choice: ")
                        for text in la3:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        menu = input(f"\n{nn} Typing... ").lower()
                        time.sleep(1)
                        os.system('cls')
                        
                        if menu == "e".lower():
                            l12 = ("\nQ.System: Exiting.....")
                            for text in l12:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            for text in l12:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            l13 = ("\nQ.System: (D - Description or C - Continue )")
                            for text in l13:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            ex = input(f"\n{nn}: Typing... ").lower()
                            if ex == "c":
                                l14 = ("Q.System: Continue... ")
                                for text in l14:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                continue 
                                
                            elif ex == "d":
                                l15 = ("Q.System: Description...") 
                                for text in l15:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "1":
                            
                            l6 = ("You have selected Simple Printing")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Print Sample\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity1()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: This is how Print Looks Like.\n\t  Pretty simple right\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "2":
                            l6 = ("You have selected Ask for your Name")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Print with input\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity2()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: This will show the Input Text at the Print Section\n\t  Pretty simple right\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "3":
                            l6 = ("You have selected Name Counter")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Name Counter\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity3()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: This will Count the Input Text or the Name you Input\n\t  Pretty simple right\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "4":
                            l6 = ("You have selected Input Type Checker")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Type Checker\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity4()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: This will Put the Type of the Number you put\n\t  Using Type attribute\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        else:
                            os.system('cls')
                            l20 = ("Q.System: Unfortunate Not in the Options")  
                            l21 = ("\nQ.System: Try Again")
                            for text in l20 and l21:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            continue
                    continue
                elif bago == "n":
                    l14 = ("Q.System: Going back to Main Menu")
                    for text in l14:
                        print(text,end="", flush=True)
                        time.sleep(.03)
                    time.sleep(0.1)
                    l15 = ("...")    
                    for text in l15:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    break
                else:
                    l16 = ("Q.System: Unfortunate Not in the Options")
                    for text in l16:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    continue
        elif menu == "2": #variable
            while True:
                time.sleep(1)
                l5 = ("Variables\n")
                for text in l5:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1)
                l3 = ("\nA variable in Python is a name that stores a value.")
                l4 = ("\nYou can think of it like a container or a label that holds information.\n")
                for text in l3:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1.2)
                for text in l4:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1.2)
                l9 = ("\nQ.System: Want to see Example(Y - YES/N - NO(will go to menu): ): ")
                for text in l9:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(.2)
                bago = input(f"\n{nn}: Typing... ").lower()
                os.system('cls')
            
                if bago == "y":
                    while True:
                        time.sleep(1)
                        l1 = ("Loading....")
                        for text in l1:
                            print(text,end="", flush=True)
                            time.sleep(0.10)
                        time.sleep(.2)
                        os.system('cls')
                        l2 = ("Q.System: The name of your variable is vrb\n")
                        for text in l2:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(1)
                        vrb = ""
                        qq = ("\nQ.System: Put the Value of the Variable(vrb): ")
                        for text in qq:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(0.10)
                        www = input(f"\n{nn}: Typing... ")
                        time.sleep(1.2)
                        vrb += www
                        l3 = ("\nQ.System: Variable updated")
                        for text in l3:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(1.2)
                        os.system('cls')
                        l9 = ("Q.System: Now call your variable name(vrb)")
                        for text in l9:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(.10)
                        qqq = input(f"\n{nn}: Typing... ")
                        os.system('cls')
                        if qqq == "vrb":
                            l4 = (f"  Output: {vrb}\n")
                            for text in l4:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l5 = ("\nQ.System: Congratulation You Now know What is Variable\n")
                            for text in l4 and l5:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l6 = ("\nQ.System: Go to Description(y - yes/r - repeat)")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going To Description")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                os.system('cls')
                                break
                            elif tp == "r":
                                l12 = ("Q.System: Repeating..")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                os.system('cls')
                                continue
                            else:
                                la1 = ("Q.System: Unfortunate Not in the Options")
                                for text in la1:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                os.system('cls')
                        else:
                            l16 = ("Q.System: Unfortunate Not in the Options\nError...")
                            for text in l16:
                                print(text,end="", flush=True)
                                time.sleep(0.03) 
                            time.sleep(0.2)
                            os.system('cls')
                            continue
                elif bago == "n":
                    ll6 = ("Q.System: Going back to Main Menu")
                    for text in ll6:
                        print(text,end="", flush=True)
                        time.sleep(0.03) 
                    time.sleep(0.2)
                    os.system('cls')
                    break
                else:
                    l16 = ("Q.System: Unfortunate Not in the Options")
                    for text in l16:
                        print(text,end="", flush=True)
                        time.sleep(0.04) 
                    time.sleep(0.2)
                    os.system('cls')
                    continue
        
        elif menu == "3": #operators
            while True:
                os.system('cls')
                time.sleep(0.2)
                l1 = ("Operators\n")
                for text in l1:
                   print(text,end="", flush=True)
                   time.sleep(0.04) 
                time.sleep(1)
                l2 = ("\nOperators are special symbols or keywords that perform actions on values or variables.")
                for text in l2:
                   print(text,end="", flush=True)
                   time.sleep(0.04) 
                time.sleep(1)
                l3 = ("\nThey are like tools that let you calculate, compare, or combine information.\n")
                for text in l3:
                   print(text,end="", flush=True)
                   time.sleep(0.04) 
                time.sleep(1)
                l4 = ("\nHeres the Operators in Python\n")
                for text in l4:
                   print(text,end="", flush=True)
                   time.sleep(0.04) 
                time.sleep(1)
                print("\n ┌──────────────────────────────────┐ ┌──────────────────────────────────┐ ┌──────────────────────────────────┐ ┌──────────────────────────────────┐")
                time.sleep(.1)
                print(" │           Arithmethic            │ │           Assignment             │ │           Comparison             │ │             Logical              │")
                time.sleep(.1)
                print(" │──────────────────────────────────│ │──────────────────────────────────│ │──────────────────────────────────│ │──────────────────────────────────│")
                time.sleep(.1)
                print(" │                                  │ │                                  │ │                                  │ │                                  │")
                time.sleep(.1)
                print(" │         + - Addition             │ │       = - Assign Value           │ │         == - Equal to            │ │     and - Both must be true      │")
                time.sleep(.1)
                print(" │         - - Subtraction          │ │       += - Add & assign          │ │         != - Not equal           │ │     or - At least one is true    │")
                time.sleep(.1)
                print(" │         * - Multiplication       │ │       -= - Subtract & assign     │ │         > - Greater than         │ │     not - Reverses True/False    │")
                time.sleep(.1) 
                print(" │         / - Divition             │ │       *= - Multiply & assign     │ │         < - Less than            │ │                                  │")
                time.sleep(.1)
                print(" │         // - Floor Divition      │ │       /= - Divide & assign       │ │         >= - Greater or Equal    │ │                                  │")
                time.sleep(.1)
                print(" │         % - Modulus              │ │       %= - Modulus & assign      │ │         <= - Less or Equal       │ │                                  │")
                time.sleep(.1)
                print(" │         ** - Exponent            │ │                                  │ │                                  │ │                                  │")
                time.sleep(.1)
                print(" └──────────────────────────────────┘ └──────────────────────────────────┘ └──────────────────────────────────┘ └──────────────────────────────────┘")
                time.sleep(1)
                l5 = ("Q.System: Want to see Example(Y - YES/N - NO)? ")
                for text in l5:
                   print(text,end="", flush=True)
                   time.sleep(0.04) 
                time.sleep(.4)
                bago = input(f"\n{nn}: Typing... ").lower()
                time.sleep(1.2)
                os.system('cls')
                if bago == "y":
                    while True:
                        a7 = ("Loading Activity Examples....\n")
                        for text in a7:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(1.2)
                        os.system('cls')
                        
                        a1 = ("...")
                        for text in a1:
                            print(text, flush=True)
                            time.sleep(1)
                        time.sleep(1.2)
                        os.system('cls')
                        print("┌────────────────────────────────────────────────────────────────────┐")
                        time.sleep(.1)
                        print("│                          Operators                                 │")
                        time.sleep(.1)
                        print("│────────────────────────────────────────────────────────────────────│")
                        time.sleep(.1)
                        print("│   1 - Simple Arithmetic                                            │")
                        time.sleep(.1)
                        print("│   2 - Arithmetic Operator Function                                 │")
                        time.sleep(.1)
                        print("│   3 - Assignment Operator                                          │")
                        time.sleep(.1)
                        print("│   4 - Comparison Operator                                          │")
                        time.sleep(.1)
                        print("│   5 - Logical Operator                                             │")
                        time.sleep(.1)
                        print("│                                                                    │")
                        time.sleep(.1)
                        print("│   E - Exit(Go to description)                                      │")
                        time.sleep(.1)
                        print("└────────────────────────────────────────────────────────────────────┘")
                        
                        print("\nQ.System: Enter your choice: ")
                        menu = input(f"\n{nn}: Typing... ").lower()
                        os.system('cls')
                        
                        if menu == "e".lower():
                            l12 = ("\nQ.System: Exiting.....")
                            for text in l12:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            l13 = ("\nQ.System: (D - Description or C - Continue )")
                            for text in l13:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            ex = input(f"\n{nn}: Typing... ").lower()
                            if ex == "c":
                                l14 = ("Q.System: Continue... ")
                                for text in l14:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                continue 
                                
                            elif ex == "d":
                                l15 = ("Q.System: Description...") 
                                for text in l15:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "1": # operators1
                            l6 = ("You have selected Simple Arithmetic")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Arithmetic\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            activity5()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using operators you can add any value to the variable with set of number.\n\t  Pretty simple right\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "2": #operator2
                            l6 = ("You have selected Arithmetic Function")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Operator Function\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity6()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using all the Arithmetic Function to the two Input Number.\n\t  Pretty simple right\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "3": #operator3
                            l6 = ("You have selected Assignment Operator")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Assignment Operator\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity7()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Updating the value of variable using Assignment Operator.\n\t  Pretty simple right\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue                            
                        elif menu == "4": #operator 4
                            l6 = ("You have selected Comparison Operator")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Comparison Operator\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity8()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using Comparison Operator will show Result as a Boolean.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "5": #operator5
                            l6 = ("You have selected Logical Operator")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Logical Operator\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity9()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using Logical Operator will also show Result as a Boolean.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        else:
                            l16 = ("Q.System: Unfortunate Not in the Options")
                            for text in l16:
                                print(text,end="", flush=True)
                                time.sleep(.03) 
                            time.sleep(0.2)
                            os.system('cls')
                            continue
                    continue
                elif bago == "n":
                    l14 = ("Q.System: Going back to Main Menu")
                    for text in l14:
                        print(text,end="", flush=True)
                        time.sleep(.03)
                    time.sleep(0.1)
                    l15 = ("...")    
                    for text in l15:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    break
                else:
                    l16 = ("Q.System: Unfortunate Not in the Options")
                    for text in l16:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    os.system('cls')
                    continue         
        elif menu == "4": #conditional statement
            while True:
                os.system('cls')
                time.sleep(1)
                l1 = ("Conditional Statement\n")
                for text in l1:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(.2)
                l2 = ("\nA conditional statement in Python allows your program to make decisions.")
                for text in l2:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                l3 = ("\nIt lets the code choose what to do based on whether a condition is True or False.\n")
                for text in l3:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(1)
                l4 = ("\nIf - If none of the above conditions were true, do this.")
                for text in l4:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(1)
                l5 = ("\nelif - If the previous conditions were not true, try this new condition.")
                for text in l5:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1)
                l6 = ("\nelse - If none of the above conditions were true, do this.\n")
                for text in l6:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1)
                l7 = ("\nQ.System: Want to see Example(Y - YES/N - NO)? ")
                for text in l7:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                bago = input(f"\n{nn}: Typing... ").lower()
                time.sleep(1)
                os.system('cls')
                if bago == "y":
                    while True:
                        os.system('cls')
                        a7 = ("Loading Activity Examples....\n")
                        for text in a7:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(1.2)
                        os.system('cls')
                        
                        a1 = ("...")
                        for text in a1:
                            print(text, flush=True)
                            time.sleep(1)
                        time.sleep(1.2)
                        os.system('cls')
                        print("┌──────────────────────────────────────────────────────────┐")
                        time.sleep(.1)
                        print("│                 Conditional Statement                    │")
                        time.sleep(.1)
                        print("│──────────────────────────────────────────────────────────│")
                        time.sleep(.1)
                        print("│                                                          │")
                        time.sleep(.1)
                        print("│     1 - Conditional with Arithmetic                      │")
                        time.sleep(.1)
                        print("│     2 - Conditional with Logical and comparison          │")
                        time.sleep(.1)
                        print("│                                                          │")
                        time.sleep(.1)
                        print("│     E - Exit                                             │")
                        time.sleep(.1)
                        print("└──────────────────────────────────────────────────────────┘")
                        la3 = ("Q.System: Enter your choice: ")
                        for text in la3:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        menu = input(f"\n{nn}: Typing... ").lower()
                        time.sleep(1)
                        os.system('cls')
                        if menu == "e".lower():
                            l12 = ("\nQ.System: Exiting.....")
                            for text in l12:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            l13 = ("\nQ.System: (D - Description or C - Continue )")
                            for text in l13:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            ex = input(f"\n{nn}: Typing... ").lower()
                            if ex == "c":
                                l14 = ("Q.System: Continue... ")
                                for text in l14:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                continue 
                                
                            elif ex == "d":
                                l15 = ("Q.System: Description...") 
                                for text in l15:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                            
                        elif menu == "1":
                            l6 = ("You have selected Conditional with Arithmetic")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Conditional with Arithmetic\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity10()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using Conditional Statement let user pick in the options.\n\t  This make our coke wider.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "2":
                            l6 = ("You have selected Conditional with Logical and Comparison stat")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Conditional with Logical and Comparison stat\nTemperature Checker\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity11()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using Conditional Statement with Logical and Comparison Statement.\n\t  Let us Scale the condition and Put the possible Data.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        else:
                            l16 = ("Q.System: Unfortunate Not in the Options")
                            for text in l16:
                                print(text,end="", flush=True)
                                time.sleep(.03) 
                            time.sleep(0.2)
                            continue
                elif bago == "n":
                    l14 = ("Q.System: Going back to Main Menu")
                    for text in l14:
                        print(text,end="", flush=True)
                        time.sleep(.03)
                    time.sleep(0.1)
                    l15 = ("...")    
                    for text in l15:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    break
                else:
                    l16 = ("Q.System: Unfortunate Not in the Options")
                    for text in l16:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    continue
        elif menu == "5": #loop
            while True:
                time.sleep(1)
                l1 = ("Looping")
                for text in l1:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(1)
                l2 = ("\nLooping in Python means repeating a block of code multiple times.")
                for text in l2:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1)
                l3 = ("\nIt lets a program do something again and again without writing the same line many times.\n")
                for text in l3:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(2)
                l4 = ("\nTwo main types of loops\n")
                for text in l4:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1)
                l5 = ("\nFor loop\nUsed when you want to repeat something a specific number of times or go through items in a list.\n")
                for text in l5:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1)
                l6 = ("\nWhile loop\nRepeats code as long as a condition is true.\n")
                for text in l6:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1)
                l7 = ("\nQ.System: Want to see some Examples (Y - YES/N - NO)? ")
                for text in l7:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(1)
                bago = input(f"\n{nn}: Typing... ").lower()
                if bago == "y":
                    while True:
                        os.system('cls')
                        a7 = ("Q.System: Loading Activity Examples....\n")
                        for text in a7:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(1.2)
                        os.system('cls')
                        
                        a1 = ("...")
                        for text in a1:
                            print(text, flush=True)
                            time.sleep(1)
                        time.sleep(1.2)
                        os.system('cls')
                        print("┌────────────────────────────────────────┐ ┌────────────────────────────────────────┐")
                        time.sleep(.1)
                        print("│               For Loop                 │ │              While Loop                │")
                        time.sleep(.1)
                        print("│────────────────────────────────────────│ │────────────────────────────────────────│ ")
                        time.sleep(.1)
                        print("│                                        │ │                                        │")
                        time.sleep(.1)
                        print("│      1 - Simple For Loop               │ │      4 - Simple While Loop             │")
                        time.sleep(.1)
                        print("│      2 - Nested Loop                   │ │      5 - Anime Compiler                │")
                        time.sleep(.1)
                        print("│      3 - Multiple Nested Loop          │ │          using While Loop              │")
                        time.sleep(.1)
                        print("│                                        │ │                                        │")
                        time.sleep(.1)
                        print("│      E - Exit                          │ │                                        │")
                        time.sleep(.1)
                        print("└────────────────────────────────────────┘ └────────────────────────────────────────┘")
                        lb9 = ("Enter your choice: ")
                        for text in lb9:
                            print(text,end="", flush=True)
                        time.sleep(.2)
                        menu = input(f"\n{nn}: Typing... ").lower()
                        os.system('cls')        
                        if menu == "e".lower():
                            l12 = ("\nQ.System: Exiting.....")
                            for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                            l13 = ("\nQ.System: (D - Description or C - Continue )")
                            for text in l13:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            ex = input(f"\n{nn}: Typing... ").lower()
                            if ex == "c":
                                l14 = ("Q.System: Continue... ")
                                for text in l14:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                continue 
                                
                            elif ex == "d":
                                l15 = ("Q.System: Description...") 
                                for text in l15:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "1":  
                            time.sleep(1)
                            l6 = ("You have selected Simple For Loop")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Simple For Loop\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity12()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using for loop Let print statement many times.\n\t  Pretty easy right.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Q.System: Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue                          
                        elif menu == "2":
                            time.sleep(1)
                            l6 = ("You have selected Nested For Loop")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Nested For Loop\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity17()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: A loop inside another loop.\n\t  Think of it like a loop within a loop — the inner loop runs completely for every single iteration of the outer loop.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nNext Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input("\nTyping... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nGoing back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue                         
                        elif menu == "3":
                            time.sleep(1)
                            l6 = ("You have selected Pyramid")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Pyramid\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            for u in range(1,7):
                                for i in range(6,u - 1,-1):
                                    print(" " ,end="")
                                for q in range(1,u * 2):
                                    print("*" ,end="")
                                print()    
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using Nested For Loop can Create Pyramid and Many more.\n\t  You can do many shape as you want using nested for loop.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nNext Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input("\nTyping... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nGoing back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue              
                        elif menu == "4":
                            time.sleep(1)
                            l6 = ("You have selected Simple While Loop")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Simple While Loop\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity21()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: A while loop in Python repeats a block of code as long as a condition is True.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nNext Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input("\nTyping... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nGoing back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue                        
                        elif menu == "5":
                            time.sleep(1)
                            l6 = ("You have selected Anime Compiler")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Anime Compiler\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            cchal15()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: In here i build a System using While Loop\n\t  In here using while loop keep your program running until you input the stopper.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nNext Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input("\nTyping... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nGoing back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue                        

                        else:
                            l16 = ("Unfortunate Not in the Options")
                            for text in l16:
                                print(text,end="", flush=True)
                                time.sleep(.03) 
                            time.sleep(0.2)
                            os.system('cls')
                            continue
                elif bago == "n":
                    l14 = ("Going back to Main Menu")
                    for text in l14:
                        print(text,end="", flush=True)
                        time.sleep(.03)
                    time.sleep(0.1)
                    l15 = ("...")    
                    for text in l15:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    break
                else:
                    l16 = ("Unfortunate Not in the Options")
                    for text in l16:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    os.system('cls')
                    continue
        elif menu == "6": #list
            while True:
                os.system('cls')
                time.sleep(1)
                l1 = ("List")
                for text in l1:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(1)
                l2 = ("\nA list in Python is a collection of items stored in a single variable.")
                for text in l2:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(1)
                l3 = ("\nIt can hold numbers, strings, or any type of data, and you can change it later.\n")
                for text in l3:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(1)
                l4 = ("\nDictionary")
                for text in l4:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(1)
                l5 = ("\nA dictionary in Python is a collection of data stored in key value pairs.\n")
                for text in l5:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(1)
                print("┌─────────────────────────────────────────────────────────┐ ┌───────────────────────────────────────────────────────────┐")
                time.sleep(.1)
                print("│                 Common List Operators                   │ │              Common Dictionary Operators                  │")
                time.sleep(.1) 
                print("│─────────────────────────────────────────────────────────│ │───────────────────────────────────────────────────────────│ ")
                time.sleep(.1)
                print("│                                                         │ │                                                           │")
                time.sleep(.1)
                print("│      Append  -  Adds an item to the end                 │ │   Keys      - Returns all the keys in the dictionary.     │")
                time.sleep(.1)
                print("│      Insert  -  Inserts item at specified index         │ │   Values    - Returns all the values in the dictionary.   │")
                time.sleep(.1)
                print("│      Remove  -  Removes first occurrence of item        │ │   Items     - Returns key value pairs as tuples.          │")
                time.sleep(.1) 
                print("│      Pop     -  Removes and returns item at index       │ │   Get(keys) - Gets the value of a key safely.             │")
                time.sleep(.1) 
                print("│      Len     -  Returns number of elements              │ │   Update    - Adds or updates multiple key value pairs.   │")
                time.sleep(.1)
                print("│      Sort    -  Sorts the list (ascending)              │ │   Pop(key)  - Removes a key value pair.                   │")
                time.sleep(.1)
                print("│      Reverse -  Reverses the list order                 │ │   Clear     - Removes all items from the dictionary.      │")
                time.sleep(.1)
                print("│                                                         │ │                                                           │")
                time.sleep(.1) 
                print("│      E - Exit                                           │ │                                                           │")
                time.sleep(.1) 
                print("└─────────────────────────────────────────────────────────┘ └───────────────────────────────────────────────────────────┘")
                time.sleep(1)
                l6 = ("Q.System: Want to see some Examples(Y - YES/N - NO)? ")
                for text in l6:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(.02)
                bago = input(f"\n{nn} Typing... ").lower() 
                if bago == "y":
                    while True:
                        os.system('cls')
                        a7 = ("Loading Activity Examples....\n")
                        for text in a7:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(1.2)
                        os.system('cls')
                        
                        a1 = ("...")
                        for text in a1:
                            print(text, flush=True)
                            time.sleep(1)
                        time.sleep(1.2)
                        os.system('cls')
                        print("┌────────────────────────────────────────┐ ┌────────────────────────────────────────┐")
                        time.sleep(.1)
                        print("│                  List                  │ │              Dictionary                │")
                        time.sleep(.1)
                        print("│────────────────────────────────────────│ │────────────────────────────────────────│ ")
                        time.sleep(.1)
                        print("│                                        │ │                                        │")
                        time.sleep(.1)
                        print("│      1 - Simple List                   │ │      4 - Simple Dictionary             │")
                        time.sleep(.1)
                        print("│      2 - List with for loop            │ │                                        │")
                        time.sleep(.1)
                        print("│      3 - List Reversed                 │ │                                        │")
                        time.sleep(.1)
                        print("│                                        │ │                                        │")
                        time.sleep(.1)
                        print("│      E - Exit(Back to Description)     │ │                                        │")
                        time.sleep(.1)
                        print("└────────────────────────────────────────┘ └────────────────────────────────────────┘")
                        time.sleep(1)
                        lb9 = ("Q.System: Enter your choice: ")
                        for text in lb9:
                            print(text,end="", flush=True)
                            time.sleep(.02)
                        menu = input(f"\n{nn}: Typing... ").lower()
                        os.system('cls')        
                        if menu == "e".lower():
                            l12 = ("\nExiting.....")
                            for text in l12:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            l13 = ("\n(D - Description or C - Continue )")
                            for text in l13:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            ex = input("\nTyping... ").lower()
                            if ex == "c":
                                l14 = ("Continue... ")
                                for text in l14:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                continue 
                                
                            elif ex == "d":
                                l15 = ("Description...") 
                                for text in l15:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                break
                            else:
                                l16 = ("Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue
                        elif menu == "1": 
                            time.sleep(1)
                            l6 = ("You have selected Simple List")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Simple List\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity23()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using List can let you store as many item  as you want in the variable.\n\t It let you access to add,remove,sort and many more \n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nNext Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input("\nTyping... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nGoing back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue                                                     
                        elif menu == "2":
                            time.sleep(1)
                            l6 = ("You have selected List with for loop")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("List with for loop\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity23_2()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using List with for loop let you print the items in the list \n\t verticaly with custom name not just the item of the list\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nNext Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input("\nTyping... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nGoing back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue                              
                        elif menu == "3":
                            time.sleep(1)
                            l6 = ("You have selected List Reversed")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("List Reversed Output\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity23_1()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using List can also reverse all the item in the list like it always start from z.\n\t  Pretty simple right\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nNext Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input("\nTyping... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nGoing back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue                            
                        elif menu == "4":
                            time.sleep(1)
                            l6 = ("You have selected Simple Dictionary")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Simple Dictionary\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            Activity27()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: Using Dictionary Let you Set a value for the given data.\n\t  Letting it more accesible.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nNext Activity (Y) or Back to Description (B):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input("\nTyping... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nGoing back To Activity Menu\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "b":
                                l12 = ("Going Back to Description..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue                            
                        else:
                            l16 = ("Unfortunate Not in the Options")
                            for text in l16:
                                print(text,end="", flush=True)
                                time.sleep(.03) 
                            time.sleep(0.2)
                            os.system('cls')
                            continue   
                    
                elif bago == "n":
                    l14 = ("Going back to Main Menu")
                    for text in l14:
                        print(text,end="", flush=True)
                        time.sleep(.03)
                    time.sleep(0.1)
                    l15 = ("...")    
                    for text in l15:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    break
                else:
                    l16 = ("Unfortunate Not in the Options")
                    for text in l16:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    os.system('cls')
                    continue    


        elif menu == "7": #function
            while True:
                os.system('cls')
                time.sleep(1)
                l1 = ("Functions\n")
                for text in l1:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(1)         
                print("\n┌──────────────────────────────────────────────────────────────────────────────────────────────┐")
                time.sleep(.1) 
                print("│  Function                                                                                    │") 
                time.sleep(.1) 
                print("│                                                                                              │")
                time.sleep(.1)
                print("│  A function in Python is a reusable block of code that performs a specific task.             │") 
                time.sleep(.1) 
                print("│  A function is like a machine: You give it input, it does some work, and gives you output.   │") 
                time.sleep(.1) 
                print("│                                                                                              │") 
                time.sleep(.1) 
                print("│──────────────────────────────────────────────────────────────────────────────────────────────│") 
                time.sleep(.1) 
                print("│     Concept                       Description                                                │") 
                time.sleep(.1)
                print("│                                                                                              │")
                time.sleep(.1)
                print("│  Built-in Functions -  Predefined by the language (e.g., print(), len())                     │") 
                time.sleep(.1)
                print("│  Programmer-Defined -  Created by the user using (def)                                       │") 
                time.sleep(.1)
                print("│  Access Methods     -  Direct call, import from modules, lambda expressions                  │") 
                time.sleep(.1)
                print("│  Pass by Value      -  Copies data (immutable types), original remains unchanged             │") 
                time.sleep(.1)
                print("│  Pass by Reference  -  Passes reference (mutable types), original may be modified            │") 
                time.sleep(.1) 
                print("│                                                                                              │")
                time.sleep(.1)
                print("│  E - Exit                                                                                    │") 
                time.sleep(.1) 
                print("└──────────────────────────────────────────────────────────────────────────────────────────────┘")   
                l6 = ("Q.System: Want to see some Examples(Y - YES/N - NO)? ")
                for text in l6:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(.2)
                bago = input(f"\n{nn}: Typing... ").lower()  


                if bago == "y":
                    while True:
                        os.system('cls')
                        a7 = ("Loading Activity Examples....\n")
                        for text in a7:
                            print(text,end="", flush=True)
                            time.sleep(.03)
                        time.sleep(1.2)
                        os.system('cls')
                        a1 = ("...")
                        for text in a1:
                            print(text, flush=True)
                            time.sleep(1)
                        time.sleep(1.2)
                        os.system('cls')
                        print("┌─────────────────────────────────────────────┐")
                        time.sleep(.1)
                        print("│                Functions                    │")
                        time.sleep(.1)
                        print("│─────────────────────────────────────────────│")
                        time.sleep(.1)
                        print("│                                             │")
                        time.sleep(.1)
                        print("│   1 - Programmer-Defined                    │")
                        time.sleep(.1)
                        print("│   2 - Access Methods                        │")
                        time.sleep(.1)
                        print("│                                             │")
                        time.sleep(.1)
                        print("│   E - Exit(Back to Description)             │")
                        time.sleep(.1)
                        print("└─────────────────────────────────────────────┘")
                        time.sleep(1)
                        lb9 = ("Q.System:Enter your choice: ")
                        for text in lb9:
                            print(text,end="", flush=True)
                            time.sleep(.02)
                        menu = input(f"\n{nn}: Typing... ").lower()
                        os.system('cls') 
                        

                        if menu == "e".lower():
                            l12 = ("\nQ.System: Exiting.....")
                            for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                            l13 = ("\nQ.System: (D - Description or C - Continue )")
                            for text in l13:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            ex = input(f"\n{nn}: Typing... ").lower()
                            if ex == "c":
                                l14 = ("Q.System: Continue... ")
                                for text in l14:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                continue 
                                
                            elif ex == "d":
                                l15 = ("Q.System: Description...") 
                                for text in l15:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                os.system('cls')
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue


                        elif menu == "1":
                            time.sleep(1)
                            l6 = ("You have selected Programmer-Defined")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nQ.System: Loading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Programmer-Defined\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            act24()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: The program shows how functions can be defined inside another function, how data can be passed using parameters,\n\t and how loops can be used to perform calculations efficiently.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (D):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input(f"\n{nn}: Typing... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Description\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "d":
                                l12 = ("Q.System: Going Back to Menu..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue      


                        elif menu == "2":
                            time.sleep(1)
                            l6 = ("You have selected Access Methods")
                            for text in l6:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l7 = ("\nLoading Activity....")
                            for text in l7:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            os.system('cls')
                            l8 = ("Access Methods\n")
                            time.sleep(0.2)
                            for text in l8:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            l9 = ("\n Output:")
                            for text in l9:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            print("\n--------------------------\n")
                            time.sleep(0.2)
                            act22()
                            time.sleep(0.2)    
                            print("\n--------------------------\n")
                            l18 = ("\nQ.System: This program is a simple guessing game where the user keeps guessing until they find the correct number.\n\t It demonstrates how loops and conditions can be used to control program flow and interact with users.\n")
                            for text in l18:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(1.2)
                            l10 = ("\nQ.System: Next Activity (Y) or Back to Description (D):")
                            for text in l10:
                                print(text,end="", flush=True)
                                time.sleep(.03)
                            time.sleep(0.2)
                            tp = input("\nTyping... ").lower()
                            os.system('cls')
                            if tp == "y":
                                l11 = ("\nQ.System: Going back To Activity Description\n")
                                for text in l11:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                continue
                            elif tp == "d":
                                l12 = ("Q.System: Going Back to Menu..\n")
                                for text in l12:
                                    print(text,end="", flush=True)
                                    time.sleep(.03)
                                time.sleep(0.3)
                                break
                            else:
                                l16 = ("Q.System: Unfortunate Not in the Options")
                                for text in l16:
                                    print(text,end="", flush=True)
                                    time.sleep(.03) 
                                time.sleep(0.2)
                                os.system('cls')
                                continue                            
                        else:
                            l16 = ("Q.System: Unfortunate Not in the Options")
                            for text in l16:
                                print(text,end="", flush=True)
                                time.sleep(.03) 
                            time.sleep(0.2)
                            os.system('cls')
                            continue
                elif bago == "n":
                    l14 = ("Q.System: Going back to Main Menu")
                    for text in l14:
                        print(text,end="", flush=True)
                        time.sleep(.03)
                    time.sleep(0.1)
                    l15 = ("...")    
                    for text in l15:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    break
                else:
                    l16 = ("Q.System: Unfortunate Not in the Options")
                    for text in l16:
                        print(text,end="", flush=True)
                        time.sleep(.03) 
                    time.sleep(0.2)
                    os.system('cls')
                    continue


        elif menu == "0": #exit
            l12 = ("\nQ.System: Exiting.....")
            for text in l12:
                                print(text,end="", flush=True)
                                time.sleep(.03)
            l13 = ("\nQ.System: (E - Exit or C - Continue )")
            for text in l13:
                print(text,end="", flush=True)
                time.sleep(.03)
            time.sleep(0.2)
            ex = input(f"\n{nn}Typing... ").lower()
            if ex == "c":
                l14 = ("Q.System: Continue... ")
                for text in l14:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                os.system('cls')
                continue 
                
            elif ex == "e":
                l15 = ("Exiting...") 
                for text in l15:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(0.2)
                l02 = ("Q.System: Thank You For Using my System")
                l02 = ("Q.System: Exiting...") 
                for text in l15:
                    print(text,end="", flush=True)
                    time.sleep(.03)
                time.sleep(0.2)
                os.system('cls')
                break
            else:
                l16 = ("Q.System: Unfortunate Error Input")
                for text in l16:
                    print(text,end="", flush=True)
                    time.sleep(.03) 
                time.sleep(0.2)
                os.system('cls')
                continue 


        elif menu == "9": #search
            
            rhs()  
            continue

        elif menu == "8": #codechallenge
            
            codelist() 
            continue
        
    elif main == "n":
        print("Q.System: Thank you for using my System...")
        for text in l16:
            print(text,end="", flush=True)
            time.sleep(.03) 
        time.sleep(0.2)
        os.system('cls')
        break                 
    else:
        l16 = ("Unfortunate Not in the Options")
        for text in l16:
            print(text,end="", flush=True)
            time.sleep(.03) 
        time.sleep(0.2)
        os.system('cls')
        continue

