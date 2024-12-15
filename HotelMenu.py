Menu={
    "Pasta" :80,
    "Pizza" :100,
    "Coffee":60,
    "Salad" :70,
    "Maggie":50
}
print("Welcome to the Restaurant")
print("Pasta : Rs8\nPizza : Rs100\nCoffee : Rs60\nSalad : Rs70\nMaggie : Rs50")
Total_Order=0
item_1=input("Enter the first item you want to order= ")
if item_1 in Menu:
    Total_Order += Menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")

Another_item=input("Do you want to order another item ? (Yes/No) ")
while Another_item!="No":
     other_item=input("Enter another item you want to order= ") 
     if other_item in Menu:
         Total_Order += Menu[other_item]
         print(f"Your item {other_item} has been added to your order")
     else:
         print(f"Ordered item {other_item} is not available yet")
     Another_item=input("Do you want to order another item ? (Yes/No) ")

print(f"Total amount to pay is {Total_Order}")