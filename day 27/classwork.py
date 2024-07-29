
# def my_range(start,end,step):
#     numbers = []

#     while start < end:
#         numbers.append(start)
#         start = start + step
        
#     return numbers

# print(my_range(10, 20 ,1))


"""
დავალება: შექმენით პროგრამა სადაც ბოლოდან პირველ ოთხის ჯერად რიცხვს გამოიტანთ სიიდან
მაგ სიაში კი 10-იდან 50-ის ჩათვლით უნდა იყოს რიცხვები
"""

# numbers = []

# for i in range(10, 50 + 1):
#     numbers.append(i)

# def func(numbers):
#     for index in range(len(numbers) -1, -1 , -1):
#         if numbers[index] % 4 == 0:
#             return numbers[index]
        
# print(func(numbers))


"""შექმენით range მსგავსი ფუნქცია სადაც მესამე არგუმენტი იქნება მომხმარებლის მიერ შეტანილი აგრეთვე კომენტარით აღწერეთ retuen"""


# def my_range(start,end,step=1):
#     numbers = []

#     while start < end:
#         numbers.append(start)
#         start += step
#     return numbers

# print(my_range(1,8))



"""შექმენიტ ფუნქცია სახელად filter მისი პირველი პარამეტრი იქნება კოლმექცია მეორე კი
 მნიშვნელობა თქვენი დავალებაა რო მკოლექციიდა ნამოიღოთ ეგ კონკრეტული მნიშვნელობა და დააბრუნოთ ის"""


# def filter(numbers,char):
#     nums = []
#     print("this is default list")
#     print(numbers)
#     for i in numbers:
#         if i != char:
#             nums.append(i)
#     print("this is new list")
#     return nums
        
# nums = [1,5,3,4,5,6,3,7,3,2]

# print(filter(nums,3))


"""შექმენით ფუნქციას რომელსაც გადაცემთ მარტკუტხა სამკუთხედის კათეტებს, თქვენი დავალებაბა აირს ის რომ დააბრუნოთ ჰიპოტენუზა"""


# ?????????

# def hypotenuse(first_angle, second_angle):

#     c = first_angle * first_angle + second_angle * second_angle
#     print(c)

# hypotenuse(35,33)


"""შექმენით ფუნქცია რომელსაც გადაეცემა თქვენი სახელი თუ სახელის სიგრძე აღემატება ხუთს დაააბრუნეთ მისი upercase
ვარიანტი. ხოლო თუ ნაკლებია ან ტოლი დააბრუნეთ capitalize ვარიანტი"""


# def len_name(name="guest"):
#     if len(name) > 5:
#         return name.upper()
#     else:
#         return name.capitalize()


# print(len_name("taz0"))




# def greet(name="Guest"):
#     print("welcome", name)

# greet()
# greet("tazo")