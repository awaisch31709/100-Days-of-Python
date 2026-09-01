# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
# # print(travel_log["France"][1])
# print(travel_log[France.index(1)])

# nested_list = ['france', 'germany' ,['belgium','netherlands']]
# print(nested_list[0])
travel_log = {
    "france": {
        "city": "France",
        "visits": 8,
    },
    "germany": {
        "city": ["Germany", "Nakki", "Dina"],
        "visits": 10
    }
}

print(travel_log["germany"]["city"][1])