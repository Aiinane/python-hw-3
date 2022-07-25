import sys




def calc(left, right, operation):

    allowed_operations = ['+', '-', '/', '*']

    try:
        match operation:
            case '*':
                print(left * right)
            case '+':
                print(left + right)
            case '-':
                print(left - right)
            case '/':
                if  right == 0:
                    print('Division by zero is not allowed')
                    sys.exit()
                else:
                    print(left / right)
            case '%':
                if  right == 0:
                    print('Operetion by zero is not allowed')
                    sys.exit()
                else:
                    print(left % right)
    except ValueError:
        
        if operation not in allowed_operations:
            print('Operation is not allowed')
            sys.exit()

def calculate ():
    
      
    if len(sys.argv) != 2 and len(sys.argv) != 4:
        print('Arg len should be 4')
        sys.exit()    
    
    left_operand = (sys.argv[1]) # легше, просто додати його в масив і слово розділяється
    
    try:
        if len(left_operand) > 2:
           
            first = int(left_operand[0])
            second = left_operand[1]
            third = int(left_operand[2])
            print (first,second,third)
            perform_operation (first, third, second)
        else:
            print (int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
            perform_operation (int(sys.argv[1]), int(sys.argv[3]), sys.argv[2])
        
    except ValueError:
        print('Left and Right operands must be int')
        sys.exit()
         
if __name__ == "__main__":
    calculate ()

