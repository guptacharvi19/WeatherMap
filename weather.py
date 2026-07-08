import os
import json
import time
import urllib.request
import urllib.parse

# Reads API key from GitHub Secrets
API_KEY = os.environ.get('OPENWEATHER_API_KEY', 'df33e424970dd68bfcf210bb8fc12ce9')
CITIES = ["New York", "London", "Tokyo", "Bhopal", "Sydney", "Cairo"]

def fetch_weather(city):
    safe_city = urllib.parse.quote(city)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={safe_city}&appid={API_KEY}&units=metric"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            if response.status == 200:
                return json.loads(response.read().decode())
    except Exception as e:
        print(f"[{city}] Fetch Error: {str(e)}")
    return None

def main():
    print(f"==================================================")
    print(f"PIPELINE TRIGGERED AT: {time.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"==================================================")
    
    alerts = []
    for city in CITIES:
        data = fetch_weather(city)
        if not data:
            continue
            
        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        print(f"Metrics Captured -> {city}: Temp={temp}°C | Sky={condition.capitalize()}")
        
        if temp >= 40.0:
            alerts.append(f"EXTREME HEAT ADVISORY: {city} is at {temp}°C!")
        elif temp <= 0.0:
            alerts.append(f"FREEZING TEMPERATURE WARNING: {city} is at {temp}°C!")
            
    print(f"--------------------------------------------------")
    if alerts:
        print("CRITICAL METRIC ANOMALIES ENCOUNTERED:")
        for alert in alerts:
            print(alert)
    else:
        print("All tracked target environments operating within normal parameters.")
    print(f"==================================================\n")

if __name__ == "__main__":
    main()