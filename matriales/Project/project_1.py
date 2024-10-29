# import random
from prettytable import PrettyTable
#
# u = "omar"
# p = "1111"
#
#
# def new_func(u, p):
#     while True:
#         x = input("Enter Username: ")
#
#         if x == u:
#             y = input("Enter Password: ")
#
#             if y == p:
#                 s = random.randrange(10000,1000000)
#                 print("Verification code is: ", s)
#                 while True:
#                     l = int(input("Enter Verification code: "))
#                     if l == s:
#                         print("Wilcom")
#                         break
#                     else:
#                         print("Incrorrect Verification code. Try again.")
#
#                 break
#             else:
#                 print("incorrect password")
#                 break
#         else:
#             print("incorrect user name")
#             break
#
#
# new_func(u, p)



""" Products in our company
project
"""
products = [
    {"name":"water","price":80.00,"Quantity":1200},
    {"name":"soda","price":130,"Quantity":1200},
    {"name":"chips","price":75,"Quantity":1200},
    {"name":"bread","price":45,"Quantity":1200},
    {"name":"Eggs","price":65,"Quantity":1200}
]
table = PrettyTable()
table.field_names = ["name","price","Quantity"]
for product in products:
    table.add_row([product["name"],product["price"],product["Quantity"]])
    print(table)
#

total_discounted_price = 0
def application(products, total_discounted_price):
    while True:
        product_name = input("Enter priduct name : ").lower()

        if product_name not in map (lambda x: x["name"].lower(), products):
            print("product not found in the table. please enter a valid product.")
            continue
        quntity_required = float(input("Enter Quantity Required: "))
        product = next(p for p in products if p["name"].lower() == product_name)
        if quntity_required > product["Quantity"]:
            print("Insufficient quantity. please enter a new quantity.")
            continue
        discounted_quantity = quntity_required // 250
        discount_percentage = 5.0 * discounted_quantity
        total_discount = min(discount_percentage, 25.0)  # Cap the discount at 25%
        discounted_price = quntity_required * product["price"] * (1 - total_discount / 100)
        product["Quantity"] -= quntity_required
        total_discounted_price += discounted_price
        print(f"Discounted Price: ${discounted_price:.2f}")

        another_item = input("Do you want to add another item? (yes/no): ")
        if another_item.lower() != 'yes':
            break

application(products, total_discounted_price)
    
    
    
    
    