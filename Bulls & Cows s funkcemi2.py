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

# Definition of lines:
line_lenght = 50
line_simple = line_lenght * "-"
line_double = line_lenght * "="

def main() -> None:
    '''
    Main function of the program
    '''
    system("cls")    # Cleaning the terminal:
    
    greeting()
    
    random_number = random_number_gen()
    while random_number_check(random_number) == False:
        random_number = random_number_gen()
        
    print(f"Start of the game: {time_for_print()}\n{line_simple}")      # Time - start of the game:
    start_substract = time_for_substracting()
    
    attempts = 0
    attempts, guessed_number = guessed_number_ins(attempts)
    while guessed_number != random_number:
        while guessed_number_check(guessed_number) == False:
            attempts, guessed_number = guessed_number_ins(attempts)
        else:
            if guessed_number == random_number:
                break
            else:
                attempt_evaluation(random_number, guessed_number)
                attempts, guessed_number = guessed_number_ins(attempts)
    
    end_substract = time_for_substracting()
    attempt_evaluation(random_number, guessed_number)
    final_evaluation(attempts, guessed_number, start_substract, end_substract)

def greeting() -> str:
    '''
    Description:
    User function with greeting and game instructions (game header)
    '''
    print(f'''{line_double} 
Welcome to the game "Bulls & Cows" !!!
{line_simple}
I've generated a random 4 digit number for you.
Guess this number in as few attempts as possible.
Let's play a "Bulls & Cows" game !!!
{line_double}''')
    
def time_for_print() -> str:
    '''
    Description:
    User function to record and print the start and end time of the game.
    point_time -> time.struct_time (needed to create point_str)
    point_str -> str (user friendly format)
    
    Example:
    Start of the game: 15:30:45
    End of the game: 15:31:15
    '''
    point_time = localtime()
    point_str = strftime("%H:%M:%S", point_time)
    return point_str

def time_for_substracting() -> float:
    '''
    Description:
    User function to record start and end time in a format usable for substraction.
    The length of the game is than calculated by subtracting these two time points.
    point -> float (seconds since January 1, 1970)
    '''
    point = time()
    return point

def random_number_gen() -> str:
    '''
    Description:
    User function to generate a random 4 digit number.
    '''
    random_number_int = randint(1000, 9999)
    random_number = str(random_number_int)
    # print(random_number_str)  # Control print
    return random_number

def random_number_check(random_number_par: str) -> bool:
    '''
    Description:
    User function to check the random generated 4 digit number.
    The random generated number must meet these conditions:
        - no duplicate digits (examples: 1233 -> no, 1234 -> yes)
    '''
    random_number_health = False
    random_number_set = set(random_number_par)
    if len(random_number_par) == len(random_number_set):
        random_number_health = True
        print(f'''{"### GENERATED SECRET NUMBER ###":^{line_lenght}}\n
{"***   " + random_number_par + "   ***":^{line_lenght}}\n
{"### SHOWN FOR CONTROL PURPOSE ###":^{line_lenght}}
{line_simple}''')
    return random_number_health

def guessed_number_ins(attempts_par: int):
    '''
    Description:
    User function to enter the guessed number.
    '''
    attempts_par += 1
    guessed_number = input(f"{attempts_par}.attempt - enter a 4 digit number:\n")
    return attempts_par, guessed_number    

def guessed_number_check(guessed_number_par: str) -> bool:
    '''
    Description:
    User function to check the guessed number.
    The guessed number must meet these conditions:
        - 4 digits (examples: 123 -> no, 1234 -> yes)
        - no duplicate digits (examples: 1233 -> no, 1234 -> yes)
        - the first digit must not be zero (examples: 0123 -> no, 1234 -> yes)
        - cannot contain non-numeric characters (examples: 123a -> no, 1234 -> yes)
    '''
    guessed_number_health = False    
    guessed_number_set = set(guessed_number_par)
    errors = 0
    if guessed_number_par == '':
        print(f"Error: no input entered\n{line_simple}")
    else:
        if len(guessed_number_par) != 4:
            errors += 1
            print(f"Error nr.{errors}: incorrect length")
        if len(guessed_number_par) != len(guessed_number_set):
            errors += 1
            print(f"Error nr.{errors}: double characters")
        if (guessed_number_par[0]) == "0":
            errors += 1
            print(f"Error nr.{errors}: the number starts with zero")
        if not guessed_number_par.isdigit():
            errors += 1
            print(f"Error nr.{errors}: non numeric characters")
        if errors != 0:
            print(line_simple)
        else:
            guessed_number_health = True
    return guessed_number_health    

def attempt_evaluation(random_number_par: str, guessed_number_par: str) -> str:
    '''
    Description:
    User function to evaluate the number of bulls and cows in the guessed number.
    Example:
    1234                #(guessed number)
    2 bulls, 1 cow
    '''
    number_bulls = 0
    number_cows = 0      
    for index, character in enumerate(guessed_number_par):
        if character == random_number_par[index]:
            number_bulls += 1          
        if character != random_number_par[index] and character in random_number_par:
            number_cows += 1
    
    bull_bulls = "bulls"
    cow_cows = "cows"
    if number_bulls == 1:
        bull_bulls = "bull"
    if number_cows == 1:
        cow_cows = "cow"
    print(f"{number_bulls} {bull_bulls}, {number_cows} {cow_cows}\n{line_simple}")
    
def final_evaluation(number_attempts_par: int, guessed_number_par: str, 
                     start_substract_par: float, end_substract_par: float) -> str:
    '''
    Description:
    User function with game statistics.
    '''
    duration = end_substract_par - start_substract_par
    print(f"End of the game: {time_for_print()}\n{line_simple}")    # Time - end of the game:
    print(f"Correct, {guessed_number_par} is the right number!!!")
    print(f"Attempts: {number_attempts_par}, Duration: {round(duration, 1)} seconds")
    print(f"Game over !!!\n{line_double}")

if __name__ == '__main__':
    main()