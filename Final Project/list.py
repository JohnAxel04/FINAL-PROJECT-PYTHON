

def Activity23():
    nm = ['apple','donut','coconut','mango','grapes']
    print(nm)
    me = input("What fruit you want to add? ")
    nm.append(me)
    print(nm)

    

def Activity23_1():
    mi = 'John Axel De Leon'
    print(f"{mi} The Name in the List")
    for u in mi:
        print(u)    #Will print my name from j to n
    print("\nReversed\n")
    for q in mi[::-1]:  #will print my name in reverse from n to j
        print(q)

def Activity23_2():
    nm = ['apple','donut','coconut','mango','grapes']
    print(nm)
    for i in nm:
        print(f"{i}  in the basket")    #all fruits one by one with 'in the basket' at the last