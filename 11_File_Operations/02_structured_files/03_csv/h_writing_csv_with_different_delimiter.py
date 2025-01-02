#!/usr/bin/python
"""
Purpose: Writing csv using csv module

"""
import csv

with open("fourth.csv", "w", newline="") as gh:
    header_names = ("sno", "name", "age", "designation")
    writer = csv.writer(gh, delimiter="/")

    # To write the headers
    writer.writerow(header_names)

    # print(dir(writer))
    writer.writerow([1, "akhila", 11, "carpenter"])
    writer.writerows([[2, "hiral", 12, "software"], [1, "neha", 13, "business"]])
    gh.close()


# assignment - create csv files with all possible delimiters and read the content also
