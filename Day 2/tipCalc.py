def tip_calculator():
    print("Welcome to tip calculator.")
    total_bill = float(input("What was the total bill? $"))
    split_by = int(input("How many people to split the bill?"))
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
    amount = round(float((total_bill/split_by) + (tip*total_bill/100)))
    print(f"Each person should pay: $ {amount}")


tip_calculator()
