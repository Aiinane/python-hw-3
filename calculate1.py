import sys

try:
 
  


 
   
     if len(sys.argv) < 4:
        print("Usage: " + sys.stdin.readlines(sys.argv[0]) + " OPERAND OPERATOR OPERAND")

     a = float(sys.argv[2])
     b = float(sys.argv[3])
     op = str (sys.argv[1])

     if op == '+':
        res = a + b
     elif op == '-':
        res = a - b
     elif op == '*':
        res = a * b
     elif op == '/':
        res = a / b
     else:
        print("Invalid operator: '{}'".format(op))
        exit()

     print(res)

    
 
#     def calculate():
#      input = sys.stdin.read()
#      operation = input('''
# Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')
#      number_1 = int(input('Please enter the first number: '))
#      number_2 = int(input('Please enter the second number: '))
#      if operation == '+':
#        print('{} + {} = '.format(number_1, number_2))
#        print(number_1 + number_2)
#      elif operation == '-':
#        print('{} - {} = '.format(number_1, number_2))
#        print(number_1 - number_2)
#      elif operation == '*':
#        print('{} * {} = '.format(number_1, number_2))
#        print(number_1 * number_2)
#      elif operation == '/':
#        print('{} / {} = '.format(number_1, number_2))
#        print(number_1 / number_2)
#      else:
#        print('You have not typed a valid operator, please run the program again.')
#      # Вызов функции calculate() вне функции
#     calculate()

    

 
except OSError as err:
    print("OS error: {0}".format(err))

import sys

try:
 
  


 
   
     if len(sys.argv) < 4:
        print("Usage: " + sys.stdin.readlines(sys.argv[0]) + " OPERAND OPERATOR OPERAND")

     a = float(sys.argv[2])
     b = float(sys.argv[3])
     op = str (sys.argv[1])

     if op == '+':
        res = a + b
     elif op == '-':
        res = a - b
     elif op == '*':
        res = a * b
     elif op == '/':
        res = a / b
     else:
        print("Invalid operator: '{}'".format(op))
        exit()

     print(res)

    
 
#     def calculate():
#      input = sys.stdin.read()
#      operation = input('''
# Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')
#      number_1 = int(input('Please enter the first number: '))
#      number_2 = int(input('Please enter the second number: '))
#      if operation == '+':
#        print('{} + {} = '.format(number_1, number_2))
#        print(number_1 + number_2)
#      elif operation == '-':
#        print('{} - {} = '.format(number_1, number_2))
#        print(number_1 - number_2)
#      elif operation == '*':
#        print('{} * {} = '.format(number_1, number_2))
#        print(number_1 * number_2)
#      elif operation == '/':
#        print('{} / {} = '.format(number_1, number_2))
#        print(number_1 / number_2)
#      else:
#        print('You have not typed a valid operator, please run the program again.')
#      # Вызов функции calculate() вне функции
#     calculate()

    

 
except OSError as err:
    print("OS error: {0}".format(err))




import sys


input = sys.stdin.read()
# print (input)
#tokens = input.split() 

# try:
    #  number1 = sys.stdin.read(1000)
    # number2 = sys.stdin.read(1000)
    # sys.stdin.close()
    
 

    # print(number1,number2)
#input = sys.stdin.read()
number1 = 0
number2 = 0
    # counter = 0

    # while input:
     
    #  number1 = input.read()
    #  if number1 == ' ':
    #     number2 = input.read()
    # if number2 == ' ':
    #     break
    #     sys.stdin.close()
    # counter += 1
while True:
    data = input("Please enter the message:\n")
    if 'Exit' == data:
        break
    print(f'Processing Message from input() *****{data}*****')

print("Done")




   # print(number1)

       
#except ValueError:
        # print("Oops!  That was no valid number.  Try again...")

# try:
# number1 = sys.stdin.read(1)
# sys.stdin.close()
# print(number1 )
# break
#  except ValueError:
# ...         print("Oops!  That was no valid number.  Try again...")

# number2 = input()




