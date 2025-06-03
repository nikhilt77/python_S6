import requests

def get_live_flights():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for flight in data["states"][:20]:  # First 10 entries 
            print({
                "ICAO24": flight[0],
                "Callsign": flight[1].strip() if flight[1] else "N/A",
                "Country": flight[2],
                "Latitude": flight[6],
                "Longitude": flight[5],
                "Altitude": flight[7],
                "Velocity": flight[9],
                "On Ground": flight[8]
            })
    else:
        print("Error fetching data:", response.status_code)

get_live_flights()
