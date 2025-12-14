def cchal1():
    r = input("Halloww! Name Please: ")
    print("\t\t\t\t\t*\t\t\t\t\n\t\t\t\t*\t\t*\t\t\t\n\t\t\t*\t\t\t\t*\t\t\n\t\t*\t\t\tHi!\t\t\t*\t\n\t*\t\t\t\t",r,"\t\t\t\t*\n\t\t*\t\t\t\t\t\t*\t\n\t\t\t*\t\t\t\t*\t\t\n\t\t\t\t*\t\t*\t\t\t\n\t\t\t\t\t*\t\t\t\t")
def cchal2():
    xel = eval(input("Enter Amount to Deposit: "))
    a = xel // 1000
    xel = xel % 1000
    b = xel // 500
    xel = xel % 500
    c = xel // 200
    xel = xel % 200
    d = xel // 100
    xel = xel % 100
    e = xel // 50
    xel = xel % 50
    f = xel // 20
    xel = xel % 20
    g = xel // 10
    xel = xel % 10
    h = xel // 5
    xel = xel % 5
    i = xel // 1
    xel = xel % 1
    print("|",a, "= P1000")
    print("|",b, "= P500")
    print("|",c, "= P200")
    print("|",d, "= P100")
    print("|",e, "= P50")
    print("|",f, "= P20")
    print("|",g, "= P10")
    print("|",h, "= P5")
    print("|",i, "= P1")
def cchal3():
    email = "BSIT-1A"
    passw = "secret"

    x = input("Email: ")
    y = input("Password: ")
    if x.lower == email and y.lower == passw:
        print("Grant Access")
    else:
        print("Access Denied")
        
def cchal4():
    ol = int(input("Pleaseeee Put any Number: "))
    if ol % 2 == 0:
        print("The number", ol, "is even number")
    else:
        print("The number", ol, "is odd number")

def cchal5():
        #My Anime List
    #Different type of Anime
    #Duration of Anime

    print("Welcome To my Anime library")
    print("Anime list Recommendation")
    print("what kind of anime")
    print("1-ISEKAI")
    print("2-COMEDY")
    print("3-FANTACY")
    print("4-ACTION")
    menu = int(input("What kind of Anime you like(1,2,3,4,): "))

    #Isekaiiiiiiiiiiiii

    if menu == 1:
        selected = "ISEKAI"
        print("Anime :", selected)
        long = input("Range (Long or Short): ")

    #longggggggg

        if long.lower() == "long":
            print("Size:", long)
            year = eval(input("What year(2000,2010,2020): "))

            if year == 2000:
                print("Year: ", year)
                print("I recommend Anime for",selected,"range of",long,"Year",year, "\n-The Twelve Kingdoms Is Rightfully Regarded as a Cult Classic of Isekai \n-MÄR Embraces the Best Shonen Clichés \n-Kiba Is Unexpectedly Bleak for a Card Game Isekai Adventure")
            
            elif year == 2010:
                print("Year: ", year)
                print("I recommend Anime for",selected,"range of",long,"Year",year,"\n-Magi: The Labyrinth of Magic\n-Re:Zero – Starting Life in Another World\n-Sword Art Online")
            
            elif year == 2020:
                print("Year: ", year)
                print("I recommend Anime for",selected,"range of",long,"Year",year,"\n-Konosuba\n-That Time I Got Reincarnated as a Slime\n-Jobless Reincarnation: Mushoku Tensei")
        
            else:
                print("Thank You so Much")

    #SHortttttt

        if long.lower() == "short":
            print("Size:", long)
            year = eval(input("What year(2000,2010,2020): "))

            if year == 2000:
                print("Year: ", year)
                print("I recommend Anime for",selected,"range of",long,"Year",year, "\n-Dual! Parallel Trouble Adventure\n-Now and Then, Here and There\n-Haibane Renmei")
            
            elif year == 2010:
                print("Year: ", year)
                print("I recommend Anime for",selected,"range of",long,"Year",year,"\n-No Game No Life\n-Problem Children Are Coming from Another World, Aren’t They?\n-Gate: Jieitai Kanochi nite, Kaku Tatakaeri")
            elif year == 2020:
                print("Year: ", year)
                print("I recommend Anime for",selected,"range of",long,"Year",year,"\n-Wise Man’s Grandchild (Kenja no Mago)\n-Tsukimichi: Moonlit Fantasy (Season 2)\n-How a Realist Hero Rebuilt the Kingdom")
            else:
                print("Error Put Year")
        else:
            print("Error, put Long or Short")

    #COmedyyyyyyy

    elif menu == 2:
        selec = "COMEDY"
        print("Anime: ",selec)
        longe = input("Range (Long or Short): ")

    #Longggg

        if longe.lower() == "long":
            print("Size:", longe)
            years = eval(input("What year(2000,2010,2020): "))

            if years == 2000:
                print("Year: ", years)
                print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-Gintama\n-School Rumble\n-One Piece")
            elif years == 2010:
                print("Year: ", years)
                print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-Fairy Tail\n-Sket Dance\n-Assassination Classroom")
            elif years == 2020:
                print("Year: ", years)
                print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-KonoSuba: God’s Blessing on This Wonderful World!\n-Uzaki-chan Wants to Hang Out!\n-Komi Can’t Communicate")
            else:
                print("error put year")

    #Shorttttt
        
        elif longe.lower() == "short":
            print("Size:", longe)
            years = eval(input("What year(2000,2010,2020): "))

            if years == 2000:
                print("Year: ", years)
                print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-Excel Saga\n-Azumanga Daioh\n-Pani Poni Dash!")

            elif years == 2010:
                print("Year: ", years)
                print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-Nichijou (My Ordinary Life)\n-Isekai Quartet\n-Asobi Asobase")
            elif years == 2020:
                print("Year: ", years)
                print("I recommend Anime for",selec,"range of",longe,"Year",years, "\n-Komi Can’t Communicate\n-My Senpai is Annoying\n-Spy × Family")
            else:
                print("error put year")	
        else:
            print("error put long or short")

    elif menu == 3:
        sel = "Adventure"
        print("Anime: ",sel)
        longes = input("Range (Long or Short): ")
        
        if longes.lower() == "long":
            print("Size:", longes)
            yearsw = eval(input("What year(2000,2010,2020): "))

            if yearsw == 2000:
                print("Year: ", yearsw)
                print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-One Piece\n-Naruto\n-Bleach")
            elif yearsw == 2010:
                print("Year: ", yearsw)
                print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-Hunter × Hunter\n-Boruto: Naruto Next Generations\n-Sword Art Online")
            elif yearsw == 2020:
                print("Year: ", yearsw)
                print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-Black Clover\n-Dragon Quest: The Adventure of Dai\n-That Time I Got Reincarnated as a Slime")
            else:
                print("error put year")

        elif longes.lower() == "short":
            print("Size:", longes)
            yearsw = eval(input("What year(2000,2010,2020): "))

            if yearsw == 2000:
                print("Year: ", yearsw)
                print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-Scrapped Princess\n-Wolf’s Rain\n-Samurai Champloo")
            elif yearsw == 2010:
                print("Year: ", yearsw)
                print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-Made in Abyss\n-No Game No Life\n-Noragami")	
            elif yearsw == 2020:
                print("Year: ", yearsw)
                print("I recommend Anime for",sel,"range of",longes,"Year",yearsw, "\n-Jobless Reincarnation: Mushoku Tensei\n-Ranking of Kings (Ousama Ranking)\n-Somali and the Forest Spirit")
            else:
                print("error put year")

    elif menu == 4:
        sell = "Action"
        print("Anime: ",sell)
        longest = input("Range (Long or Short): ")
        
        if longest.lower() == "long":
            print("Size:", longest)
            yearsp = eval(input("What year(2000,2010,2020): "))
        
            if yearsp == 2000:
                print("Year: ", yearsp)
                print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-Fullmetal Alchemist\n-D.Gray-man\n-Zatch Bell! (Konjiki no Gash Bell!!)")
            elif yearsp == 2010:
                print("Year: ", yearsp)
                print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-JoJo’s Bizarre Adventure\n-Attack on Titan\n-World Trigger")
            elif yearsp == 2020:
                print("Year: ", yearsp)
                print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-My Hero Academia\n-Bleach: Thousand-Year Blood War\n-Demon Slayer")
            else:
                print("error put year")
        elif longest.lower() == "short":
            print("Size:", longest)
            yearsp = eval(input("What year(2000,2010,2020): "))

            if yearsp == 2000:
                print("Year: ", yearsp)
                print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-Black Lagoon\n-Afro Samurai\n-Gungrave")
            elif yearsp == 2010:
                print("Year: ", yearsp)
                print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-Akame ga Kill!\n-Parasyte: The Maxim\n-Black Bullet")
            
            elif yearsp == 2020:
                print("Year: ", yearsp)
                print("I recommend Anime for",sell,"range of",longest,"Year",yearsp, "\n-Jujutsu Kaisen\n-Chainsaw Man\n-Tower of God")
            else:
                print("error put year")
        else:
            print("error put long or short")
    else:
        print("error \nplease select 1,2,3,4")
def cchal6():
    name = eval(input("Put a number: "))
    num = 1
    for u in range(name,0,-1):
        num *= u
    print("the factorial of", name ,"is",num)

def cchal7():
    tot = 0
    for x in range(1, 11,1): 
        name = eval(input("Put Number: "))
        if name % 2:
            tot += name
    print("The Sum of all odd number is",tot) 
def cchal8():
    print("Multiplication Table Maker")
    name = eval(input("Put a Number: "))
    print("Multiplication Table For: ",name)
    for u in range(1 ,11):
        total = name * u
    print(name,"x",u,"=", total)
def cchal9():
    print("Countdown Simulator")
    name = eval(input("Count Start: "))
    print("\nCountdown started")
    for u in range(name,0,-1):
        print(u)
    print("lift off")
def cchal10():
    #Make a pyramid using for loop

    print("\t\t *")
    for me in range(2,11):
        for u in range(10,me,-1):
            print(" ",end=" ")
        for tm in range(1,me,1):
            print("*",end=" ")
        for hm in range(1,me,1):
            print("*",end=" ")
        print()
def cchal11():
    #Make a Diamond using loops
    print("\t\t *")
    for me in range(2,10,1):
        for u in range(10,me,-1):
            print(" ",end=" ")
        for tm in range(1,me,1):
            print("*",end=" ")
        for hm in range(1,me,1):
            print("*",end=" ")
        print()
    for me in range(1,10,1):
        for u in range(1,me,1):
            print(" ",end=" ")
        for tm in range(10,me,-1):
            print("*",end=" ")
        for hm in range(10,me,-1):
            print("*",end=" ")
        print()
    print("\t\t *")
def cchal12():
    #Triangle using for loop with set of numbers

    for i in range(1,7):
        for l in range(7,i,-1):#For spaces
            print(" ",end=" ")
        for m in range(i,0,-1):#left triangle/reverse number
            print(m,end=" ")
        for p in range(2,i + 1):#right triangle
            print(p,end=" ")
        print()#to print from top to bottom
def cchal13():
    #Christmas Tree
    for me in range(2,6,1):
        for u in range(0,7):
            print(" ",end=" ")
        for i in range(6,me,-1):
            print(" ",end=" ")
        for tm in range(3,me):
            print("▀",end=" ")
        for hm in range(2,me,1):
            print("▀",end=" ")
        print()    
    for mem in range(1,3,1):
        for yt in range(0,7):
            print(" ",end=" ")
        for iy in range(0 - 1,mem,1):
            print(" ",end=" ")
        for tm in range(2,mem,-1):
            print("▀",end=" ")
        for hm in range(3,mem,-1):
            print("▀",end=" ")
        print()    
    for new in range(2,9,1):
        for c in range(12,new,-1):
            print(" ",end=" ")
        for mn in range(2,new,1):
            print("▀",end=" ")
        for po in range(1,new):
            print("▀",end=" ")
        print()
    for ntw in range(2,10,1):
        for jk in range(12,ntw,-1):
            print(" ",end=" ")
        for pn in range(1,ntw):
            print("▀",end=" ")
        for un in range(2,ntw):
            print("▀",end=" ")
        print()
    for hty in range(2,13,1):
        for rtr in range(12,hty,-1):
            print(" ",end=" ")
        for uy in range(1,hty):
            print("▀",end=" ")
        for ign in range(2,hty):
            print("▀",end=" ")
        print()
    for yty in range(1,7):
        for me in range(1,9):
            print(" ",end=" ")
        for wer in range(1,9):
            print("",end="▀")

        print()
def cchal14():
    #All odd will calculated and skip if even


    name = input("Whats your name: ")

    odd = 0
    numb = "" #More like a list
    ys = True

    while ys == True:
        num = eval(input("Put a number: "))
        if num % 2 == 1:
            print("Odd Detected")
            odd += num
            numb += str(num) + "," #Will add coma each number
            continue
        elif num == 0: #Will stop if user input 0
            print("Bye Bye")
            break
        else:
            print("Even detected")
            print("Skipping")
            continue
    print(f"Total of all odd number: {odd}")
    print(f"All odd number: {numb}")

def cchal15():
    #Anime list
    #Using list and while loop
    print("Anime Title List")

    anime = [] #empty list
    mn = True   

    while mn == True:
        num = input("Put a Title of an Anime: ")
        print("Anime Added to the your Anime List")
        anime.append(num) #all title that put will go to the list
        if num == "exit": #stopper
            print("All done,You are now exiting!! ")
            anime.pop() #will remove the string exit to list
            break    #to stop the loop

    print(f"Here All the Title of your Anime: ") 
    for r in anime:     #will print all the anime u putted,from up to down
        print(f"- {r}")
        
def cchal16():
    
    import os
    import json
    os.system('cls') #To clear the menu when putted something
    diction = {} #empty dictionary

    while True: 
        print("Select From options Below\nA - Add Information\nB - Print all\nc - Search Information\nd - Delete Information\ne - To Edit File\nF - Export Data\nG - Import Data\nP - Exit") #Menu List

        new = input("Typing...       ").lower() #lower so the putted letter can be lower case or upper case

        if new == "a":
            print("Adding Information")
            ky = input("Key to call for the Information: ")
            fname = input("Input Student First Name: ")
            lname = input("Input Student Last Name: ")
            course = input("Input Course: ")
            email = input("Input Student Email: ")

            diction[ky] = [fname,lname,course,email] #It will add multiple data to the dictionary 
            print("Data saved")
            os.system('cls')
            continue
        elif new == "c":
            os.system('cls')
            srch = input("key of the information: ")

            for a in diction.keys():# for q in diction(): #Search, For loop will help us connect to the dictionary
                if  srch in diction.keys(): #it will check if  the Input keys is in the dictionary
                    print("record Found")
                
                    print("Record Info")
                    print("--------------------------")
                    for y in diction[srch]:
                        print(f": {y}")
                    print("--------------------------")
                else:
                    print("Information not Found")  
                break
            continue
        elif new == "b":
            os.system('cls')
            for a,p in diction.items(): #for loop it will manage all the information in the dictioanary
                print(f"STUDENTS ID {a}: STUDENT RECORD {p}") #it will now print all the items in dictionary
            continue
        elif new == "d":
            os.system('cls')
            print("Delete existing record")
            srch = input("key of the information: ")
            if  srch in diction.keys(): #it will check if  the Input keys is in the dictionary
                

                print("Record deleted")
                print("--------------------------")
                for i in diction[srch]:
                        print(f": {i}")

                diction.pop(srch)
                print("Record deleted")
            else:
                print("Information cannot found") 
            continue
        elif new == "e":
            os.system('cls')
            print("Record Modification")
            
            srch = input("key of the information: ")

            for a in diction[srch]:
                        print(f": {a}")

            
            fname = input("Input Student First Name: ")
            lname = input("Input Student Last Name: ")
            course = input("Input Course: ")
            email = input("Input Student Email: ")

            diction[srch][0] = fname
            diction[srch][1] = lname
            diction[srch][2] = course
            diction[srch][3] = email

            print("Data Updated")

            continue
        elif new == "f":
            os.system('cls')
            with open("diction.json","w") as new_file:
                json.dump(diction,new_file, indent=4)
                print("Data Exported")
            continue
        elif new == "g":
            os.system('cls')
            with open("diction.json","r") as new_file:
                diction_json = json.load(new_file)

            diction = diction_json
            print("Data Imported")

            continue
        elif new == "p":
            print("Exiting")
            break
        else:
            print("Invalid Input")
        


