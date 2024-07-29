"""
Write a function that takes a list of numbers as input and returns the sum of all the numbers in the list."""


# # ვქმნით ფუნქციას რომელიც მომხმარებლის მიერ შემოტანილ რიცხვებს ამატებს სიას
# def user_input_numbers():
#     list1 = []
# # ვამატებთ sum ცვლადს რომელიც ითვლის ჯამს
#     sum = 0
# # ფუნქციას ტანში ვუწერთ for ციკლს დიაპაზონში 6
#     for i in range(6):
#         nums = int(input("enter numbers: "))
#         list1.append(nums)
#         sum += nums
# # ვბეჭდავთ sum ჯამს
#     print(sum)
    
# # ვიძახებთ ფუნქციას
# user_input_numbers()


########################################################################################################################################


"""
Write a function that takes a list of strings as input and returns a new
list containing only the strings that have a length greater than 5.
# """
# # ვქმნით ფუქნციას 
# def str_len_5():
#     numbers = []
# # ვქმნით ფუნქციაში for loop-ს  
#     for i in range(7):
#         user_input_numbers = input("enter nimbers: ")
#         if len(user_input_numbers) <= 5:
#             numbers.append(user_input_numbers)
#     print(numbers)

# # ვიძახებთ ფუნქციას
# str_len_5()



########################################################################################################################################


"""Write a function that takes a list of numbers as input and returns
   a new list containingonly the even numbers from the original list."""


# def list_of_numbers():
#     main_list = []
#     even_list = []
#     for i in range(5):
#         num = int(input("enter number: "))
#         main_list.append(num)
#         if num % 2 == 0:
#             even_list.append(num)     
    
#     print("numbers list =", main_list)
#     print("even numbers list =", even_list)
          
# list_of_numbers()

########################################################################################################################################


"""Write a function that takes a list of numbers as input and returns the largest number in the list.
"""

# # ვქმნიტ ფუნქციას სადაც მომხმარებლის მიერ მაქსიამლურ შემოტანილ რიხვს დავპეჭდავთ სიიდან
# def largest_number():
#     list1 = []
#     for i in range(4):
#         num = int(input("enter number: "))
#         list1.append(num)
#     print(max(list1))


# largest_number()


########################################################################################################################################

"""Write a function that takes a list of strings as input and returns
 a new list containing only the strings that start with the letter 'a'."""

# # ვქმნით სიას სადაც თუ მომხმარებელი შემოიტანს str რომელიც იწყევა ა-ზე დაემატოს სიას
# def list_start_a():
#    names = []
# # for loop-ით ვაკეთებთ გამეორებას ხუთჯერ
#    for i in range(5):
#       user_input_name = input("enter name and name add in list: ")
#       if user_input_name[0] == "a":
#          names.append(user_input_name)
# # ვბეჭდავთ სიას
#    print(names)

# # ვიძახებთ შექმნილ ფუნქციას
# list_start_a()

########################################################################################################################################

"""Write a function that takes a list of numbers as input and returns a new list containing the square of each number.
"""


# def square_of_numbers():
#    default_numbers = []
#    square_numbers = []
#    for i in range(5):
#       num = int(input("enter some number: "))
#       default_numbers.append(num)
#       num *= num
#       square_numbers.append(num)
#    print("default numbers =",default_numbers)
#    print("numbers of squere",square_numbers)
   


# square_of_numbers()

########################################################################################################################################



"""Write a function that takes a list of strings as input and returns a new list containing the lengths of each string."""

# # ვქმნიტ ფუნქციას 
# def list_return_len():
#    full_list = []
#    len_list = []
#    for i in range(4):
#       input_for_list = input("type some word: ")
#       full_list.append(input_for_list)
#       len_list.append(input_for_list)
#    print(full_list)
#    print(len(len_list[i]))

# # ვიძახებთ ფუნქციას
# list_return_len()


########################################################################################################################################


"""Write a function that takes a list of numbers as input and returns the sum of all the numbers that are greater than 10."""

# # ვქმნიტ ფუნქციას რომელიც იტვლის რიცხვების ჯამს
# def sum_numbers():
#    numbers = []
#    sum = 0
#    for i in range(7):
#       num = int(input("enter some number: "))
#       numbers.append(num)
#       sum += num
#    if sum >= 10:
#       numbers.append(sum)
#    print(numbers)
#    print("sum of numbers:",sum)  

# # ვიძახებთ შექმნილ ფუნქციას
# sum_numbers()



########################################################################################################################################

