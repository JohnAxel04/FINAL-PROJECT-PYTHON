def Activity19():
    ur = int(input("Put any number that will add(0 to quit): "))

    op = 0

    while not ur == 0:
        op += ur
        ur = int(input("Put another number again: "))

    print(f"Times up all of number got {op}")

