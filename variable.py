# age=18
# print(age)
# name="lucky"
# print(name)
dish_name="pizza"
print("I love to eat " + dish_name)

order_quantity=2
order_rate=50.00
dhaba_items=("pav bhaji", "ROTI" , "DAL", "RICE")
dhaba_manu={
    "pav bhaji": 50.00,
    "ROTI": 60.00,
    "DAL": 55.00,
    "RICE": 45
}

print("dhaba items:" + str(dhaba_items))
print("order quantity:" + str(order_quantity))
print("order rate:" + str(order_rate))

print(type(order_quantity))
print(type(str(order_rate)))

print(type(dhaba_items))
print(type(dish_name))

print("---billing---")
order_a_quantity=2
order_a_rate=50.50

total_a=order_a_quantity *order_a_rate
print("total for order A:"+ str(total_a))



order_b_quantity=5
order_b_rate=60.00
total_b=order_b_quantity * order_b_rate
print("total for order B:"+ str(total_b))

total_bill=total_a + total_b
print("total bill amount:" + str(total_bill))

cash_given=500.00
change=cash_given - total_bill
print("change to be returned:" + str(change))

budget=1000.00
food_cost= 39
max_food= (budget / food_cost)
max_food1= (budget // food_cost)
print("maximum food that can be bought with the budget:" + str(max_food))
print("maximum food that can be bought with the budget:" + str(max_food1))
customer_number= 123456789
remainder=customer_number%100
print("remainder when customer number is divided by 100:" +str(remainder))

base_point=4
multiplier= base_point** 3
print("loyalty point multipler: " + str(multiplier))

loyalty_points= int(input("enter the your loyalty points:"))

if loyalty_points > 50:
    print("customer is eligible for a discount", )
    discount= loyalty_points * 0.1
    print("discount amount:" +
          str(discount))
else:
    print("customer is not eligible for discount.")

    is_dhaba_open=True
    dal_stock= 0

    if is_dhaba_open:
        print("Dhaba is open.")

        if dal_stock > 0:
            print("dal is available.")
        else:
            print("dal is out of stock.")
    else:
        print("dhaba is closed")

