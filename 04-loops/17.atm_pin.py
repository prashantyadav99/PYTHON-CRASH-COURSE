print('=== BANK OF BHAROSA===')  

pin = int(input('Enter your PIN: '))

while pin != 9936:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 9936:
  print('PIN accepted!')
