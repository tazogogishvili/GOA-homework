# def find_short(s):
#     words_list = s.split(" ")
#     min_length = len(words_list[0])
    
#     for word in words_list:
#         if min_length > len(word):
#             min_length = len(word)
#     return min_length

#####################################################################

# def get_middle(s):
#     word_length = len(s)
#     index = word_length // 2
    
#     if word_length % 2 == 0:
#         return s[index - 1] + s[index]
    
#     return s[index]