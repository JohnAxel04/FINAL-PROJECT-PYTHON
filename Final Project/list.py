def Activity21():
    fruits = []

    fruits.append('apply')
    fruits.append('mango')
    fruits.append('orange')
    fruits.append('banana')
    print(fruits)

def Activity22():
    pl = ['js','html','css','python']

    pl.insert(2,'sdf')
    print(pl[0])
    print(pl[1])
    print(pl[2])
    print(pl[-1])

def Activity23():
    nm = ['apple','donut','coconut','mango','grapes']
    nm.append('orange')   #add an item to the last of the list
    print(nm)
    nm.pop()    #remove the last item
    print(nm)
    nm.insert(0,'Monggo')   #add item in dif position
    print(nm)
    for i in nm:
        print(f"{i}  in the basket")    #all fruits one by one with 'in the basket' at the last

    mi = 'John Axel De Leon'
    for u in mi:
        print(u)    #Will print my name from j to n
    print("\nReversed\n")
    for q in mi[::-1]:  #will print my name in reverse from n to j
        print(q)
