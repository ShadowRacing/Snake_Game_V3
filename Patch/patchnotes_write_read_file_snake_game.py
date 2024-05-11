# *****************************************
# Shadows Snake Patchnotes File
# *****************************************

"""
Module for managing the patchnotes of the Shadows Snake game.
"""

# Import the json module
import json
import traceback

# Define the patchnotes list
patchnotes = [
    {
        "version": "1.0",
        "changes": [
            "Added feature X",
            "Fixed bug Y",
            "Improved performance"
        ]
    },
    {
        "version": "1.1",
        "changes": [
            "Added feature Z",
            "Fixed bug X",
            "Improved performance"
        ]
    }
]

# Save the patchnotes to a JSON file
FILENAME = "patchnotes.json"
try:
    with open(FILENAME, "w", encoding='utf-8') as file:
        json.dump(patchnotes, file)
except FileNotFoundError as e:
    traceback.print_exc(e)

# Read the patchnotes from the JSON file
try:
    with open(FILENAME, "r", encoding='utf-8') as file:
        patchnotes = json.load(file)
except FileNotFoundError as e:
    traceback.print_exc(e)

# Print the patchnotes


# *****************************************
# Shadows Snake Patchnotes File
# *****************************************
