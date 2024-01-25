import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

@app.route('/weather', methods=['GET'])
def get_weather_info():
    api_key = "867d235047c605557fcb3b632bbf73cc"
    city = request.args.get('city', default='', type=str)

    if city:
        weather_data = get_weather(api_key, city)
        if weather_data:
            temperature = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            return jsonify({"city": city, "temperature": temperature, "description": description})
        else:
            return jsonify({"error": "Unable to fetch weather data for the specified city"}), 404
    else:
        return jsonify({"error": "City parameter is missing"}), 400

if __name__ == "__main__":
    app.run(debug=True)
