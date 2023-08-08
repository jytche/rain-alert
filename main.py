import requests
from twilio.rest import Client

api_key = "OWM_API_KEY"

OWM_Endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
MY_LAT = 23.810331
MY_LONG = 90.412521
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}

account_sid = "ACC_ID"
auth_token = "AUTH_TOKEN"

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["list"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Please bring an ☂️",
        from_='+TWILIO NUMBER',
        to='+ADDRESS NUMBER'
    )
    print(message.status)
