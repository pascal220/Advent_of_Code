# import numpy as np

def ChallengePart_1():
    # input_file_exanple = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
    input_file = open('input.txt', 'r').readlines()
    current_value = 50
    zero_counter = 0

    for str in input_file:
        current_number = int(str[1:])
        
        if str[0] == 'L':
            current_number = current_number *-1
        
        current_value = (current_value + current_number)%100

        if current_value == 0:
            zero_counter += 1
        
        # For debugging only
        # print(current_value)

    print(f"The password is: {zero_counter}")

def ChallengePart_2():
    input_file_exanple = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
    # input_file = open('input.txt', 'r').readlines()
    current_value = 50
    zero_counter = 0
    
    for str in input_file_exanple:
        current_number = int(str[1:])
        
        if str[0] == 'L':
            current_number = current_number *-1
        
        current_value = (current_value + current_number)%100

        if abs(current_number) > 100:
            zero_counter += current_number%100

        if current_value == 0:
            zero_counter += 1


    print(f"The password is: {zero_counter}")

def main():

    # ChallengePart_1()
    ChallengePart_2()
    

if __name__ == "__main__":
    main()