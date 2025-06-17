business_hours=int(input("How many hours did you work this month? " ))
Hourly_rate=int(input("How much do you earn per hour? "))
tax=int(input("What is the tax rate? "))
gross=business_hours*Hourly_rate
net=gross*(1-tax/100)
print("Salary after tax",net)
print("Salary before tax",gross)