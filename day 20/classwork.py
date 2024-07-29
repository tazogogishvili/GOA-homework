
# def even_index(lastname):
#     even_index_chars = []

#     for index in range(len(lastname)):
#         if index % 2 == 0:
#             even_index_chars.append(lastname[index])

#     return ''.join(even_index_chars)
    
# lastname = input("please enter your lastname: ")

# print(even_index(lastname))






def even_index(lastname):
    
    result = ''
    for index in range(len(lastname)):
        if index % 2 == 0:
            result = result + lastname[index]

    return result
    
lastname = input("please enter your lastname: ")

print(even_index(lastname))
