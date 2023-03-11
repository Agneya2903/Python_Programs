#Python Program for factorial of a number
'''
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter any number to find its factorial: "))
print("The Factorial of ", num ,"is ",factorial(num))
'''

#--------------------------------------------------------------------------------

#Maximum of two numbers in Python
'''def maximum(a,b):
    if a >= b:
        return a
    else:
        return b
a =45
b= 48
print(maximum(a,b))

#Alternate Method
c= 47
d= 88
print(max(c,d))
'''
#----------------------------------------------------------------------------------------------------------

#Python Program To Add Two Numbers
'''num1 = int(input("Enter the number:- "))
num2 = int(input("Enter the number:- "))
sum = num1+num2
print("The Addition of {0} and {1} is {2}".format(num1,num2,sum))'''