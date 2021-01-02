#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


print("Welcome to the tip Calculator!")
Total_bill = input("What is the total bill? ")
percent_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
person_will_pay = input("How many people will split the bill? ")

#Float and Int 
Total_bill_int = float(Total_bill)
percent_tip_int = int(percent_tip)
person_int = int(person_will_pay)

#Computation for the tip
percented_tip = Total_bill_int * (percent_tip_int / 100)
rounded_tip = round(percented_tip, 2)

#Adding total bill and tip
Total_bill_tip = Total_bill_int + rounded_tip

#Split the Total Bill
Split_bill = Total_bill_tip / person_int

print("Each person should pay: $" + str(Split_bill))