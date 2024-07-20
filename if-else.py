a = int(input("enter a number on your choice"))
b = a % 2

if b == 0:
    print('the number is even')
    if a > 5:
        print('Greater than 5')
    else:
        print("smaller than 5")
else:
    print("the number is odd")


## Write a code to check if the number is postive/negative
p = int(input("Enter a number on your choise"))
if p > 0:
    print("It is  a postive number")
elif p < 0:
    print("It is a negative number")
else:
    print("the number is Zero")
## write a code to print greatest number among three user input
a = int(input("enter a number on your choise"))
b = a % 2

if b == 0:
    print('the number is even')
    if a > 5:
        print('Greater than 5')
    else:
        print("smaller than 5")
else:
    print("the number is odd")


p = int(input("Enter a number on your choise"))
if p > 0:
    print("It is  a postive number")
elif p < 0:
    print("It is a negative number")
else:
    print("the number is Zero")



num1 = int(input("Enter a number on first choice num1: "))
num2 = int(input("Enter a number on second choice num2: "))
num3 = int(input("Enter a number on third choice num3: "))

if (num1 >= num2) & (num1 >= num3):
    largest = num1
elif (num2 >= num1) & (num2 >= num3):
    largest = num2
else:
    largest = num3
print("enter greatest number is", largest)



