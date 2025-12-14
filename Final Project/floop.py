
def Activity12():
    for u in range (1 , 11):
        print(u, "hello world")

def Activity13():
    p = 0

    for u in range(1 ,11 ,1):
        cm = eval(input("Put any number i will add: "))
        p += cm
        print(p ,"New value of",cm)
    print("total", p)

def Activity14():
    for u in range(20 ,0 ,-1):
        print(u ,"Hiii")
    print("String Formatting")
    a = "John"
    b = "Axel"
    c = "De_Leon"
    print(f"My name is {a} {b} {c}")
    #Get the summation of all odd numbers
def Activity15():
    end = 0

    for me in range(1,11):
        nb = eval(input("Put number"))
        if nb % 2 == 1:
            end += nb
    print(f"The summation of all number is {end}")

def Activity16():
    for i in range(1,11):
        print(i,end=" ")

def Activity17():
    for me in range(1,11):
        for u in range(1,11):
            print(u,end=" ")
        print()

def Activity18():
    for me in range(1,21):
        for u in range(1,me):
            print(u,end=" ")
        print()
def Activity19():
    for u in range(1,11):
        for i in range(1,u,1):
            print("*",end="")
        print()
def Activity20():
    for me in range(1,11):
        for u in range(1,me,1):
            print("#",end=" ")
        for th in range(10,me,-1):
            print("o",end=" ")
        print()
        
def Activity21():
    #while loop

    me = True

    while me == True:
        moon = input("(Yes or No): ")

        if moon.lower() == "yes":
            print("COntinue")
            continue
        elif moon.lower() == "no":
            print("Stop")
            break
        else:
            print("Error input")
            continue