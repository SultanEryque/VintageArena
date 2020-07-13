#The progran determines whether a year is a leap year.
#leap year is divisible by four and not 100 bt by 400

x = input("Enter year: ")

def leap(x):
    x = int(x)
    if (x % 4 == 0) or (x % 400 == 0):
        return "Its a leap year"
    else:
        return "Its not a leap year"
    endif

lp = leap(x)
print (lp)
