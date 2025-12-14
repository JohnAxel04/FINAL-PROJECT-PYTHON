def activity5():
    print("Type and Add")
    xel = eval(input("Put something(1-100): "))
    print("The Data type of something is", type(xel))

    answer = 6 + xel
    print("The answer is ",answer)

def Activity6():
    x = eval(input("Number Please(1-100): "))
    y = eval(input("Number Please(1-100): "))
    a = x + y
    b = x - y
    c = x * y
    d = x / y

    print("The sum of", x, "and" ,y,"is", a)
    print("The difference of", x, "and" ,y, "is", b)
    print("The product of", x, "and" ,y, "is", c)
    print("The quotient of", x, "and" ,y, "is", d)
    print(x, "exponent by", y, "is" ,x**y)
    print("The remainder of", x, "and" ,y, "is", x%y)
    print("The floor division of", x, "and" ,y, "is", x//y)

def Activity7():
    ox = 5

    print("The Value of it is", ox)

    ox *= 5

    print("The Value of it is", ox)

    ox /= 50	
    print("The Value of it is", ox)

def Activity8():
    utangko = 1000
    perako = 500

    print((utangko) <= (perako))

    cash = 50
    payment = 80

    print((cash) <= (payment))

def Activity9():
    put = "email"
    pit = 4321

    print((put == "email") and (pit == 4321))
    print((put == "email") or (pit == 5321))
    print(not((put == "emaill") or (pit == 5321)))


