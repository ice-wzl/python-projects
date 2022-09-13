from termcolor import colored

premium_gs = 125.00

def banner():
  welcome = """
   __       _       __ _     _             _             
  / _\ __ _| |___  / _\ |__ (_)_ __  _ __ (_)_ __   __ _ 
  \ \ / _` | / __| \ \| '_ \| | '_ \| '_ \| | '_ \ / _` |
  _\ \ (_| | \__ \ _\ \ | | | | |_) | |_) | | | | | (_| |
  \__/\__,_|_|___/ \__/_| |_|_| .__/| .__/|_|_| |_|\__, |
                              |_|   |_|            |___/ 
"""
  print(welcome)

def charts():
  ground_shipping = """
// Cost of Ground Shipping:
2 lb or less: $1.50 per pound + flat rate: $20.00
Over 2 lb but less than or equal to 6 lb: $3.00	+ flat rate: $20.00
Over 6 lb but less than or equal to 10 lb $4.00 + flat rate: $20.00
Over 10 lb $4.75 + flat rate: $20.00"""
  drone_shipping = """
// Drone Shipping
**No Flat Rate Charge**
2 lb or less: $4.50 per pound
Over 2 lb but less than or equal to 6 lb: $9.00 per pound
Over 6 lb but less than or equal to 10 lb: $12.00 per pound
Over 10 lb: $14.25 per pound
"""
  print(colored(ground_shipping + "\n", 'blue', attrs=['bold']))
  print(colored("// Premium Ground Shipping Rate: %s" % "$125.00", 'red', attrs=['bold']))
  print(colored(drone_shipping, 'green', attrs=['bold']))
def calc():
  weight = input("Enter the weight of your package: ")
  weight = float(weight)
#ground shipping 
  if weight <= 2:
    print("Ground Shipping: " + str(weight * 1.50 + 20.00))
  elif weight > 2 and weight <= 6:
    print("Grpund Shipping: " + str(weight * 3.00 + 20.00))
  elif weight > 6 and weight <= 10:
    print("Ground Shipping: " + str(weight * 4.00 + 20.00))
  else:
    print("Ground Shipping: " + str(weight * 4.75 + 20.00))
#drone shipping
  if weight <= 2:
    print("Drone Shipping: " + str(weight * 4.50))
  elif weight > 2 and weight <= 6:
    print("Drone Shipping: " + str(weight * 9.00))
  elif weight > 6 and weight <= 10:
    print("Drone Shipping: " + str(weight * 12.00))
  else:
    print("Drone Shipping: " + str(weight * 14.25))

banner()

choice = True
while choice == True:
  user_choice = input("Enter (C) to see charts, (X) to calculate or (Q) to quit: ")
  user_choice = user_choice.upper()
  if user_choice == "Q":
    print("Goodbye")
    choice = False
  elif user_choice == "C":
    charts()
  elif user_choice == "X":
    calc()
  else:
    print("That was not a valid option.")
