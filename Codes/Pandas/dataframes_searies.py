#!/usr/bin/env python3
import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(type(data))               # pandas.core.frame.DataFrame
# print(type(data["temp"]))       # pandas.core.series.Series

# converting csv to json
# data_json = data.to_json()
# print(data_json)

# series to list
# temp_list = data["temp"].to_list()
# print(temp_list)
# finding average of temperature of the week
# temp_sum = 0
# for temp in temp_list:
#     temp_sum += temp
# print(f"The average temperature of the week is: {temp_sum/len(temp_list)}")
# pythonic way of finding average of temp
# print(data["temp"].mean())      # mean is panda's series method


# get data in columns
# print(data.condition)
# get data in row
# print(data[data.day == "Monday"])
# accessing single column of row
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(f"Monday temperature in Fahrenheit is {monday_temp_f} ")


# create data frame
# data_dict = {
#     "students" : ["Amy", "James", "John"],
#     "score" : [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# print(data)
# converting dict to csv and saving in new file
# data.to_csv("new_file.csv")

################################Squirrel Data###############################################

data = pd.read_csv("Squirrel_Data.csv")
# getting count of squirrels by their colour
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

# putting that data into a python dictionary
data_dict = {
    "Fur colour": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}
# creating dataframe and making a csv file of that dataframe
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

