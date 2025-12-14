def Activity22():
    import random



    num = random.randint(1,10)

    tries = 0
    we = True

    while we == True:
        g = int(input("What number u guess(1-10): "))
        tries += 1

        if g == num:
            print("Congratulation")
            print(f"the number is {num}")
            print(f"YOu online took {tries} tries")
            break

        else:
            print("youre wrong")
            continue

def activity24():
    def greeter(name):  #own function number 1
        print(f"Hello {name}, How are you? ")

    def summ(x):    #own function number 2
        total = 0
        for y in range(x, 0, -1):
            total += y  #all the number counted will go to total 
        print(f"The of {x} is {total}") #print the total or sum of the numbers
    greeter("ewrqwe")
    greeter("ewrw")
    greeter("ewwerwerqwe")
    greeter("ewrqwerwerwerwe")


    summ(15)
    summ(3)
    summ(5)
    summ(12)
def Activity25():
    def activity1():
        nam = input("What is youre name: ")
    def activity2():
        age = eval(input("What is youre age: "))
    def activity3():
        address = input("Where do you live: ")
    def activity4():
        gen = input("Male/Female -> ")

    name  = input("Whats is your name: ")

    print(f"Welcome {name} to my File compiler")

    t = True

    while t == True:
        print("Select a program")
        print("A - Activity1\nB - Activity2\nC - Activity3\nD - Activigty 4\nE - Exit")

        new = input("What program would you like to run: ").lower()

        if new == "a":
            activity1()
            continue
        elif new == "b":
            activity2()
            continue
        elif new == "c":
            activity3()
            continue
        elif new == "d":
            activity4()
        elif new == "e":
            print("Thank you for sunshine")
            break
        else:
            print("error input")