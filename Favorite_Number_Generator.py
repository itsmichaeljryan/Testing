# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:30:34 2020

@author: mjrya
"""

MR = '4'
MM = '11'

##Make the program restart with a loop function
while True:
    
##Get the user to input a name
    Text = input("Please type the name of who you want to search for, or press Q to quit the program. ")

##Use the program to check the name that was input
    if Text == "Michael":
        print("Michaels favorite number is " + MR)
    elif Text == "Miranda":
        print("Mirandas favorite number is " + MM)
    elif Text == "q":
        print("Goodbye")
        break
    else:
        print("I dont know that person")

