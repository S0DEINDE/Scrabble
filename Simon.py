import os
import random
import time


# Clear the game
def clear_the_area():
    os.system('cls' if os.name == 'nt' else 'clear')


# Show High-score
def show_me():
    print(f"High Score: {highscore} by {highname}")


# Show Player's Current Score
def show_current():
    print(f"Score: {score}")


# Add Color to Simon's Sequence
def adder():
    global simons_colors
    simons_colors += random.choice(colors)


# Your Turn
def user_time():
    turn = input("Your turn:\n").upper()
    return turn


# Get High Score as Number
def getter():
    with open("highscore.txt", "r") as hs:
        stats = hs.readlines()
    return stats


# Set High Score and Name
def setter(n, s):
    with open("highscore.txt", "w") as hs:
        hs.write(f"{n}\n{s}")


# Create highscore file if none
try:
    getter()
except:
    with open("highscore.txt", "w") as f:
        f.write("null\n0")

# High Score Values
record = getter()
highname = record[0]
highscore = int(record[1])

# Possible Colors in Sequence
colors = ('R', 'G', 'B', 'Y')

# Simon's Sequence
simons_colors = []

# Tracks Player's Score
score = 0

# Initialize Simon's Sequence
for i in range(2):
    adder()

# Show High Score
clear_the_area()
show_me()
time.sleep(2)

# Show Player Score
clear_the_area()
show_current()
time.sleep(2)

# Gameplay Loop
while True:

    # Add Color to Sequence
    adder()

    # Combine Simon's Colors into Sequence
    sequence = ''.join(simons_colors)

    # Show Simon before printing sequence
    print("Simon says:")
    time.sleep(1)
    clear_the_area()
    show_current()

    # Show One Color at a Time
    for color in simons_colors:
        # Pause Between Colors
        print("Simon says:")
        time.sleep(0.1)
        clear_the_area()
        show_current()

        # Display Next Color
        print(f"Simon says: {color}")
        time.sleep(1)
        clear_the_area()
        show_current()

    # Correct Sequence from Player
    if user_time() == sequence:

        # Increase Score
        score += 1
        clear_the_area()
        show_current()

    # Game Over
    else:

        # New High Score
        if score > highscore:

            # Display High Score Message
            clear_the_area()
            print(f"GAME OVER\nNew High Score: {score}!")

            # Get player's name
            name = input("Wass ya name? ")

            # Save new high score
            setter(name, str(score))
            break

        # No New High Score
        else:

            # Display Game Over Message
            clear_the_area()
            print("GAME OVER")

            # Show High Score
            show_me()

            # Show Player Score
            print(f"Score: {score}")
            break
