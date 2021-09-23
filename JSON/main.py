import json

car_data = {"name": "Tesla",
            "engine": "electric"}

# print(car_data)
# print(type(car_data))

# json.dumps()      # It is used to write a Python object into a JSON String
# json.dump()       # It is used to write a Python object into a file as a JSON formatted data

car_data_json_string = json.dumps(car_data)
# print(car_data_json_string)
# print(type(car_data_json_string))
#
# with open("new_json_file.json", "w") as jsonfile:
#     json.dump(car_data, jsonfile)

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car["name"])
    print(car["engine"])