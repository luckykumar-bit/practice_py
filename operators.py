print("---billing section---")
order_a_quantity=2
order_a_rate=50.50

total_a= order_a_quantity * order_a_rate

budget=1000.00
paratha_cost=37
max_paratha= (budget // paratha_cost)
print("maximum paratha that can be bought :" +str(max_paratha) )

base_point=4
multiper=base_point** 3
print("multiper value is:" + str(multiper))

loyalty_points=100
if loyalty_points >50:
    print("customer is eligible for discount")
    discount= loyalty_points * 0.1
    print("discount amount is:" + str(discount))
