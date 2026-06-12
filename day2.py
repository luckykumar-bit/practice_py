list=[1,2,3,4,5]

for number in list:
    print(number)

for number in range(1,6):
    print(number)

order_queue= {"table1":"aaloo paratha","table2":"paneer paratha","table3":"gobi paratha"}
for table, order in order_queue.items():
    print("table:" + table + "order:" + order)
print(order_queue.items())

quantity_aaloo_paratha= 10
while quantity_aaloo_paratha > 0:
    print("aaloo paratha is being prepared.")
    quantity_aaloo_paratha -=1
    
    if quantity_aaloo_paratha == 5:
        print("half of the aaloo paratha is ready. time to start preparing the gogi paratha.")
        continue
        print("preparing aaloo paratha. remaining quantity:" + str(quantity_aaloo_paratha))
    if quantity_aaloo_paratha == 1:
        print("only aaloo paratha is left. need to prepare more aaloo paratha.")