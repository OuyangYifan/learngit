#python using 2d arrarys list the right way
#ref: www.geeksforgeek.org/python-using-2d-arrays-lists-the-right-way
# Python 3 program to demostrate working
# of method a and method b for  generation of 2d array

rows,cols = 5,5
#method 2a
arr_2d = [[0]*cols]*rows

#let change the first element of the fist row to 1
#and print the array
arr_2d[0][0] = 1

#check if the two row of 2d arr refer to the same object,i.e shallow list
if arr_2d[0] is arr_2d[1]:
    print("Warning: proboble inappropriate usage of shallow list.")
    print("""Current way to declare a 2d array:\r
           [ [0] * cols ] * rows""")
for row in arr_2d:
    print(row)


#method 2b
arr_2d = [[0 for i in range(cols)] for j in range(rows)]

#let change the first element of the fist row to 1
#and print the array
arr_2d[0][0] = 1

#check if the two row of 2d arr refer to the same object,i.e shallow list
if arr_2d[0] is arr_2d[1]:
    print("Warning: proboble usage of shallow list.")
else:
    """tracing out errors caused by  inappropriate usage of shallow list 
    is difficult"""
    print("""Recommend way to declare a 2d array:\r
           [[0 for i in range(cols)] for j in range(rows)]""")


for row in arr_2d:
    print(row)


















