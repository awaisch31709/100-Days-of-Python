# with open("weather_data.csv") as file:
#     read = file.read()
#     print(read)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.DictReader(data_file)
#     temperatures = []
#     for row in data:
#         temperature = int(row["temp"])
#         temperatures.append(temperature)
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(len(data_dict))
#
# list = data["temp"].to_list()
# print(len(list))
#
# # average = sum(list)/len(list)
# # print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in Columns
#
# print(data["condition"])
# print(data.day)
#
# #get Data in Row
# print(data[data.temp == "Monday"])
#
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# fahreneit = (data.temp[0] * 9 / 5) + 32
# print(f"Temperature in fahreneit: {fahreneit} F")

# thisdict = {
#     "brand": ["Ford", "Toyota", "Honda"],
#     "model": "Mustang",
#     "year": 1964
# }
#
# data = pandas.DataFrame(thisdict)
# print(data)


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260912.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")