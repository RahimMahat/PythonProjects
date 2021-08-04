#!/usr/bin/env python3
# Reading csv with file io
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# Reading csv with in-built csv module and extracting only temperature as int
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             tmp = int(row[1])
#             temp.append(tmp)
#     print(temp)

# Pythonic way of reading csv with pandas extracting temp
import pandas as pd
data = pd.read_csv("weather_data.csv")
print(data["temp"])
