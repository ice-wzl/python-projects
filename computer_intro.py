import requests
from datetime import datetime


def greeting():
  time_now = datetime.now()
  nickname = "NICKNAME_HERE"
  greeting = time_now.strftime("%H")
  greeting = int(greeting)
  if greeting > 5 and greeting < 12:
    print("Good morning " + nickname)
  elif greeting > 12 and greeting < 17:
    print("Good afternoon " + nickname)
  else:
    print("Good evening " + nickname)

  _date = time_now.strftime("%m/%d/%Y")
  _time = time_now.strftime("%H:%M:%S")
  print("Date: " + _date)
  print("Time: " + _time)

def get_random_quote():
	try:
		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if response.status_code == 200:
			## extracting the core data
			json_data = response.json()
			data = json_data['data']
			print(data[0]['quoteText'])
		else:
			print("Error while getting quote")
	except:
		print("Something went wrong! Try Again!")



#weather func
def weather():
  print("Your Current Weather Report: ")
  url = "https://wttr.in/"
  r = requests.get(url)
  print(r.text)


greeting()
weather()

#quote of the day 
print("Quote of the Day: ")
get_random_quote()

