#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


miessage = 'In order to watch this movie...'

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your connection speed in Mbps?"))

# if input value was higher or equal to 25
if connection >= 25:
    message = message + 'You must have Starlink or not live in the sticks'
elif connection >= 5:
    message = message + 'You must have Viasat.'
elif connection >= 2:
    message = message + 'You poor soul, you must have Hughes:net.'
else:
    message = message + "I'm sorry"
print(message)
