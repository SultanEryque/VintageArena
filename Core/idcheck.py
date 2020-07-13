#!usr/bin/env python

import string

alphas = string.ascii_letters + '_'
nums = string.digits

print ("Welcome to the Identifier Checker Ver 1.0")
print ("Testees should atleast be 2 chars long")
inp = input("Enter identifier to be tested: ")

if len(inp) > 1:

    if inp[0] not in alphas:
        print ("Error! 1st letter must be alphabetic")

    else:
        for otherchar in inp[1:]:
            if otherchar not in alphas + nums:
                print("Error! rest of the chars should be alphanumeric")
                break
        else:
            print ("Good for an Identifier")
