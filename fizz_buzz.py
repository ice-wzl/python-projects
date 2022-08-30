""" Write a program that prints the numbers from 1 to 100. But for multiples of three print 'Fizz' instead of the number and for the multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'"""

for i in range(1,101):
  #see if divisable by 3 and 5 
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  #see if divisible by 3
  elif i % 3 == 0:
    print("Fizz")
  #see if divisable by 5
  elif i % 5 == 0:
    print("Buzz")
  #else print the number 
  else:
    print(i)
