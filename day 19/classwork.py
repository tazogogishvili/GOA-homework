
"""ბატონი ლუკას ახსნილი დავალება"""

# def even_numbers(numbers):
#     even_numbers_list = []

#     for num in numbers:
        
#         if num % 2 == 0:
#             even_numbers_list.append(num)
    
#     return even_numbers_list

# list1 = [1,2,3,4,5,6,7,8,9,10]

# print(even_numbers(list1))

#########################################################################

# def max_numbers(numbers):
#     return max(numbers)

# print(max_numbers([23,1,11,42,6,323,5]))


# დაწვრილებით

# def largest_number(numbers):
#     max_number = numbers[0]

#     for num in numbers:
#         if max_number < num:
#             max_number = num
    
#     return max_number

# numbers = [2,3,6,9,2,1323,6]

# print(largest_number(numbers))




"""შექმენით პროგრამა სადაც მომხმარემელს შემოვატანინებთ თუ რამდენი რიცხვის შეტანა
სურს სიაში შემდეგ შექმნიან სიას for ციკლში input-ით შეეკიტხეთ რიცხვი და შეიტტანე სიაში ბოლოს სიის ჯამი დააბრუნეთ"""




# def sum_of_numbers():
#     iteracion = int(input("enter number for iteracion: "))
#     sum = 0
#     numbers = []
    
#     for num in range(iteracion):
#         user_num = int(input("enter some number: "))
#         sum = sum + user_num
#         numbers.append(user_num)
        
#     return sum



# def even_numbers():
#     iteracion = int(input("enter number for iteracion: "))
#     numbers = []
    
#     for num in range(iteracion):
#         user_num = int(input("enter some number: "))
#         if user_num % 2 == 0 and user_num > 10:
#             numbers.append(user_num)
        
#     return numbers


# print("sum of numbers =",sum_of_numbers())
# print("even numbers for list", even_numbers())



"""შექმენით ფუნქცია რომელსაც გადაცემთ სიას და ამ კონკრეტულ სიას დაალაგებს ზრდადებით"""


# def incremental_numbers(list1):
#     for index in len(list1):
#         if min(index) > list1:
        

#     print(list1, index)

# list = [3,1,5,7,4,8]

# incremental_numbers(list)


"""შექმენით ფუნქცია რომელსაც გავუწერთ 2 პარამეტრს. პირველი პარამეტრი მართკუთხედის სიგრძე მართკუთხედის სიმაღლე
საბოლოოდ დაააბრუნეთ მისის ფართობი  """


# def rectangle_area():
#     rectangle_length = int(input("enter rectangle length: "))
#     rectangle_width = int(input("enter rectangle width: "))
#     area = rectangle_length * rectangle_width
#     return area

# print("rectangle area =", rectangle_area())