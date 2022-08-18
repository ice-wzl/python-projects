# calculator that can convert RGB values to Hexadecimal (hex) values, and vice-versa.

def rgb_hex():
  invalid_msg = "That is an invalid message"
  red = int(raw_input("Enter a value for red: "))
  if red > 255 or red < 0:
    print invalid_msg
    return
  green = int(raw_input("Enter a value for green: "))
  if green > 255 or green < 0:
    print invalid_msg
    return
  blue = int(raw_input("Enter a value for red: "))
  if green > 255 or green < 0:
    print invalid_msg
    return   
  val = (red << 16) + (green << 8) + blue
  print "%s" % (hex(val)[2:]).upper()

def hex_rgb():
  hex_val = raw_input("Enter a hex value: ")
  if len(hex_val) != 6:
    print "That is not a valid hex char you fool: "
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "Red: %s Green: %s Blue: %s" % (red,green,blue)

def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == '1':
      print "RGB to Hex..."
      rgb_hex()
    elif option == '2':
      print "Hex to RGB..."
      hex_rgb()
    elif option == 'X':
      break
    else:
      print "Error, you are a fool!"
convert()















