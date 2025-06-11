# 🌦️ Weather Data Analysis Project

This project analyzes and visualizes historical weather data from locations including **Death Valley**, **Sitka**, and **San Francisco**.  
It highlights temperature trends, daily highs/lows, and precipitation patterns using Python and Matplotlib — ideal for showcasing real-world data analysis skills.

---

## 🧠 Project Overview

- Parses and cleans weather data from CSV files.
- Visualizes daily high and low temperatures for selected locations.
- Handles missing or inconsistent data entries.
- Focuses on practical skills in **data wrangling**, **visualization**, and **error handling**.

---

## 🔍 Skills Demonstrated

- **Data Wrangling**: Extracted relevant data from raw CSV files using Python's built-in `csv` module and `Pathlib`.
- **Data Visualization**: Created line plots and filled areas to illustrate temperature ranges and rainfall using `Matplotlib`.
- **Missing Data Handling**: Implemented logic to handle incomplete datasets and avoid runtime errors.

---

## ✨ Key Features

- 📈 **Daily Temperature Trends**:
  - Visualizes high and low temperatures for:  
    - Death Valley, CA  
    - Sitka, AK  
    - San Francisco, CA

- 🌧️ **Rainfall Visualization**:
  - Plots daily rainfall levels for Sitka in 2021.

- 🛠️ **Robust to Missing Data**:
  - Gracefully handles missing or corrupt entries in real-world datasets.

---

## 🧪 Future Improvements

- 🔄 **Real-Time Data**: Integrate APIs for real-time weather updates.
- 🧭 **Interactive Visuals**: Use Plotly or Dash for enhanced interactivity.
- 🌍 **Expanded Coverage**: Add analysis for more cities and climate zones.

---

## 🗂️ Technologies Used

| Tool        | Purpose                                  |
|-------------|------------------------------------------|
| Python      | Core language for scripting and analysis |
| Matplotlib  | Data visualization (line plots, fills)   |
| CSV Module  | Reading and parsing weather data         |
| Pathlib     | File system navigation and access        |

---

## 🗺️ Data Sources

Weather data used in this project is sourced from CSV files containing daily high, low, and precipitation data for the respective cities.

---

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-data-analysis.git
cd weather-data-analysis
````

### 2. Install Dependencies

```bash
pip install matplotlib
```

### 3. Run the Scripts

Example: To visualize Death Valley temperature data:

```bash
python death_valley_highs_lows.py
```

Other available scripts include:

* `sitka_highs_lows.py`
* `san_francisco_highs_lows.py`
* `sitka_rainfall.py`

Each script will generate a corresponding weather visualization.

---

## 📌 Notes

* Built with **Python 3.x** and **Matplotlib**
* Ideal for beginners and intermediates in data science and climate data exploration
* Modular structure makes it easy to add more cities or weather metrics

---

Feel free to fork, star ⭐, or contribute!
