import csv
name_1 = "Anna"
name_2 = "Victor"

with open("data.csv", "w") as fi:
    wr = csv.writer(fi)
    wr.writerow(
        [name_1, name_2]
    )
