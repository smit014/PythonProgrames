"""Grocery List Total: Given a dictionary of grocery items and their prices,
calculate the total cost of a shopping list."""


def AddtoCart():
    while True:
        Check = input("Want to add  item(y/n): ")
        if Check == "y":
            itemName = input("Enter item name : ")
            UserCart[itemName] = Grocary[itemName]
        elif Check == "n":
            break
    print("Items are added to cart")


def RemovefromCart():
    while True:
        Check = input("Want to Remove  item(y/n): ")
        if Check == "y":
            removeItem = input("Enter item name, Which you wnat to Remove : ")
            del UserCart[removeItem]
        elif Check == "n":
            break
    print("Items are removed from cart")


def ViewCart():
    print("You Added this items in your Cart :")
    for item in UserCart:
        print(item)


def CheckItemPrice():
    itemName = input("Enter item name : ")
    print("Your Item Price is :", Grocary[itemName])


def CalculateTotalCost():
    print("Total cost :", sum(UserCart.values()))


def GroceryStore():
    for i in Grocary:
        print(i, ":", Grocary[i])


list_item = [
    "Apple",
    "Milk",
    "Banana",
    "Cereal",
    "Eggs",
    "Bread",
    "Cheese",
    "Cherry",
    "Pineapple",
    "Chocolate",
]
list_price = [2.99, 1.99, 3.49, 4.99, 1.79, 2.29, 3.19, 4.49, 2.49]
Grocary = dict(zip(list_item, list_price))
UserCart = {}
while True:
    print("\t******* GROCARY SHOP *******")
    print("\t 1.View items in Shop")
    print("\t 2.View items in your cart")
    print("\t 3.Add items in your cart")
    print("\t 4.Check cart items price")
    print("\t 5.Remove item from your cart")
    print("\t 6.Know about your Total Cost")
    print("\t 7.Want to Leave the shop")
    Choice = int(input("How can i Help You :"))
    if Choice == 1:
        GroceryStore()
    elif Choice == 2:
        ViewCart()
    elif Choice == 3:
        AddtoCart()
    elif Choice == 4:
        CheckItemPrice()
    elif Choice == 5:
        RemovefromCart()
    elif Choice == 6:
        CalculateTotalCost()
    elif Choice == 7:
        print("Thanks for shopping,Welcome Back")
        break
    else:
        print("Invalid Choice !!")
