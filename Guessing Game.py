# Improting the good stuff
import random
import time
from colorama import init, Fore
import re
from tkinter import * 
from tkinter import messagebox
import keyboard

#. Initializes Colorama
init(autoreset=True)

# * Initializing The Game Variabels.
Retries = 10
Time = 2
Tries = 0
special_chars = re.compile('[@_!#$%^&*()<>?/\|}`{~:]')

# / Defining the countdown function when winning/losing.
def countdown(Time):
    while Time:
        mins, secs = divmod(Time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        Time -= 1  


# * Print out the credits.
print(Fore.BLUE + 
"                                           *********************************\n"                                                        
"                                           *       The Guessing Game       *")
print(Fore.YELLOW + "                                           *      Made by - Almog Beni     *\n"
"                                           *********************************\n")

# * Print out the instructions.
print(                                    
"                                              The instructions are simple.\n"
"                                    Your'e playing against the computer a guessing game\n"
"                                        If you guessed the number right - YOU WIN")
print(Fore.RED + "                                                    Else - YOU LOSE.")
print("                                                       Good Luck!\n")



# ! Game loop.
while True:
    try:
        keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
        try:
            Computer = random.randint(0,20)
            User_input = input("Please enter a number between 0 and 20: ")
            while (special_chars.search(User_input) != None) or User_input == '+' or re.search('[a-zA-Z]', User_input):
                print(Fore.LIGHTYELLOW_EX + "\nInvalid. Please enter a number between 0 and 20 and not a blank input.")
                User_input = input("Please enter a number between 0 and 20: ")
            while User_input == '':
                print(Fore.LIGHTYELLOW_EX + "\nInvalid. Please enter a number between 0 and 20 and not a blank input.")
                User_input = input("Please enter a number between 0 and 20: ")
            while int(User_input) < 0 or int(User_input) > 20:
                print(Fore.LIGHTYELLOW_EX + "\nInvalid. Please enter a number between 0 and 20 and not a blank input.")
                User_input = input("Please enter a number between 0 and 20:")
            print(Fore.MAGENTA + "You chose: ", User_input.lstrip('0'))
            print(Fore.LIGHTGREEN_EX + "The computer chose: ", Computer)
            

            # / Checking if the player guessed right/or not.

            if User_input != str(Computer):
                User_input = print(Fore.LIGHTRED_EX + "You didn't guessed the number correctly!\n")
                Retries -= 1
                Tries += 1
                print("Retries left:", Retries)
                if Retries == 1:
                    print(Fore.RED + "One last chance!")

                # ! Player lost.
                if Retries == 0:
                    print(Fore.LIGHTRED_EX + "Out of chances.\n"
                    "Game Over!\n")
                    check = input("Do you want to quit or start again? \n"
                    "enter Y to restart or another key to end: ")
                    if check == 'Y':
                        Retries = 10
                        continue
                    print(Fore.LIGHTMAGENTA_EX + "Bye Bye. Exiting in 2 seconds..")
                    countdown(Time)   
                    break

            # * Player won the game.
            elif User_input == str(Computer): 
                print(Fore.YELLOW + "You guessed the number correctly. ")
                print(Fore.LIGHTBLUE_EX + "You did it in",Tries, Fore.LIGHTBLUE_EX + "Tries.")
                print(Fore.LIGHTWHITE_EX + "Great Job! :)\n")
                Flag = False
            
                check = input("Do you want to quit or start again? \n"
                "enter Y to restart or another key to end: ")
                if check == 'Y':
                    Retries = 10
                    continue
                print(Fore.LIGHTMAGENTA_EX + "Bye Bye. Exiting in 2 seconds..")
                countdown(Time)   
                break
        except ValueError:
            print(Fore.LIGHTYELLOW_EX + "\nInvalid. Please enter a number between 0 and 20 and not a blank input.")
    except KeyboardInterrupt:
        print(Fore.RED + "You can't stop me.")