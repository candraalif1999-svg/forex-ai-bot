# calendar.py
import requests
import os

def get_economic_calendar():
    api_key = os.getenv("ALPHA_VANTAGE_API")
    url = f"https://www.alphavantage.co/query?function=ECONOMIC_CALENDAR&apikey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json().get("data", [])
        events = []
        for ev in data:
            if ev.get("impact") == "High":  # Hanya high impact
                events.append({
                    "country": ev.get("country", "Global"),
                    "event": ev.get("event", "No Event"),
                    "time": ev.get("date", "").split("T")[1][:5] if "T" in ev.get("date", "") else "N/A",
                    "impact": ev.get("impact")
                })
        return events[:5]
    except Exception as e:
        print(f"Error fetching calendar: {e}")
        return []
