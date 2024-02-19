#Declaring the names of each book

First_Book = "The Birth of Gio Gagnidze"
Second_Book = "The Ascending of Gagnidze"
Third_Book = "The Downfall of Giogi"
Fourth_Book = "The revenge of Gio Gagnidze"
Fifth_Book = "The Marriage of Gio Gagnidze"
Sixth_Book = "The Death of Gio Gagnidze"
Seventh_Book = "The son of Gio Gagnidze"
Eighth_Book = "The Return of the king"
Nineth_Book = "The ressurection of Gagnidze"
Tenth_Book = "Why Gagnidze is the best crew leader"
#Declaring the price of the books
First_BPrice = 100
Second_BPrice = 250
Third_BPrice = 690
Fourth_BPrice = 420
Fifth_BPrice = 69420
Sixth_BPrice = 42069
Seventh_BPrice = 80085
Eighth_BPrice = 1000
Nineth_BPrice = 5000
Tenth_BPrice = 1000000000
#Declaring the variables for discounts
discount1 = 10
discount2 = 20
#Declaring the new values after the discount is applied
#book 1
Book1_After_discount1 = First_BPrice - First_BPrice * discount1 / 100
#book 2
Book2_After_discount1 = Second_BPrice - Second_BPrice * discount1 / 100
#book 3
Book3_After_discount1 = Third_BPrice - Third_BPrice * discount1 / 100
#book 4
Book4_After_discount1 = Fourth_BPrice - Fourth_BPrice * discount1 / 100
#book 5
Book5_After_discount1 = Fifth_BPrice - Fifth_BPrice * discount1 / 100
#book 6 , we now switch to discount 2 (20%)
Book6_After_discount2 = Sixth_BPrice - Sixth_BPrice * discount2 / 100
#book 7
Book7_After_discount2 = Seventh_BPrice - Seventh_BPrice * discount2 / 100
#book 8 
Book8_After_discount2 = Eighth_BPrice - Eighth_BPrice * discount2 / 100
#book 9
Book9_After_discount2 = Nineth_BPrice - Nineth_BPrice * discount2 / 100
#book 10
Book10_After_discount2 = Tenth_BPrice - Tenth_BPrice * discount2 / 100

#Now we print them all
#Printing the books with discount 1 of 10
print("The first book will be",Book1_After_discount1,"after the discount.")
print("The second book will be",Book2_After_discount1,"after the discount.")
print("The third book will be",Book3_After_discount1,"after the discount.")
print("The fourth book will be",Book4_After_discount1,"after the discount.")
print("The fifth book will be",Book5_After_discount1,"after the discount.")
#Printing the books with discount 2 of 20
print("The sixth book will be",Book6_After_discount2,"after the discount.")
print("The seventh book will be",Book7_After_discount2,"after the discount.")
print("The eighth book will be",Book8_After_discount2,"after the discount.")
print("The nineth book will be",Book9_After_discount2,"after the discount.")
print("The tenth book will be",Book10_After_discount2,"after the discount.")
#finished homework