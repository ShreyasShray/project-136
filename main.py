import csv

temp_star_data = []
data = []

with open("final.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        row.pop(0)
        temp_star_data.append(row)

headers = temp_star_data[0]
star_data_rows = temp_star_data[1:]

# print(star_data_rows)

for star_data in star_data_rows:
    temp_dict = {
        "name":star_data[0],
        "distance":star_data[1],
        "mass":star_data[2],
        "radius":star_data[3],
        "gravity":star_data[4]
    }
    data.append(temp_dict)

print(data)