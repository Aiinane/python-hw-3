
def double_zero(array):
    output_array = []
    i = 0
    
    try:
        for i in range(len(array)): 
            if array[i] == 0:
                output_array.insert(i+2,array[i])
                output_array.insert(i+2,array[i])

            else:
                output_array.append(array[i]) 

        print (output_array)
    except Exception as err:  # всі
        print('Some err')

try:
    input = input().split(",")

    array = []
    for i in range(len(input)):
        array.append(int(input[i]))

    double_zero((array))
except Exception as err:  # всі
    print('Some err')


     
    
# double_zero([1,0,2,3,0,4,5,0]) # [1,0,0,2,3,0,0,4,5,0,0]
# double_zero([1,2,0,3,4,0,5,0]) # [1,0,0,2,3,0,0,4,5,0,0]
# double_zero([1,2,3]) # [1,2,3] 