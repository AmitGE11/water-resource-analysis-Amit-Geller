#  Jerusalem Water Supply Analysis

This project analyzes measurements of water flowing into various **water facilities in Jerusalem**, with the goal of supporting engineering decisions through clear **data visualizations** and **statistical insights**.

Developed for the **lead water resources engineer**, this tool helps evaluate flow behavior, detect patterns, and guide operational planning based on real-world data from multiple facility locations.

---

##  Project Objectives

-  **Ingest** and process water flow data collected from multiple supply stations in Jerusalem.
-  **Visualize** water flow over time — daily, monthly, and per location.
-  **Compare water behavior** across weekdays (e.g., Monday vs. Saturday) and weekend windows.
- **Export actionable insights** to Excel reports with embedded graphs for stakeholders and engineers.

---

##  Folder Structure

```
projects/
└── jerusalem_water_supply/
├── Jerusalem_water_supply.py # Main plotting and export logic
├── mon_vs_sat.py # Weekday comparison and statistics
├── water_supply_monthly_plots.xlsx # Output Excel with plots
├── water_supply_plot.png # Overview image of all flows
└── [Excel/CSV input files] # Raw water measurement files
```

---

##  Key Features

### `Jerusalem_water_supply.py`:
- Reads Excel files from multiple Jerusalem water facilities.
- Smooths and plots water flow over time.
- Generates:
  - Full timeline plots
  - Monthly plots
  - Individual location plots
  - Four "Thursday–Saturday" operational windows
- Outputs all graphs to a **single Excel report**.

### `mon_vs_sat.py`:
- Aggregates and compares water levels for **Mondays vs. Saturdays** to the rwquest of the leading engineer.
- Calculates:
  - Overall and daytime averages
  - Monthly breakdowns
  - Hourly patterns
- Exports the analysis to **Excel with visuals and stats**.
- Prints summary of percentage differences between weekdays.

---

##  Technologies Used

- `pandas` for data cleaning and analysis  
- `matplotlib` and `seaborn` for visualizations  
- `openpyxl` for exporting graphs into Excel files  
- Python 3.8+

Install dependencies:
```bash
pip install pandas matplotlib seaborn openpyxl
```

---

##  Output Highlights

- Water flow graphs over time for all locations
- Separate monthly visualizations
- Statistical comparison of weekdays (Monday vs. Saturday)
- Operational window (Thursday–Saturday) flow snapshots
- Excel reports (.xlsx) with embedded visuals for engineer review

---

##  Example Use Case

The lead engineer at a Jerusalem water resource firm can use this project to:

- Understand facility-specific behavior over time
- Compare weekdays vs. weekends for maintenance planning
- Identify anomalies or irregularities before they escalate
- Present visual summaries to municipalities or contractors
