x = input("Enter Cents, max:100: ")
x = int(x)

def dollars(x):
    if (x / 25 >= 1):
        y = x / 25
        y = int(y)
        mod = x % 25

        return y, "quarter(s) and", mod, "penny(s)"

    elif (x / 10 >= 1):
        y = x / 10
        y = int(y)
        mod = x % 10

        return y, "dime(s) and", mod, "penny(s)"

    elif (x / 5 >= 1):
        y = x / 5
        y = int(y)
        mod = x % 5

        return y, "nickel(s) and", mod, "penny(s)"

    else:
        return x, "penny(s)"
        
dol = dollars(x)
print (dol)
