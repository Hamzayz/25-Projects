import requests
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

load_dotenv()

def get_weather(location):
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    url = f"{base_url}/{location}/today"
    
    params = {
        "key": os.getenv("WEATHER_API"),
        "unitGroup": "metric",
        "include": "days,current",
        "elements": "temp,precip,precipprob,windspeed,conditions"
    }
    
    response = requests.get(url, params=params)
    return response.json()

def check_alerts(data, location):
    current = data.get('currentConditions', data['days'][0])
    alerts = []
    
    # Rain alert
    if current.get('precipprob', 0) > 50:
        alerts.append(f"🌧️ {current['precipprob']}% chance of rain - Bring an umbrella!")
    
    # Temperature alerts
    if current['temp'] < 0:
        alerts.append(f"🥶 Freezing! Temperature: {current['temp']}°C")
    elif current['temp'] > 35:
        alerts.append(f"🥵 Very hot! Temperature: {current['temp']}°C")
    
    # Wind alert
    if current.get('windspeed', 0) > 40:
        alerts.append(f"💨 Strong winds: {current['windspeed']} km/h")
    
    return alerts

def send_email(alerts, location):
    if not alerts:
        print("No weather alerts today!")
        return
    
    # Setup email (use Gmail or any SMTP)
    sender_email = os.getenv("EMAIL")
    sender_password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    
    message = MIMEText(f"Weather Alerts for {location}:\n\n" + "\n".join(alerts))
    message['Subject'] = f"⚠️ Weather Alert - {location}"
    message['From'] = sender_email
    message['To'] = receiver_email
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(message)
        print("✅ Alert sent!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Run daily with cron job or Task Scheduler
if __name__ == "__main__":
    location = "London,UK"
    data = get_weather(location)
    alerts = check_alerts(data, location)
    
    if alerts:
        print("\n".join(alerts))
        # send_email(alerts, location)  # Uncomment to enable email


