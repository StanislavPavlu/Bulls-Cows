# Identification:
"""
Buls & Cows.py: second project for Engeto Online Python Akademie
author: Stanislav Pavlů
email: standic@seznam.cz
discord: Standa P. (standa_40063)
"""

# Import modules:
from os import system
from random import randint
from time import time, localtime, strftime

def time_for_print():
    '''
    Description:
    User function to record and print the start and end time of the game.
    point_time -> time.struct_time (needed to create point_str)
    point_str -> str (well-readable format)
    
    Example:
    Start of the game: 15:30:45
    End of the game: 15:31:15
    '''
    point_time = localtime()
    point_str = strftime("%H:%M:%S", point_time)
    return(point_str)

def time_for_substracting():
    '''
    Description:
    User function to record start and end time in a format usable for substraction.
    The length of the game is than calculated by subtracting these two time points.
    point -> float (seconds since January 1, 1970)
    '''
    point = time()
    return(point)

# Cleaning the terminal:
system("cls")

# Greeting and introduction:
line_lenght = 50
line_simple = line_lenght * "-"
line_double = line_lenght * "="
print(f'''{line_double} 
Welcome to the game "Bulls & Cows" !!!
{line_simple}
I've generated a random 4 digit number for you.
Guess this number in as few attempts as possible.
Let's play a "Bulls & Cows" game !!!
{line_double}''')

# Generating a secret number:
generation_running = True
while generation_running == True:
    number_generated_int = randint(1000, 9999)
    # print(number_generated_int)       # Control print
    number_generated_str = str(number_generated_int)
    number_generated_set = set(number_generated_str)
    if len(number_generated_str) == len(number_generated_set):
        generation_running = False

print(f'''{"### GENERATED SECRET NUMBER ###":^{line_lenght}}\n
{"***   " + number_generated_str + "   ***":^{line_lenght}}\n
{"### SHOWN FOR CONTROL PURPOSE ###":^{line_lenght}}
{line_simple}''')

# Time - start of the game:
start_print = time_for_print()
print(f"Start of the game: {start_print}\n{line_simple}")
start_substract = time_for_substracting()

# Entering and checking the guessed number:
number_guessed_str = str()
number_attempts = 1
while number_guessed_str != number_generated_str: 
    error_checking = True    
    while error_checking == True:
        number_guessed_str = input(f"{number_attempts}.attempt - enter a 4 digit number:\n")
        number_guessed_set = set(number_guessed_str)
        errors = 0
        if number_guessed_str == '':
            print(f"Error: no input entered\n{line_simple}")
        else:
            if len(number_guessed_str) != 4:
                errors += 1
                print(f"Error nr.{errors}: incorrect length")
            if len(number_guessed_str) != len(number_guessed_set):
                errors += 1
                print(f"Error nr.{errors}: double characters")
            if (number_guessed_str[0]) == "0":
                errors += 1
                print(f"Error nr.{errors}: the number starts with zero")
            if not number_guessed_str.isdigit():
                errors += 1
                print(f"Error nr.{errors}: non numeric characters")
            if errors != 0:
                print(line_simple)
            else:
                error_checking = False
        number_attempts += 1    
        
    # Attempt evaluation:
    number_bulls = 0
    number_cows = 0      
    for index, character in enumerate(number_guessed_str):
        if character == number_generated_str[index]:
            number_bulls += 1          
        if character != number_generated_str[index] and character in number_generated_str:
            number_cows += 1

    # Attempt results - print:
    bull_bulls = "bulls"
    cow_cows = "cows"
    if number_bulls == 1:
        bull_bulls = "bull"
    if number_cows == 1:
        cow_cows = "cow"
    print(f"{number_bulls} {bull_bulls}, {number_cows} {cow_cows}\n{line_simple}")
    
# Time - end of the game:
end_print = time_for_print()
print(f"End of the game: {end_print}\n{line_simple}")
end_substract = time_for_substracting()

# Final evaluation:
duration = end_substract - start_substract
print(f"Correct, {number_guessed_str} is the right number!!!")
print(f"Attempts: {number_attempts - 1}, Duration: {round(duration, 1)} seconds")
print(f"Game over !!!\n{line_double}")