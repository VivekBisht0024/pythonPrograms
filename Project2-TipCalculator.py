print("Welcome to the tip calculator !")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10,12,15? "))

people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + tip / 100)

print("Each person should pay -> " + str(bill_with_tip))