# # import os
# import json
import csv

file_path = "brocode/input.csv"

try:
    with open(file_path, "r") as file:
        # content = file.read()
        content = csv.reader(file)
        for line in content:
            print(line)
        # print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read that file")
