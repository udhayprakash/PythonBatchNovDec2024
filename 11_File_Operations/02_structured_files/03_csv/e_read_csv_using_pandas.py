"""
Purpose: Reading(Parsing) csv using pandas module

    pip install pandas
"""
import pandas as pd

# print(dir(pandas))

# Loading a csv
data_frame = pd.read_csv("my_file.csv")

# print(type(data_frame))
# print(data_frame)

# print(data_frame.head())

print(set(data_frame.name))