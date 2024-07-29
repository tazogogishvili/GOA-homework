"""რაც კი ვისწავლეთ შედარების ოპერატორები, მათემატიკური ოპერატორები,
მექანიკური მონაცემთა ტიპის შეცვლა და ავტომატური ყველაფერზე ივარჯიშეთ და ნამუშევარი ატვირთე რაზეც ივარჯიშეთ
3) ისწავლეთ სინტაქსი არა მკაცრი შედარებების მაგალითად მეტიან ან ტოლია"""
 

# declaring numbers for mathematical equations

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter the third number: "))
num4 = int(input("enter fourth number: "))
num5 = int(input("enter the fifth number: "))


# Call the created variables

print(num1 + num2 * num4 - num2 / num5 % num3)
print(num1 + num5)
print(num5 - num3)
print(num2 * num2)
print(num3 / num4)
print(num4 // num1)
print(num1 & num2)

# printing func

print(str(num2) + str(num1))
print(int("100") + 200)
print(float(5.55) - float(3.5))
print(num4 > num2)
print(43 > 35) #true
print(30 == 19.0) #false
print(10 == 10) #true
print(25 < 10) #false
print(20 % int(1.7))
print(30 % 600)