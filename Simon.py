import os
import random
import time

print("~~~~~~~~~~~~~~~~~SIMON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~SAYS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Function to clear the game
def clear_the_area():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to output new high-score
def show_me():
    print(f"High Score: {highscore} by {highname}")


# Function to output the current score of the user
def show_current():
    print(f"Score: {score_counter}")


# Function to add another color to Simon's sequence
def adder():
    global simons_colors
    simons_colors += random.choice(colors)


# Function to say that is now your turn
def user_time():
    turn = input("Your turn:\n").upper()
    return turn


# Function to get the current high-score
def getter():
    with open("highscore.txt", "r") as hs:
        stats = hs.readlines()
    return stats


# Function to set new high-score
def setter(n, s):
    with open("highscore.txt", "w") as hs:
        hs.write(f"{n}\n{s}")


# Try and except for using the file to reach the current high-score file
try:
    getter()
except:
    with open("highscore.txt", "w") as f:
        f.write("null\n0")

# This is for current the high-score
record = getter()
highname = record[0]
highscore = int(record[1])

# The possible colors for Simon
colors = ('R', 'G', 'B', 'Y')

# The list for Simon's colors
simons_colors = []

# The count for the user's current score
score_counter = 0

# Initialize Simon's Sequence
for i in range(2):
    adder()

# Output High Score
clear_the_area()
show_me()
time.sleep(2)

# Output the user's current score
clear_the_area()
show_current()
time.sleep(2)

# Gameplay Loop
while True:

    # call the add color function
    adder()

    # addd the colors to Simon's sequence
    sequence = ''.join(simons_colors)

    # Output the official start of the game
    print("Simon says:")
    time.sleep(1)
    clear_the_area()
    show_current()

    # Output a color at a time
    for color in simons_colors:
        # Make sure there is a pause for the user after each color Simon says
        print("Simon says:")
        time.sleep(0.1)
        clear_the_area()
        show_current()

        # Output the next color Simon says
        print(f"Simon says: {color}")
        time.sleep(1)
        clear_the_area()
        show_current()

    # Correct Sequence from Player
    if user_time() == sequence:

        # Increment the score
        score_counter += 1
        clear_the_area()
        show_current()

    # Game Over condition
    else:

        # New High-score condition
        if score_counter > highscore:

            # Output the new high-score
            clear_the_area()
            print(f"GAME OVER\nNew High Score: {score_counter}!")

            # Ask user for input of their name
            name = input("Wass ya name? ")

            # call setter function
            setter(name, str(score_counter))
            break

        # No New High Score Condition
        else:

            # Output Game Over Message
            clear_the_area()
            print("GAME OVER")

            # Output High-score
            show_me()

            # Output player score
            print(f"Score: {score_counter}")
            break
print("--------------THANKS FOR USING MY PROGRAM!------------------------------------------------------------------\n")
print()
