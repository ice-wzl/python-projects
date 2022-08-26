#project to practice OOP, bank account to allow for deposit and withdraw with some error checking 
class BankAccount(object):
  balance = 0 

  def __init__(self, name):
    self.name = name

  def __repr__(self): 
    return "Account Owner: %s, Balance: $%.2f" % (self.name, self.balance)

  def show_balance(self):
    return "Balance: $%.2f" % (self.balance)

  def deposit(self, amount):
    self.amount = amount
    if amount <= 0:
      print "That is not a valid balance!"
      return 
    else:
      print "Deposit Amount: $%.2f" % (self.amount) 
      self.balance += amount
      print self.show_balance()

  def withdraw(self, amount):
    self.amount = amount
    if amount > self.balance:
      print "That is an invalid request, amount requested is greater than current balance"
      return 
    else:
      print "Withdrawing: $%.2f" % (self.amount)
      self.balance -= amount
      print self.show_balance()

my_account = BankAccount("Jack's Account")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
