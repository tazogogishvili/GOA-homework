"""
1. Manual Sum Function: Create a function called manual_sum that iterates over list and adds
   their sum in a variable, then returns variable. Use for loop for this task.
"""

# # ვქმნით ფუნქციას სახელად manal sum  ეს ფუნქცია დაითვლის რიცხვთა ჯამს
# def manual_sum(list1):
#     sum = 0
# # გადავუვლით სიას
#     for i in list1:
#         sum += i
#     return sum


# numbers = []

# for i in range(6):
#     num = int(input("enter umber: "))
#     numbers.append(num)
# print(numbers)


# print(manual_sum(numbers))


"""
2. Manual Max Function: Define a function named manual_max that iterates through list,updating a 
variable with the maximum value, then returns the maximum value found. Use for loop for this task.
"""


# def manual_max(number_list):
#     max_number = 0

#     for i in number_list:
#         if max_number < i:
#             max_number = i

#     return max_number

# print(manual_max([1,2,3,15,5,6,7,7,4,2,9,8]))


"""
3. Manual Min Function: Define a function named manual_min that iterates through list, updating
a variable with the minimum value, then returns the minimum value found. Use for loop for this task.
"""

# def manual_min(numbers_list):
    
#     min_number = numbers_list[0]

#     for i in numbers_list:
#         if min_number > i:
#             min_number = i
    
#     return min_number

# print( manual_min([3,7,1,2,9,3]))



"""
4. Manual Len Function: Develop a function named manual_len that iterates through list, counting
 each element, and returns the count as the length of the list. Use for loop for this task.
 """


# def manual_len(numbers_list):
#     index = 0
#     for i in numbers_list:
#         index += 1
#     return index


# print(manual_len([3, 2, 3, 2, 3, 2, 3, 2]))



"""Copy function of reduce: define a function named manual_reduce that takes a list as input,
 then create an empty list named copied_list to store the copied items inside it. Then use for
loop to loop over each item in the original list, append them to the copied_iterable list In the
end, return the copied_iterable after iterating through all items.

finally demonstrate the usage of the manual_reduce function by creating an original list, making 
a copy of it, and printing both the original and copied lists."""


# def manual_reduce(numbers_list):
#     numbers = []

#     for i in numbers_list:
#         numbers.append(i)

#     return numbers_list,numbers


# print(manual_reduce([10,20,30,40,50]))