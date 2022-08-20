"""Activity: Python Function Practice Part 4"""

__author__ = "Caroline Konrad"


#Find the max of 3 numbers

def max_num(x, y, z):
    return max(x, y, z)

print(max_num(1, 7, 3))
print(max_num(9, 5, 4))
#Multiply all numbers in a list
def mult_list(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

print(mult_list([1, 2, 3, 4]))
print(mult_list([5, 7, 2, 1]))

#Reverse a string
def rev_string(myString):
    return myString[::-1]

print(rev_string('Hello world'))
print(rev_string('This is my string'))

#Check whether a number falls in a given range
def num_within(myInt, lower, upper):
    if myInt > lower and myInt < upper:
        return True
    else:
        return False

print(num_within(5, 3, 7)) #True
print(num_within(6, 7, 3)) #False

#Prints out first n rows of Pascal's triangle
def pascal(n):
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n>=1

pascal(2)
pascal(4)