def investment_report(principal,years,rate):
    rate/=100
    print("Year\tStarting balance\tInterest\tEnding balance")

    total_interest = 0.0
    for year in range(1, years + 1):
        interest = principal * rate
        ending_balance = principal + interest
        total_interest += interest
        print(f"{year}\t{principal:.2f}\t\t{interest:.2f}\t\t{ending_balance:.2f}")
        principal = ending_balance

    print(f"Ending balance: ${principal:.2f}")
    print(f"Total interest earned: ${total_interest:.2f}")

p=float(input("Enter the investment amount : "))
y=int(input("Enter the number of years : "))
r=int(input("Enter the rate as % : "))
investment_report(p,y,r)
