"""1)
Write a program that takes asks user for number (use input). If number is even, print that number is even.
 Else print that number is not even, also print next even number, for example if input is 15, print 16.
"""
 
# num = int(input("enter first number: "))

# if num % 2 == 0:
#     print("this number is even ")
#     num + 2
#     print("this number is aslo even",num)
# else:
#     print("thisn number is not even")

#############################################################################################################################################


"""
Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best".
 Also print the count of incorrect passwords."""


# sum = 0
# password = input("enter password: ")


# while password != "GOA":
#     password = input("enter password again: ")
#     sum = sum + 1
# if password == "GOA":
#     print("Password is correct")

# print("Number of incorrect passwords",sum)


#############################################################################################################################################


"""Write an algorithm that takes a string as input and returns True if first character of that string is "G"."""


# name = input("enter youre name: ")




#############################################################################################################################################



"""Ask user for five names (use input five times). Add all of them in one list and print only first three names."""


# #  ვადეკლარირებთ ცარიელ სიას
# list1 = []


# for i in range(5):
#     name = input("please enter youre name: ")
#     list1.append(name)

# # დავბეჭდოთ სია 
# print(list1[:3])

#############################################################################################################################################




"""Write an algorithm that checks if a given number is prime or not 
(prime number has only two divisors - გამყოფი) Use a for loop for this task."""


# # ვადეკლარირებთ int ტიპის ცვლადს სახელად num1 სადაც მომხმარებელს შეუძლია შემოიტანოს ინფორმაცია
# num1 = int(input("enter firs numbet: "))

# # თუ მომხმარებლის შემოტანილი რიცხვი არ იყოფა სამზე უნაშთოთ მაშინ ტერინალში დაიბეჭდოს 
# # რომ რიცხვი არის this number is prime
# if num1 % 3 != 0:
#     print("this number is prime")

# # სხვა შემთხვევაში დაიბეჭდოს რომ This number is not prime
# else:
#     print("This number is not prime")
    


#############################################################################################################################################

"""Create a while loop that prints numbers from 10 to 0 (10-იდან 0-მდე)."""

# # ვადეკლარირებთ int ტიპის ცვლადს სადაც მომხარელს შემოაქვს რიცხვი
# num = int(input("Write a number between 10 and 0: "))
# # სანამ მომხმარებლის მიერ შემოტანილი რიცხვი მეტია ან უდრის ნულს დაიპრინტოს შემოტანილ რიცხვის -1
# while num >= 0:
#     print(num)
#     num -= 1


# num1 = int(input("Write the number between 10 and 0: "))
# while num1 <= 10:
#     print(num1)
#     num1 += 1

#############################################################################################################################################


"""Implement a simple calculator that takes two numbers and an operator (+, -, *, /)
 as input from the user and performs the corresponding operation. Bonus task if you want,
   it's not necessary - add degree (ხარისხი), use ** operator for it."""


# print("Please select the operation.")    
# print("1 - Add")    
# print("2 - Subtract")
# print("3 - Divide")     
# print("4 - Multiply")

# operacion = int(input("please enter choice: "))

# num1 = int(input("enter first number for operacion: "))
# num2 = int(input("enter second number for operacion: "))
# sum = 0

# if operacion == 1:
#     sum = num1 + num2
#     print(num1, "+", num2, "=", sum)

# elif operacion == 2:
#     sum = num1 - num2
#     print(num1, "-", num2, "=", sum)

# elif operacion == 3:
#     sum = num1 / num2
#     print(num1, "/", num2, "=", sum)

# if operacion == "4": 
#     sum = num1 * num2
#     print(num1, "x", num2, "=", sum)



#############################################################################################################################################


"""Ask user to enter name and print the last character of that string."""

# # ვადეკლარირებთ ცვლადს სახელად name 
# name = input("What is your name?:  ")
# print(name[-1])


#############################################################################################################################################


""""Using for loop, ask user for number. Then create a list which will have even numbers in next range:
 from 0 to user's number. At last, print out whole list. """

# # ვადეკლარირებთ ცარიელ სიას
# list1 = []
# # ვადეკლარიებთ ცვლადს სახელად num სადაც მომხმარებელს შეუძლია შემოიტანოს ინფორმაცია
# num = int(input("enter first number: "))
# # i-ი დიაპაზონში მომმხმარებლის მიერ შემოტანილ რიცხვში
# for i in range(num):  
#   num = int(input("enter number: "))
#   list1.append(num)
# # ვბეჭდავთ სიას 
# print(list1)


#############################################################################################################################################



"""Ask user for whole number. Then create a factorial for this number and print it out 
(If you don't know what a factorial is, google it)"""



print("write the number and find out factorial")

num1 = int(input("enter first number: "))
factorial = 1
if num1 < 0:
    print("this number is not factional")
elif num1 == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num1 + 1):
        factorial *= i

print(factorial)