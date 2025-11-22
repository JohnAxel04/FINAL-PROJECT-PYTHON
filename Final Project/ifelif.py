def Activity10():	#Grocery
	print("---------------------------\n        Welcome \n---------------------------")
	name = input("What is your Name? ")
	item = input("What item(Fish/Pork): ")
	many = eval(input("How many(1-10): "))
	fr = eval(input("How much? "))
	pwd = input("are you PWD or Senior(Yes/No): ")
	equal = many * fr * .05
	man = many * fr
	more = man - equal

	print("---------------------------")
	if pwd.lower() == "yes":
		print("Hello", name, "\nItem: ",item, "\nQuantity: ",many,"\nPrice each: ",fr,"\nTotal: ",man ,"\nDiscount:",equal,"\nTotal w/discount: ",more)
	else:
		print("Hello", name, "\nItem: ",item, "\nQuantity: ",many,"\nPrice each: ",fr,"\nTotal: ",man ,"\nDiscount:","\nTotal w/discount: ",man)


def Activity11():
    #Temperature checker
    tmp = eval(input("what temp is it now? "))

    if tmp <= 0:
        print("the temp is freaking cold")
    elif tmp >= 1 and tmp <= 20:
        print("The temp is cold")
    elif tmp >= 21 and tmp <= 30:
        print("The temp is lookwarm")
    elif tmp >= 31 and tmp <= 40:
        print("The temp is warm")
    elif tmp >= 41 and tmp <= 50:
        print("The temp is hot")
    elif tmp >= 51:
        print("The temp is boiling hot")
    else:
        print("error")