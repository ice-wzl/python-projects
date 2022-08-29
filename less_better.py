from time import sleep, strftime

banner = "Ⓛⓔⓢⓢ, ⓑⓤⓣ Ⓑⓔⓣⓣⓔⓡ"

database_ = {}

def welcome_msg():
  print(banner)
  print('Date: The current date is: ' + strftime("%A %B %d, %Y"))
  print("This is where we record the most important daily task\n")
  
def start_():
  welcome_msg()
  start = True 
  while start == True:
    options_ = input("Select V to view past entries, press E enter todays, or Q to Quit : ")
    options_ = options_.upper() 
    if options_ == "V":
      if len(database_.keys()) < 1:
        print("You have no past entries")
      else:
        print(database_)  

    elif options_ == "E":
      acomp = input("What would you like to acomplish today?: ")
      current_date_ = strftime("%A %B %d, %Y") 
      database_[current_date_] = acomp
      print("Update Successful")

    elif options_ == "Q":
      start = False

    else:    
      print("Incorrect Selection")

start_()
