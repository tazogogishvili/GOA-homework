"""დავალება1) 
შექმენით სია, რომელშიც შეიტანთ რიცხვებს 0-იდან 20-ის ჩათვლით (ხელით ჩაწერეთ, ციკლის გარეშე),ბოლოს დაპრინტეთ მთლიანი სია.
Create an array which will include numbers from 0 to 20 (write it manually, without loops), then print whole array.
"""

# # ვქმნით კოლექციას სადაც ვინახავთ ინფორმაციას 0-იდან 20-ჩათვლით
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# # ვბეჭდავთ სიას
# print(nums)



# ##########################################################################################################################################

# """დავალება2) შექმენით ახალი სია, რომელშიც შეიტანთ ლუწ რიცხვებს წინა სიიდან. ბოლოს დაპრინტეთ ეს სია.
# Create a new array, which will include even numbers from the first array. Then print this new array."""

# # ვქმნიტ სიას სადაც ვინახავთ ლუწ რიცხვებთ 0-იდან 20-ის ჩათვლით
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # ვბეჭდავთ სიიდან ლუწ რიცხვებს

# print(nums[1:20:2])



###########################################################################################################################################


"""დავალება3) შექმენით ახალი სია, შემდეგ 50-იდან 100-მდე ამ სიაში შეიტანეთ ყველა რიცხვი (დასერჩეთ python array append). ბოლოს დაპტინტეთ თქვენთვის სასურველი სიის ნაწილი უარყოფითი index-ების საშუალებით.
Create an array, then add numbers from 50 to 100 to it. In the end, print the part of this array with negatives indexes.
"""

# list = []

# for i in range(50, 100):
#     list.append(i)
# print(list)




###########################################################################################################################################


"""დავალება4) მომხმარებელს შეეკითხეთ ორი მთელი რიცხვი, შემდეგ ამ ორი ცვლადიდან for ციკლში უმცირესი ჩასვის start-ის,
 ხოლო უდიდესი end-ის პოზიციაზე, step არ გინდათ. ახლა ჩაურთეთ if statement და დაპრინტეთ მარტო ხუთის ჯერადები.
Ask user for two inputs and store them as variables, their type has to be int. Then use for loop, use lower number from this two variables as start, Higher number as end, you do not need step. After that, you'll have to use if statement to only print multiples of five."""

# num1 = int(input("enter firs number: "))
# num2 = int(input("enter second number: ")) 

# lower_num = min(num1,num2)

# print("numbers from", lower_num, "to", max(num1,num2),":")
# for i in range(lower_num, max(num1,num2) + 1):
#     print(i)

###########################################################################################################################################





"""დავალება5) შექმენით ახალი სია. შემდეგ მომხმარებელს შეეკითხეთ მისი ასაკი და თუ ასაკი 18-ზე მეტი იქნება,
 შეეკითხეთ მას სახელი. მეორე ინფუთის შემდეგ სახელი შეიტანეთ სიაში და დაპრინტეთ ის."""


# ვადეკლარირებთ int ტიპის ცვლადს სადაც მომხმარებელს შეუძლია შემოიტანოს ტავისი ასაკი
age = int(input("enter youre age: "))

list = []


# თუ მომხმარებლის შემოტანილი ასაკი მეტია 18-ზე მომხმარებელმა შეძლოს სახელის შემოტანა
if age > 18:
    name = input("what is youre name: ")
    # list.append(age)
    # list.append(name)
    list = ["youre name is", name, "youre age is", age]
    print(list)
# სხვა შემოთხვევაში დაიბეჭდოს რომ მომხმარებელი არასრულწლოვანია
else:
    print("you are not adult!")
