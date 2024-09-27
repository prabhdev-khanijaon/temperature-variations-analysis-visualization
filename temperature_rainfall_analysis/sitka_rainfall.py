from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Examine the header data.
#print(header_row)

# Find out which columnds of data we need.
#for index, column_header in enumerate(header_row) :
#    print(index, column_header)

# Extract dates, and high, and low temperatures.
dates, precipitation_values = [], []
for row in reader :
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    precipitation = float(row[5])
    dates.append(current_date)
    precipitation_values.append(precipitation)

#print(highs)

# Plot the high and low temperatures.
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, precipitation_values, color='blue', alpha=0.7)

# Format plot.
ax.set_title("Daily Precipitation, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()