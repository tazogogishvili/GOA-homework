# declaring variable name and give it variable valuve
# 10% discount
book_Harry_Potter = 25
book_Maze_Runner = 10
book_Lord_of_the_Rings = 30
book_The_Alchemist = 40
book_The_Da_Vinci_Code =20

# 20% discount
book_The_Hobbit = 15
Dream_of_the_Red_Chamber = 35
Don_Quixote = 45
The_Bible = 55
Moby_Dick = 60


# declare variable for discount

discount1 = 10
discount2 = 20


# declaring variables 10% discount
price_after_discount0 = book_Harry_Potter - book_Harry_Potter * discount1 // 100
price_after_discount1 = book_Maze_Runner - book_Maze_Runner * discount1 // 100
price_after_discount2 = book_Lord_of_the_Rings - book_Lord_of_the_Rings * discount1 // 100
price_after_discount3 = book_The_Alchemist - book_The_Alchemist * discount1 // 100
price_after_discount4 = book_The_Da_Vinci_Code - book_The_Da_Vinci_Code * discount1 // 100


# declaring variables 20% discount
price_after_discount5 = book_The_Hobbit - book_The_Hobbit * discount2 // 100
price_after_discount6 = Dream_of_the_Red_Chamber - Dream_of_the_Red_Chamber * discount2 // 100
price_after_discount7 = Don_Quixote - Don_Quixote * discount2 // 100
price_after_discount8 = The_Bible - The_Bible * discount2 // 100
price_after_discount9 = Moby_Dick - Moby_Dick * discount2 // 100

# print created variables 
# 10% discount


print("discount 10%")
print("Harr Potter->",price_after_discount0,str('gel'),"  Maze Runner->",
      price_after_discount1,str('gel'),"  Lord of the Rings->",price_after_discount2,
      str('gel'),"  The Alchemist->",price_after_discount3,str('gel'),
      "  The Da Vinci Code->",price_after_discount4,str('gel'))

print()

# 20% discount


print("discount 20%")
print("book The Hobbit->",price_after_discount5,str('gel'),"  Dream of the Red Chamber->",
      price_after_discount6,str('gel'),"  Don Quixote->",price_after_discount7,
      str('gel'),"  The Bible->",price_after_discount8,str('gel'),"  Moby Dick->",
      price_after_discount9,str('gel'))