# *****************************************
# Shadows Snake Patchnotes File
# *****************************************

# Import the json module
import json, traceback

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
filename = "patchnotes.json"
try:
    with open(filename, "w") as file:
        json.dump(patchnotes, file)
except Exception as e:
            traceback.print_exc(e)

# Read the patchnotes from the JSON file
try:
    with open(filename, "r") as file:
        patchnotes = json.load(file)
except Exception as e:
            traceback.print_exc(e)

# Print the patchnotes


# *****************************************
# Shadows Snake Patchnotes File
# *****************************************