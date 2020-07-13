N1 = input("Enter N1: ")
N2 = input("Enter N2: ")
 
OP = {"1":"Addition", "2": "Subtraction", "3":"Multiplication", \
      "4":"Division", "5":"Modulus", "6":"Exponetiation"} 

print (OP)
opr = input("Enter corresponding integer operation: ")
opr = int(opr)
def do_math(N1, N2):

    N1 = int(N1)
    N2 = int(N2)
   
    if (opr == 1):
        return N1 + N2
    elif (opr == 2):
        return N1 - N2
    elif (opr == 3):
        return N1 * N2
    elif (opr == 4):
        return N1 / N2
    elif (opr == 5):
        return N1 % N2
    elif (opr == 6):
        return N1 ** N2
    else:
        print ("Invalid Selection!") 

ans = do_math(N1, N2)
print (ans) 

