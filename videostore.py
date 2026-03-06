"""
Program: videostore.py
Chapter 2 project (page 50)
Author: Nanette
Date: 02/13/2026

Simple app that prompts the user for the number of each rental type. Calculates and displays the grand total.
"""

# Variables and constants
NEW_VIDEOS = 3.00
OLD_VIDEOS = 2.00
GAMES = 4.00    

# Get user input
numNew = int(input("PLease enter the number of NEW rentals >> "))
numOld = int(input("Now, enter the number of OLD rentals >> "))
numGames = int(input("Here, enter the number of GAME rentals >> "))

# Processing phase
grandTotal = (numNew * NEW_VIDEOS) + (numOld * OLD_VIDEOS) + (numGames * GAMES)
grandTotal = round(grandTotal, 2)

# Output phase
print("The total charge for your rentals is $", grandTotal)

input("Press the Enter to exit.")