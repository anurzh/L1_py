income = int(input("Input income of company: "))
costs = int(input("Input costs: "))
if int(income) > int(costs):
    print("Great, you have income")
    efficiency = (income - costs) / income
    print("Your efficiency is %.2f" % efficiency)
    workers_amount = int(input("Input amount of workers: "))
    profit = income - costs
    salary = profit / workers_amount
    print("Each worker income: ", salary, "$")
elif int(costs) > int(income):
    print("No income, don't worry, try to work better")
else:
    print("Equal")
