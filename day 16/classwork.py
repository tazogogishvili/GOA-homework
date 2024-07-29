
# # ვადეკლარირებთ str ტიპის ცვლადს

# name = input("please enter your name: ")
# lastname = input("enter your lastname: ")

# list1 = [name[0], lastname[0]]

# print(list1)

# print(name[0]+"."+lastname[0])


"""დავალება: შექმენით ორი სია, უნდა გქონდეთ ორივე განსხვავებული ზომის. lef ფუნქციის გამოყენებით და გაიგეთ მატი სიგრძე"""


# cars = ["mercdes", "ford", "toyota", "BMW", "pagani", "lexsus", "mazda", "volkswagen"]

# GOA_grups = [11, 16, 17, 5, 22]

# print("Car quanity:",len(cars,)," GOA grups quantity:",len(GOA_grups))




"""დავალება2: len ფუნქციის გამოყენებით გამოიტანეთ თქვენი გვარის ბოლო ასო"""


# name = input("enter your name: ")
# lastname = input("enter your lastname: ")

# list1 = [name, lastname]

# print("The last letter of the last name is:",lastname[len(lastname) -1])



"""დავალება3: გააერთიანეთ ერთი სია მეორე სიასთან"""


cars = [
    "mercdes",
    "ford", 
    "toyota",
    "BMW", 
    "pagani", 
    "lexsus", 
    "mazda",
    "volkswagen"]

GOA_grups = [11, 16, 17, 5, 22]

cars.append(GOA_grups)
print(cars)
