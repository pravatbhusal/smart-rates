import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from smart_rates import get_car_info

app = Flask(__name__)
CORS(app)

# global variable to save our access_token
access = None

client = smartcar.AuthClient(
    client_id='',
    client_secret='',
    redirect_uri='http://localhost:80/exchange',
    scope=['read_vehicle_info'],
    test_mode=True
)


@app.route('/login', methods=['GET'])
def login():
    auth_url = client.get_auth_url()
    return redirect(auth_url)


@app.route('/exchange', methods=['GET'])
def exchange():
    code = request.args.get('code')

    # access our global variable and store our access tokens
    global access

    # grab the access code and redirect the user to the client
    access = client.exchange_code(code)
    return "<h3>Reload the Smart Rates client application now.</h3>"


@app.route('/vehicles', methods=['GET'])
def vehicles():
    # access our global variable to retrieve our access tokens
    global access

    # handle a blank access
    if access is None:
        return "{}"

    # the list of vehicle ids
    vehicle_ids = smartcar.get_vehicle_ids(
        access['access_token'])['vehicles']

    # add all vehicles into a dictionary
    vehicles = {}
    for vehicle in vehicle_ids:
        vehicle_obj = smartcar.Vehicle(vehicle, access['access_token'])
        info = vehicle_obj.info()
        vehicles[len(vehicles)] = get_car_info(
            info["make"], info["model"], str(info["year"]), length=5)

    return jsonify(vehicles)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
