def square_digits():
    num = str(list(num))
    
    new_arr = []
    for i in num:
        new_arr.append(int(i))

    res_str = ""
    for i in new_arr:
        squared = i ** 2
        res_str += str(squared)
    return int(res_str)

"""
.incert - ჩასმა  
.append -  დამატება
lower() - სტრინგში ყველა ასო დაპატარავდება
capitalize() - სტრინგის პირველი ასო დიდი იქნება დანარჩენი პატარა
upper() - სტრინგის ყველა ასო დიდი იქნება
find() - პოილობს სტრინგს და აბრუნებს მის ინდექსს
list.incert(2,"risi chasmac gvinda") - ამატებს სიას კონკრეტულ ინდექსზე მნიშვნელობას
list.pop(ინდექსი) -შლის ელემენტს ინდექსის მიხედვით"""



# def opposite(number):
#     return -number
