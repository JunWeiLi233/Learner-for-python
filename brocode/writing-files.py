import json
import csv

#txt_data = "I like python"
#employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# employee = {
#     "name" : "Spongebob",
#     "age": 30,
#     "job": "cook"
# }

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientists"]]
file_path = "brocode/output.csv"

try:
    with open(file=file_path, mode="w", newline="") as file:
        # for employee in employees:
        #     file.write(employee + "\n")
        # json.dump(employee, file, indent=4)

        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)

        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
