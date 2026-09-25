import requests
from datetime import datetime

USERNAME ="awais917"
TOKEN = "ksmspwxmas"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Running graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url = graph_endpoint,json = graph_config,headers = headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today =datetime.now()

pixel_data = {

    "quantity":"4.5",
    "date": today.strftime("%Y%m%d"),


}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_creation_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity":"4.5",
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)
