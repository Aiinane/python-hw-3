def remove_duplicates(array):
    
    output_set = set()
    output_array = []
    i = 0
    try:
        for i in range(len(array)):
            output_set.add(array[i])

        for i in output_set:
            output_array.append(i)

        print (output_array)
    except Exception as err:  # всі
        print('Some err')

try:
    input = input().split(",")

    array = []
    for i in range(len(input)):
        array.append(int(input[i]))
   

    remove_duplicates((array))
except Exception as err:  # всі
    print('Some err')


# remove_duplicates([1,1,2]) # [1,2]
# remove_duplicates([0,0,1,1,1,2,2,3,3,4]) # [0,1,2,3,4]
# remove_duplicates([1,1,1,1,1,1,1,1]) # [1]