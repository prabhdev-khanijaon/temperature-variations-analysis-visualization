from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('weather_data/san_juan_weather_temperature_2021.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Examine the header data.
#print(header_row)

# Find out which columnds of data we need.
#for index, column_header in enumerate(header_row) :
#    print(index, column_header)

# Create a mapping of column to indexes.
header_index_map = {column: index for index, column in enumerate(header_row)}

# Set the location name.
first_row = next(reader)
station_name = first_row[header_index_map['NAME']]

# Extract dates, and high, and low temperatures.
# Error except incase of missing data.
dates, highs, lows = [], [], []
for row in reader :
    current_date = datetime.strptime(row[header_index_map['DATE']], '%Y-%m-%d')
    try :
        high = int(row[header_index_map['TMAX']])
        low = int(row[header_index_map['TMIN']])
    except ValueError :
        #print(f"Missing data for {current_date}")
        continue
    else :
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

print(highs)

# Plot the high and low temperatures.
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = f"Daily High and Low Temperatures, 2021\n{station_name}, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()