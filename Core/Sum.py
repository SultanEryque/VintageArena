x = input("Enter number: ")
y = input("Enter another number: ")

def add(x, y):       
    sm = x + y
    return "The sum is", sm

def mult(x, y):
    ml = int(x) * int(y)
    return "the product is ", ml

res = add(x, y)
prod = mult(x, y)

print (prod)
print (res)


