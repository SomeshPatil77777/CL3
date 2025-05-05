import csv
from datetime import datetime

weather_data = []

with open("weather_data.csv", "r") as file:
    reader = csv.DictReader(file)
    print("CSV Headers:", reader.fieldnames)  # Optional: shows the detected headers

    for row in reader:
        try:
            dt_str = row["Date_Time"].strip()
            temp = float(row["Temperature_C"].strip())
            weather_data.append((dt_str, temp))
        except Exception as e:
            print(f"Skipping row due to error: {e}, Row: {row}")
            continue

# Check if data is available
if not weather_data:
    print("No valid data found! Please check your CSV content.")
else:
    # Find coolest and hottest entries
    coolest = min(weather_data, key=lambda x: x[1])
    hottest = max(weather_data, key=lambda x: x[1])

    print("Coolest Date_Time:", coolest[0], "Average Temperature:", coolest[1])
    print("Hottest Date_Time:", hottest[0], "Average Temperature:", hottest[1])
