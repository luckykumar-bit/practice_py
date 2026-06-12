# for i in range(1, 6):
#     print(i)


i = 1
while i <= 5:
    print(i)
    i += 1

#     total = 0

# for i in range(1, 6):
#     total += i

# print("Sum =", total)

# for i in range(2, 11, 2):
#     print(i)

#     num = 8

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

    #  age = 18
    #  if age >= 18:
    #   print("Can Vote")
    #  else:
    #   print("Cannot Vote")
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