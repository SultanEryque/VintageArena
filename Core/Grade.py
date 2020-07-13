#Finds grades according to score
#90-100: A
#80-89: B
#70-79: C
#60-69: D
#60 and below: F

print("Welcome to Grade/Average Finder")
scores = []

#main function
def grade():

    x = input("Enter score: ")
    x = int(x)

    if (x >= 90) and (x <= 100):
        print ("A")
    elif (x >= 80) and (x <= 89):
        print ("B")
    elif (x >= 70) and (x <= 79):
        print ("C")
    elif (x >= 60) and (x <= 69):
        print ("D") 
    else:
        print ("F")

    scores.append(x)    

def avg():
    ln = len(scores)
    if ln > 1:   
        total = sum(scores)
        Avg = total / ln
        print ("The Average is ", Avg)
    else:
        print("Error! Can not find mean of a single unit")
def disp():
    print (str(scores))

def menu():
    prompt = """
(A)dd
(M)ean
(V)iew
(Q)uit
Enter choice: """

    done = 0
    while not done:

        chosen = 0
        while not chosen:
            try:
                choice = input(prompt)[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice == 'q'         
            if choice not in 'amvq':
                print ("Error!", choice, "invalid choice")
            else:
                chosen = 1

        if choice == 'q': done = 1
        if choice == 'a': grade()
        if choice == "m": avg()
        if choice == 'v': disp()

if __name__ == '__main__':
    menu()

