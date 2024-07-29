


"""ანაცვლებს ყველა სტრინგს გაწერილი პარამეტრების მიხედვით"""

# word = "tazogogishvili"

# # word2 = word.replace("i", "g")


# print(word.replace("g", "e"))



#                      #რა 
#                     #სიმბოლოც
#                     #უნდა 
#             #სიტყვა #ჩანაცვლდეს    #რა სიმბოლოთი უნდა ჩანაცვლდეს
# def my_replace(word, replace_char, input_char):
#     changed_word = ''

#     for char in word:
#         if char == replace_char:
#             changed_word = changed_word + input_char
#         else:
#             changed_word = changed_word + char

#     return changed_word

# print(my_replace("tzoooie", "o", "g"))




########################################################



# print("tazo".count("a"))

"""ალგორითმი ქაუნთის"""

# "tamazaaaaaaa".count("a") --> result:9

# def my_count(collection, count_element):
#     count = 0

#     for element in collection:
#         if element == count_element:
#             count = count + 1
#     return count
    

# print(my_count("tamazaaaaaaa", "a"))


########################################################


# print("few".find("e"))

"""ჩემი დაწერილი ალგორითმი"""
# def my_find(collection, value):
#     sum = 0
#     for index in collection:
#         if index == value:
#             return sum
#         else:
#             sum = sum + 1
#     return -1        

# print(my_find([1,2,4,5,], 0))


# """ბატონი ლუკას დაწერილი ალგორითმი"""
# def my_find(collection, value):
    
#     for index in range(len(collection)):
#         if collection[index] == value:
#             return index
#     return -1

# print(my_find([1,2,4,5,6,7,8], 8))



"""დაცალებები:
1) შექმენით პროგრამა სადაც გექნებათ მოცემული სია
   და უნდა დავითვალოთ ამ სიაში ლუწი რიცხვები"""



# def sum_of_collection(collection):
#     list1 = []
#     for i in collection:
#         if i  % 2 == 0:
#             list1.append(i)
#     return list1

# print(sum_of_collection([1,2,3,4,4,4,1,2]))



"""2) შექმენით პროგრამა სადაც გექნებათ მოცემული სია ან სტრინგი
      ხოლო ამ კოლექციებში ლუწ ინდექსებზე მყოფი ჩაანაცვლეთ
      სხვა სიმბოლოთი ან სხვა რიცხვით
"""


# def my_replace_index(collection, change_char):
#     result = ''
#     for index in range(len(collection)):
#         if index % 2 == 0:
#             result = result + change_char
#         else:
#             result = result + collection[index]
#     return result

# print(my_replace_index("tazooo", "k"))




"""3)იპოვეთ სიაში ბოლო ლუწი რიცხვის ინდექსი"""

# def find_last_even(numbers_list):
#     for i in range(len(numbers_list) -1, -1, -1):
#         if numbers_list[i] % 2 == 0:
            
#             return numbers_list[i]

# print(find_last_even([1,2,3,4,5]))


# print([1,2,3,4,5,6][::-1])


"""ჯოინ მეთოდი"""

# print("+".join(["1","2","3"]))

# def my_join(join_str, strings_list):
#     joined_elements = ''

#     for word in strings_list:
#         joined_elements += word + join_str
#     return joined_elements[:-1]
    

            

# print(my_join("+",["1","2","3"]))



"""
გადმოგეცემათ რიცხვთა სია ფუნქციაში თქვენი დავალებაა ამ სიაში მყოფი ლუწი რიცხვები შეაერთოდ + მეშვეობით 
და დააბრუნოთ საბოლოო შედეგად სტრინგი    შესატანი[1,2,3,4]

საბოლოო შედეგი: "2+4"

გაითვალისწინეთ ის რომ თუ სიაში მხოლოდ ერთი ლუწი რიცხვია დაბრუნდეს პირდაპირ

ხოლო თუ არარის შიაში ლუწი რიცხვი დააბრუნეთ ცარიელი სტრინგი


""" 




# def find_even_numbers(list1):
#     result = ''
#     for number in list1:
#         if number % 2 == 0:
#             result += str(number) + "+"
#         else:
#             return list1
#     return result[:-1]
    
# print(find_even_numbers([1,3,5,7,9]))
