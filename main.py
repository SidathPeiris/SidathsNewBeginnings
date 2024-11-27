#given function 
def two_number_sum(input: list[int], target: int)-> list[int]:

    #counter for first number thats being counted, starting at position 0 in the array
    counter_num1 = 0
    #counter for second number thats being counted, starting at position 1 in the array 
    counter_num2 = 1

    #while function which is running when counter_num1 is less than the length of the input array minus 1 and counter_num2 is less than the length of the input array
    #length of input is how many numbers are in the list that the user inputs
    while counter_num1 < (len(input)-1) and counter_num2 < len(input):
        #if statement that checks if the sum of the two numbers is equal to the target number
        if input[counter_num1] + input[counter_num2] == target:
            #if the two numbers are equal to the target number, print the two numbers
            print(input[counter_num1], input[counter_num2])
            #ends the while loop
            break
        # if statement for what happens if the sum of the two numbers is not equal to the target number
        elif input[counter_num1] + input[counter_num2] != target:
            #if the sum of the two numbers is not equal to the target number, add 1 to the counter_num2
            counter_num2 = counter_num2 + 1
            #once the counter has reached the length of the input, add 1 to counter_num1 and resets counter_num2 to counter_num1 plus 1
            if counter_num2 == len(input):
                counter_num1 = counter_num1 + 1
                counter_num2 = counter_num1 + 1
        else:
            continue

two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10)