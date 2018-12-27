"""List, being an essential python container is used  in day-day programming
and also in web-development.
Knowledge of its operation is necesarry.

Let's see all thediffernt ways of accessing the last elemetn of a list.
"""
#Method 1: very naive method

#Python code to demonstrate accessing
#last element of lig

#initializing list
test_list = [1,4,5,6,7,8,3,9]

import os
os.system('cls')
#printing original list
print("The original list is :"+str(test_list))

#using loop to print last element
for i in range(0,len(test_list)):
    if i == (len(test_list) -1):
        print("The last element of list using loop :"+str(test_list[i]))

#using reverse method to print the last element
test_list.reverse()
print("The last element of list reverse :"+str(test_list[0]))
    
test_list.reverse()
#using -1 index to print last list element
print("The last element of list using [-1] :"+str(test_list[-1]))

#using pop() index to print last list element
print("The last element of list using pop() :"+str(test_list.pop()))





















