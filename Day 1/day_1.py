# The following is the first set of two challenges of the very first day of the Advent of Code 2025.
# The description of each puzzle can be found following this link: https://adventofcode.com/2025/day/1
# Author of this code: Filip P. Paszkiewicz
# Last Edited: 8th of December 2025

def ChallengePart_1():
    # input_file_example = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
    input_file = open('input.txt', 'r').readlines()
    current_value = 50
    zero_counter = 0

    for str in input_file:
        # Transforms string into a number we can work wtih 
        current_rotation = int(str[1:])
        if str[0] == 'L':
            current_rotation = current_rotation *-1
        
        # Calculates the new dial after rotation
        current_value = (current_value + current_rotation)%100

        if current_value == 0:
            zero_counter += 1

    print(f"The password is: {zero_counter}")

def ChallengePart_2():
    # input_file = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
    input_file = open('input.txt', 'r').readlines()

    current_value = 50
    zero_counter = 0

    for str in input_file:
        # Transforms string into a number we can work wtih 
        current_rotation = int(str[1:])
        if str[0] == 'L':
            current_rotation = current_rotation *-1

        # Find instances when teh dial passes through or stops at zero
        sum = current_value+current_rotation
        if sum>99:
                zero_counter += (current_value+current_rotation)//100
        elif sum<=0:
                if current_value == 0:
                     zero_counter -= 1
                zero_counter += abs(current_value+current_rotation)//100 + 1

        # Calculates the new dial after rotation
        current_value = (current_value + current_rotation)%100

    print(f"The password is: {zero_counter}")

def main():

    ChallengePart_1()
    ChallengePart_2()
    

if __name__ == "__main__":
    main()