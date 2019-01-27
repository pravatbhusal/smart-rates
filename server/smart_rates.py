import requests
import json


# return the first "length" cars using its make, model, and year information
def get_car_info(make, model, year, length):
    # market check's API service
    api_key = ''
    info_api = 'http://api.marketcheck.com/v1/search?api_key=' + api_key + \
               '&year=' + year + '&make=' + make + '&model=' + model + '&car_type=used'
    headers = {
        'Host': 'marketcheck-prod.apigee.net'
    }
    # send a get request to get the information on the car
    cars = requests.request('GET', info_api, headers=headers)
    cars = json.loads(cars.text)["listings"]
    cars_dict = {}
    for car in cars:
        # set the information on each sale of the car into a dictionary
        if len(cars_dict) < length:
            try:
                name = make + " " + model + " " + year
                car_dict = {"name": name, "price": car["price"]}
                cars_dict[len(cars_dict)] = car_dict
            except:
                pass
    return cars_dict
