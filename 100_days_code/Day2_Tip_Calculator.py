print("Welcome to Tip Calculator")
billamt = int(input("What was the total bill?"))
percentage = int(input("What percentage tip would you like to give? 10,12,15"))
ppl = int(input("How many people to split the bill?"))

percen = billamt*(percentage/100)
new_billamt = percen + billamt

pay = round(new_billamt/ppl,2)

print(f"Each person should pay ${pay}")