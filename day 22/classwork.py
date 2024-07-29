# def grow(arr):
#     sum = 1
    
#     for num in arr:
#         sum = sum * num
    
#     return sum

# list1 = [1, 2, 3]
# print(grow(list1))

############################################

"""გავამარტივოთ ეს კოდი"""


# def descending_order(num):
#     res_str = ""
#     num_str = str(num)
#     reversed_str = ""
#     res_arr = [] 
   
#     for i in range(len(num_str)-1, -1, -1):
#         reversed_str += num_str[i]
   
#     for i in reversed_str:
#         res_arr.append(i)
#     res_arr.sort(reverse = True)
#     return int("".join(res_arr))
