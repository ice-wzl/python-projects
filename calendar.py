from time import sleep, strftime

name = raw_input("What is your name?: ")

calendar = {}

def welcome():
  print "Welcome to the best calendar %s" % name
  print "One sec as the calendar opens..."
  sleep(1)
  print 'The current date is: ' + strftime("%A %B %d, %Y")
  print 'The current time is: ' + strftime("%H:%M:%s")
  sleep(1)
  print "What would you like to do?: "

def start_calendar():
  welcome()
  start = True 
  while start == True:
    user_choice = raw_input('Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ')
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "There are no entries in your calendar :("
      else:
        print calendar 
    elif user_choice == "U":
      date = raw_input("What date is this for: ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update was successful!"
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter Event: ")
      date = raw_input("Enter Date (MM/DD/YYYY): ")
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "That is not a properly formatted date!"
        try_again = raw_input("Would you like to try again Y for Yes, N for No?: ")
        try_again = try_again.upper()
        if try_again == "Y":
         contine 
        else:
          start = False
      else:  
        calendar[date] = event
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "The calendar is empty!"
      else:
        event = raw_input("What event?: ")
        for date in calendar.keys():
           if event == calendar[date]:
            del calendar[date]
            print "Event was deleted successfully!"
            print calendar
           else:
             print "Incorrect date was specified, no entry for that date!"
    elif user_choice == "X":
      start = False   
    else:
      print "Invalid Command, quiting for your incompetence!"

start_calendar()                
