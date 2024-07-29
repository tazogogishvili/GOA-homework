"""ვქმნით ფუნქციას რომელსაც გავუწერტ for ციკლს"""



# def func(name):
#     for i in range(int(input("enter first number: "))):
#         print(i)

# func()

# def func():
#     name = input("enter youre name: ")
#     for i in range(int(input("enter firs number: "))):
#         print(name)

# func()
    

# def func(x):
#     for i in range(x):
#         print("tazo")

# func(23)




"""შექმენით 4 ფუქნცია: 1)შეკრება, 2)გამოკლება, 3)გამრავლება 4)გაყოფა"""


print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divison")

operacion = int(input("enter operacion: "))
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

def add(num1, num2):
    return num1 + num2

def subtract(num1 , num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

if operacion == 1:
    print(add(num1, num2))
elif operacion == 2:
    print(subtract(num1, num2))
elif operacion == 3:
    print(multiply(num1, num2))
else:
    print(division(num1, num2))
