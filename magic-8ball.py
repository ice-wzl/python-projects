#fun magic 8 ball game, enter your name and question to recieve your answer
import random
print("""
  __  __             _         ___        ____        _ _ 
 |  \/  |           (_)       / _ \      |  _ \      | | |
 | \  / | __ _  __ _ _  ___  | (_) |_____| |_) | __ _| | |
 | |\/| |/ _` |/ _` | |/ __|  > _ <______|  _ < / _` | | |
 | |  | | (_| | (_| | | (__  | (_) |     | |_) | (_| | | |
 |_|  |_|\__,_|\__, |_|\___|  \___/      |____/ \__,_|_|_|
                __/ |                                     
               |___/                                     
""")
continue_ = True
while continue_ == True:
  name = input("What is your name?: ")
  name = name.capitalize()
  question = input("Ask a yes or no question?: ")
  question = question.capitalize()
  answer = ""
  print("%s asks: %s" % (name,question))
  random_number = random.randint(1,9)
  if random_number == 1:
    answer = "Yes, definitely."
  elif random_number == 2:
    answer = "It is decidedly so."
  elif random_number == 3:
    answer = "Without a doubt."
  elif random_number == 4:
    answer = "Reply hazy, try again."
  elif random_number == 5:
    answer = "Ask again later"
  elif random_number == 6: 
    answer = "Better not tell you now"
  elif random_number == 7:
    answer = "My sources say no."
  elif random_number == 8:
    answer = "Outlook not so good"
  elif random_number == 9:
    answer = "Very doubtful"
  else:
    answer = "Error"
  print("Magic 8-Ball's answer: %s" % answer)
  user_choice = input("Do you want to replay (Y/N)?: ")
  user_choice = user_choice.upper()
  if user_choice == "N":
    continue_ = False
  elif user_choice == "Y":
    continue
  else:
    print("Error invalid choice")

