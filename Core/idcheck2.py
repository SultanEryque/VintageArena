#!usr/bin/env python
#This program checks whether a certain string can be used as a identifier or
#is a keyword

#importing module
import string
import keyword

alphas = string.ascii_letters + '_'
nums = string.digits
alphanums = alphas + nums
keys = keyword.kwlist

print ("Welcome to Identifier Checker Ver 2.0")
inp = input("Enter an identifer: ")


if inp not in keys:
    if inp[0] not in alphas:
        print ("Error! 1st letter should be alphabetic")
    else:
        for otherchar in inp[:]:
            if otherchar not in alphanums:
                print ("other chars should be alphanumeric")
        else:
            print ("Good for an Identifier")
else:
    print (inp, "is a keyword, can not be used as an identifier!")

