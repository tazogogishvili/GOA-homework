""" გადაიმეორეთ ყველაფერი რაც ვისწავლეთ while ციკლამდე და გააკეთეთ 5-5 მაგალითი"""



"""N1"""
# შევქმენით num ცვლადი სადაც მომხმარებელი სემოიტანს რიცხვს ერთიდან ათამდე
# num = int(input("Write a number from one to ten :"))

# მომხმარებელს ვაწვდით ინფორმაციას თუ რა მოხდება რიცხვის შემოტანის შემდეგ
# print("Your written number will be filled from one to ten")

# while num <= 10:
#     print(num)
#     num = num + 1


"""N2"""
# # ვადეკლარირებთ ცვლადებს while იტერაციისტვის
# i = 0
# sum  = 0

# while i <= 100:
#     print(i)
#     i = i + 1
#     sum = sum + i

# # ვიძახებთ sum ცვლადს ანუ ერთიდან ასის ჩათვლით რიცხვთა ჯამს
# print(sum)


"""N3"""
# # ვადეკლარირებთ num ცვლადს სადაც მომხმარებელი შემოიტანს რიცხვს 
# num = int(input("Please enter number: "))

# while num / 2 == 0:
#     num = num / 2
#     print(num)
# if num != 2:
#     print("This number is not divisible by 2")


"""N4"""
# ვადეკლარირებთ ინტეჯერის ტიპის ცვლადს რომელსაც ვანიჭებთ მნიშვნელობას 0
# i = 0

# სანამ i ცვლადი ასის ჩათვლით დიაპაზონში ნაკლებია ასზე დაპრინტოს
# i ცვლადის მნიშვნელობა და გასარდოს ყოვრლ დაპრინტვაზე 5-ით
# while i in range(100 + 1):
#     print(i)
#     i = i + 5


"""N5"""
# i = 0
# num = 240

# while i < num:
#     print(i)
#     i = i + 20

##################################################################################################################################





"""ყველაფერი რაც ვისწავლეთ"""

##################################################################################################################################


# ვადეკლარირებთ ცვლადებს სადაც მომხმარებელი შემოიტანს თავის მინიმალურ ინფორმაციას

# name = input("Enter youre name: ")
# print("Your name is", name)


# # ცადეკლარირებთ string ტიპის ცვლადს სადაც მომხმარებელს შემოაგ მისი გვარი


# lastname = input("Please enter youre lstname: ")
# print("Youre lastname is", lastname)


# # ვადეკლარირებთ integer ტიპის ცვლადს სადაც მომხმარებელი შემოიტანს მის ასაკს

# age = int(input("Enter youre age: "))

# # თუ მომხმარებელის ასაკი აღემატება თვრამეტს გამოიტანოს რო ის სრულწლოვანი წინააღმდეგ შემთხვევაში არასრლწლოვანი

# if age > 18:
#     print("You are adult")
# else:
#     print("You are not an adult!")


##################################################################################################################################




"""ვაკეტებთ ფასდაკლებას მანქანებზზე"""

##################################################################################################################################


# # ვადეკლარირებთ int ტიპის ცვლადებს მანქანის ფასზე

# mercedes_price = 4000
# bmw_price = 2000
# audi_price = 1000


# # ვქმნით int ტიპის ცვლადებს სახელად ფასდაკლება და ვანიჭებთ მნიშვნელობას 10% 20%

# discount1 = 10
# discount2 = 20


# # ცადეკლარირებთ მანქნის ფასდაკლების ცვლადებს სადაც ვაკეთებთ 10% ფასდაკლებას

# mercedes_discount1 = mercedes_price - mercedes_price * discount1 // 100
# bmw_discount1 = bmw_price - bmw_price * discount1 // 100
# audi_discount1 = audi_price - audi_price * discount1 // 100


# # ცადეკლარირებთ მანქნის ფასდაკლების ცვლადებს სადაც ვაკეთებთ 20% ფასდაკლებას

# mercedes_discount2 = mercedes_price - mercedes_price * discount2 // 100
# bmw_discount2 = bmw_price - bmw_price * discount2 // 100
# audi_discount2 = audi_price - audi_price * discount2 // 100


# # ვპრინტავთ დადეკლარირებულ ცვლადებს ფასდაკლების გარეშე

# print("Mercedes price", str(mercedes_price) + "$")
# print("BMW price", str(bmw_price) + "$")
# print("Audi price", str(audi_price) + "$")
# print()

# # ვპრინტავთ 10% ფასდაკლებას მანქანებზე

# print("Car prices after 10% discount")
# print()
# print("Mercedes price", str(mercedes_discount1) + "$")
# print("Bmw price", str(mercedes_discount1) + "$") 
# print("audi price", str(audi_discount1) + "$")
# print()

# # ვპრინტავთ 20% ფასდაკლებას მანქნებზე

# print("Car prices after 20% discount")
# print()
# print("Mercedes price", str(mercedes_discount2) + "$")
# print("Bmw price", str(bmw_discount2) + "$")
# print("Audi price", str(audi_discount2) + "$")


##################################################################################################################################




"""ვწერთ კოდს სადაც მომხმარებელს შეეძლება ივარჯიშოს"""

##################################################################################################################################

# # ვადეკლარირებთ str ტიპის ცვლადს სახელად name

# name = input("Enter youre name: ")
# print("hello", name)


# # აზიდვების მიზანი

# pushup_target = 200
# yes = (input("Are you rady for pushups? yes or no!: "))

# #
# if yes == "yes":
#     print("You are chad, Pushup target",pushup_target)
# else:
#     print("You are not chad!!!! you are LOSER")


# pushup_made = int(input("how many pushup you made? "))

# if pushup_made >= pushup_target:
#     print("now you are strong:DD")
# else:
#     print("you are not strong")


##################################################################################################################################






##################################################################################################################################

# num1 = int(input("dawere raime ricxvi: "))
# num2 = int(input("dawere kidev raime ricxvi: "))


# if num1 > num2:
#     print("pirveli ricxvi metia meore ricxvze",num1)
# else:
#     print("meore ricxvi metia pirvel ricxvze",num2)

##################################################################################################################################


"""Timer: დაწერეთ პროგრამა, რომელიც ითვლის 10-დან 1-მდე, დაბეჭდავს თითოეულ რიცხვს და შემდეგ დაბეჭდავს "დრო ამოიწურა"."""

# timer პროგრამა


# ვადეკლარირებთ str ტიპის ცვლადს რომელსაც ვანიჭებთ მნიშვნელობას 10
# i = 10

# while i > 0:
#     print(i)
#     i = i - 1

# print("time out!")


##################################################################################################################################



##################################################################################################################################

"""რიცხვების ჯამი: დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვებს განუწყვეტლივ,
 სანამ ისინი არ შეიყვანენ 0-ს. შემდეგ დაბეჭდეთ ყველა შეყვანილი რიცხვის ჯამი."""


# num = int(input("enter first number: "))
# sum = 0 
# i = 0

# while num != i:
#     sum = sum + num 
#     num = int(input("enter number: ")) 
# print("sum of numbers",sum)    
        

##################################################################################################################################


"""პაროლის შემოწმება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას.
 განაგრძეთ კითხვა, სანამ სწორი პაროლი არ იქნება შეყვანილი. დავუშვათ, რომ სწორი პაროლი არის "12345678"""

# name = input("enter youre name: ")
# pas = 12345678
# user_pas = int(input("enter youre password: "))

# while user_pas != pas:
#     user_pas = int(input("please try again: "))
# if pas == user_pas:
#         print("Wellcome",name)


##################################################################################################################################


"""ლუწი რიცხვები: დაწერეთ პროგრამა, რომელიც ბეჭდავს ყველა ლუწ რიცხვს 0-დან 20-მდე while ციკლის გამოყენებით."""

# დავადეკლარირეთ int ტიპის ცვლადი რომელსაც მივანიჭეთ მნიშვნელობა 0
# i = 0

# while i in range (20):
#     print(i)
#     i = i + 2

##################################################################################################################################


"""დადებითი რიცხვები: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს უწყვეტად შეიყვანოს დადებითი რიცხვები,
 სანამ ისინი უარყოფით რიცხვს არ შეიყვანენ. შემდეგ დაბეჭდეთ ყველა შეყვანილი დადებითი რიცხვის ჯამი"""

# sum_of_positive_numbers = 0

# while True:
#     number = float(input("Enter a positive number (or a negative number to stop): "))
    
#     if number < 0:
#         break
#     else:
#         sum_of_positive_numbers += number

# print("Sum of all positive numbers entered:", sum_of_positive_numbers)


##################################################################################################################################


"""შეამოწმეთ ლუწია თუ კენტი: დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს და ბეჭდავს ლუწია თუ კენტი."""


# num1 = int(input("Please enter number: "))

# if num1 % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd")

##################################################################################################################################


"""ტემპერატურის კლასიფიკაცია: შექმენით პროგრამა, რომელიც მომხმარებელს სთხოვს ტემპერატურას ცელსიუსში.
 შემდეგ დაბეჭდეთ ცხელი (> 30°C), თბილი (20-30°C) ან ცივი (<20°C)."""


# # ვადეკლარირებთ ცვლადებს

# temp = int(input("Write the temperature: "))

# hot_temp = 30
# warm_temp = range(20, 30)
# cold_temp = 20


# if temp > 30:
#     print("თhe weather is nice today: ")

# if temp == warm_temp:
#     print("It's warm today")


# if temp < cold_temp:
#     print("It's cold today")



"""ასოების შეფასება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოცდის ქულას.
  შემდეგ დაბეჭდეთ მათი ასოების შეფასება შემდეგი სკალის მიხედვით: A (90-100), B (80-89), C (70-79), D (60-69), F (< 60)."""


# user_result = int(input("How many points did you get?: "))

# for a in range(90,100 + 1):
#     if user_result == a:
#         print("You got the highest score")
       

# for b in range(80, 90):
#     if user_result == b:
#         print("You got a high score")


# for c in range(70, 80):
#     if user_result == c:
#         print("You got an average score")

# for d in range(60, 70):
#     if user_result == d:
#         print("You got a low score")

# for c in range(0, 60):
#     if user_result == c:
#         print("You did not pass the score threshold")




""""
შეამოწმეთ გაყოფა: შექმენით პროგრამა,რომელიც მომხმარებელს სთხოვს რიცხვს შემდეგ დაბეჭდეთ იყოფა თუ არა 2-ზე,3-ზე ან ორივეზე.
რიცხვების შედარება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს ორ რიცხვს და შეადარებს მათ."""



# num = int(input("Enter first number: "))

# while num % 3 != 0:
#     print("This number is not divisible by 3")
#     break
# else:
#     if num % 2 == 0:
#         num = int(input("Enter first number: "))
#     else:
#         print("This number is not divisible by 2")



# num1 = int(input("Entr firs number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print("The first number is greater than the second:")
# else:
#     print("The second number is greater than the first")




"""combined (გამოიყენეთ while loop და if statement):

რიცხვის გამოცნობა: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს
რიცხვი (მაგ., 5, ეს რიცხვი თქვენ აირჩიეთ). განაგრძეთ კითხვა, სანამ არ გამოიცნობენ სწორად."""


# num = 5
# User_selected_number = int(input("Choose a number: "))
# while num != User_selected_number:
#     User_selected_number = int(input("Choose number again"))
#     if User_selected_number == num:
#         print("Congratulations, you guessed the number 5")
#         print("You won")


"""რიცხვების შემოწმება: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს.
 სანამ ეს რიცხვი არ იქნება ლუწი, შეეკითხეთ მომხმარებელს თავიდან"""


# num = int(input("enter first number: "))

# while num % 2 != 0:
#     num = int(input("enter first number: ")) 
# else:
#     print("This number is even")


"""რიცხვების კლასიფიკაცია: შექმენით პროგრამა, სადაც 50-იდან 100-ის ჩათვლით
 გამოიტანთ კენტ რიცხვებს. ციკლის გარეთ შექმენით ჯამის ცვლადი, სადაც დაემატება ციკლის ის რიცხვები,
   რომლებიც მეტია 75-ზე. ბოლოს დაპრინტეთ ამ ცვლადის მნიშვნელობა"""




# sum = 0
# sum1 = 0
# for i in range(50, 100, 3):
#     sum += i
#     sum1 += sum
#     print(i)
# print(sum)
# print(sum1)


"""რიცხვების შედარება: მომხმარებელს შეეკითხეთ რიცხვი. სანამ ის ნაკლები იქნება მასზე 20-ით დიდ რიცხვზე,
 დაპრინტეთ ის და მასზე მოახდინეთ იტერაცია 1-ით."""

# num = int(input("enter first number: "))

# while num < 20:
#     num = num + 1
#     print(num)
    

"""
სახელის გამოცნობა. შექმენით ცვლადი სადაც იქნება შენახული თქვენი სახელი.
 მომხმარებელს შეეკითხეთ სახელი და სანამ თქვენსას არ შემოიტანს თავიდან შეეკითხეთ"""


# my_name = "tazo"
# user = input("enter name: ")

# while my_name != user:
#     user = input("enter name again: ")
# else:
#     print("shen gamoicani saxeli")
 






