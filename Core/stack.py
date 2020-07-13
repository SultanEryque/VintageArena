#! usr/bin/env python

stack = []

def pushit():
    stack.append(input("Enter a string: "))

def popit():
    if len(stack) == 0:
        print ("Cannot pop an empty list")
    else:
        print ("Removed ", stack.pop())

#uncomment all function for deque function addition
#def deq():
    #if len(stack) == 0:
        #print ("Cannot deque from an empty list")
    #else:
        #print ("Dequed: ", stack.pop(0))

def viewstack():
    print (str(stack))

def showmenu():
    prompt = """
p(U)sh
p(O)p
(V)iew
(Q)uit
Enter choice: """

    done = 0
    while not done:

        chosen = 0
        while not chosen:
            try:
                choice = input(prompt)[0]
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print ("You picked: ", choice)
            if choice not in 'uovq':
                print ("Invalid Option, Try Again")
            else:
                chosen = 1

        if choice == 'q': done = 1
        if choice == 'u': pushit()
        if choice == 'o': popit()
        if choice == 'v': viewstack()
if __name__ == '__main__':
    showmenu()
