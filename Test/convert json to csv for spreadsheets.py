import json, csv, os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Load colors from JSON file
with open(os.path.join(script_dir, 'colors.json'), 'r') as f:
    COLORS_DICT = json.load(f)

with open("E:\Codes python\Snake working games\Snake working games\Work_InProgress_Snake\Current files/colors_csv.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["color name", "hex value"])
    for color, hex in COLORS_DICT.items():
        writer.writerow([color, hex])

