#Function to print binary number for the input decimal using recursion
def decToBin(n):
    if n > 1:
        #divide with integral result
        #(discard reminder)
        decToBin(n//2)

    print(n%2,end = "")

#Python code to demonstrate naive method using loop
def Binary(n):
    binary =""
    i = 0
    while n > 0 and i<=8:
        s1 = str(int(n%2))
        binary = binary + s1
        n/=2
        i = i+1
        d = binary[::-1]
    return d

#function returning binary string
def Bin(n):
    """using the buil-in function bin():
        reduce the time required to code
        and also avoid the hassle may encountered in above two methods"""
    s = bin(n)
    #removing the "0b" prefix
    s1 = s[2:]
    return s1

#Driver code
if __name__ == '__main__':
    decToBin(8)
    print("\r")
    decToBin(18)
    print("\r")
    decToBin(7)


    print("\r")
    print("The binary representation of 100(using loop) is :",end="")
    print(Binary(100))

    print("\r")
    print("The binary representation of 100(using bin()) is :",end="")
    print(Bin(100))

