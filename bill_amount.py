bill_amount = int(input())
if(bill_amount <10000):
    print("No discount")
elif(bill_amount>=10000 and bill_amount<25000):
    print("Discount of 10%")
    discount_price = 0.1*bill_amount
    final_price = bill_amount- discount_price
    print("final_price=",final_price)
elif(bill_amount>=25000 and bill_amount<35000):
    print("discount of 30%")
    discount_price = 0.3*bill_amount
    final_price = bill_amount- discount_price
    print("final_price=",final_price)
else:
    print("Discount of 50%")
    discount_price = 0.5*bill_amount
    final_price = bill_amount- discount_price
    print("final_price=",final_price)
