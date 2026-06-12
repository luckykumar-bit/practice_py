# print("/n--------Fucntions in Python--------/n")

# balance = 1000.00

# # function with no parameters and no return value
# def check_balance():
#     print("Your current balance is: " + str(balance))   


# print("Checking balance for the first time:")
# check_balance()

# # function with parameters and no return value
# def update_balance(amount):
#     new_balance = balance + amount
#     print("Balance updated successfully. New balance: " + str(new_balance))



# print("Updating balance by adding 500.00:")

# update_balance(500.00)


# #function with parameters and return value
# def calculate_total_bill(rate, quantity):
#     total = rate * quantity
#     return total


# print("Calculating total bill for Order A:")
# total_a = calculate_total_bill(10.00, 5)
# print(type(total_a))
# print("Total for Order A: " + str(total_a))

#function with default parameter value
def calculate_total_bill_with_tax(rate, quantity, tax_rate=0.05):
    total = rate * quantity
    total_with_tax = total + (total * tax_rate)
    return total_with_tax

# print("calculating total bill for order b:")
# total_b = calculate_total_bill_with_tax(30.00,3)
# print("total for order b:" + str(total_b))

# def mark_ration(total_marks,sub_marks):
#     total=(sub_marks/otal_marks)*100
#     return total
# print("calculating marks percentage:")
# percentage=mark_ration(500,429)
# print("percentage:"+ str(percentage))

def change(x):
    x = 100
    print("Inside function:", x)

a = 10
change(a)

print("Outside function:", a)

# def add(a,b):
#     return a*b
# result = add(10,30)
# print("Result:", result)

def new_fun(a,b,c):
    sum=a+b+c
    print("this is a new function.")
    return sum
sum= 5+ new_fun(1,2,3)
print("sum of 5 and the return value of new_fun:" + str(sum))