import random
import time

def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")

        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("this is not a valid input")
    return user_input


while(True):
    rand_number = random.randint(0, 1000)
    
    for x in range(0, 10, 1):
        guess = get_input("please input a number between 0 and 1000", int)

        if guess > rand_number:
            print(f"{guess} is too high\n")
        elif guess < rand_number:
             print(f"{guess} is too low\n")
        elif guess == rand_number:
             print(f"{guess} is correct, well done! It took you {x+1} guesses\n")
             break
        if x == 9:
             print(f"uh oh, bad luck buddy. you only got 10 guesses. the number was {rand_number}\n")
             time.sleep(3)


        
