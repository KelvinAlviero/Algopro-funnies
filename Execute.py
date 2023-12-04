from Classes import food_KA

while True:
    f_amount = int(input("Enter amount of items your willing to buy"))
    if f_amount <=0:
        print("Amount must be greater than 1")
        pass
    else:
        break

f_list = []

for i in range(f_amount):
    print(f"item #{i+1}-")
    f_order= str(input("Enter food: "))
    P_order = float(input("Enter amount of pounds: "))

    my_order = food_KA(f_order,f_amount)
    f_list.append(my_order)

total_price = 0

print("Summary of purchases:")
print("="*20)
for i in f_list:
    print(f"Item {i.get.name_KA()}")
    print(f"Amount ordered: {i.get_amount_KA()}pounds\n")
    print(f"price per pound: ${i.get_priceperpound_KA()}\n")
    print(f"price of orders: ${i.calculate_price_KA()}")

    total_price += i.calculate_price_KA()

print()
print(f"Total price: ${total_price}")