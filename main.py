#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator.\n")
bill = input("What was the bill? ")
percentage = input("What percentage would you like to give? ")
people = input("How many people to split the bill? ")
percentage_as_int = int(percentage)
bill_as_float = float(bill)
people_as_int = int(people)
new_percentage = percentage_as_int / 100
new_bill = bill_as_float + (bill_as_float * new_percentage)
result = (new_bill / people_as_int)
new_result = round(result, 2)
print(f"Each person should pay:${new_result}")