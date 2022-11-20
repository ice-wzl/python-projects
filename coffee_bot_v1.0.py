# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
def get_size():
  res = input("What size drink can I get for you:\n[a] Small\n[b] Medium\n[c] Large \n")
  res = res.lower()
  if res == 'a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large'
  else:
    print('Im sorry, I did not understand your selection. Please enter the corresponding letter for your response.')
    return get_size()

def get_drink_type():
  res = input('What type of drink would you like:\n[a] Brewed Coffee\n[b] Mocha\n[c] Latte\n')
  res = res.lower()
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return order_latte()
  else:
    print('Im sorry, I did not understand your selection. Please enter the corresponding letter for your response.')
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk would you like for your latte:\n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk\n")
  if res == 'a':
    return 'Latte'
  elif res == 'b':
    return 'Non-fat latte'
  elif res == 'c':
    return 'Soy latte'
  else:
    print_message()
    return order_latte()

# Call coffee_bot()!
coffee_bot()
size = get_size()
drink_type = get_drink_type()
print("Alright, that\'s a {} {}".format(size, drink_type))
name = input("Can I get your name? ")
print("Thanks, {}! Your drink will be ready shortly".format(name))
