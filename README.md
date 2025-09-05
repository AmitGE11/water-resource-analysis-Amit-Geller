# Data Analysis & Automation – Water Resource Management

**Amit Geller**

This repository showcases my work as a Data Analysis & Automation Support Specialist at Yaron Geller - Planning & Management of Water Resources. The repo contains Python projects and scripts designed to analyze real-world water supply data, automate data preparation, and produce clear, decision-support visualizations for engineers.

## About the Work

- Retrieve live project data (CSV/Excel) from the water industry (facility inflows, water levels, supply monitoring, etc)
- Automate data processing and analysis workflows
- Generate engineering reports and visualizations
- Support infrastructure planning and water resource management decisions

## Projects

### XY Automation - Coordinate Processing & Elevation Data

**Location**: `projects/xy-automation/`

This project automates the process of retrieving ground elevation values for coordinates provided in ITM (Israel Transverse Mercator, EPSG:2039). It was developed to support water infrastructure projects, where engineers receive CSV files containing X/Y coordinates of sewage pipe junctions.

Previously, the lead engineer had to manually search each coordinate in Google Earth to determine elevation values and then update the dataset. This script eliminates that manual effort by converting ITM coordinates to latitude/longitude, querying an elevation API, and updating the CSV automatically.

#### Features

- Converts ITM coordinates (EPSG:2039) → WGS84 latitude/longitude (EPSG:4326)
- Retrieves ground elevation for each point using an external elevation API
- Updates the original CSV with a new Elevation (Ground) column
- Saves time and reduces errors compared to manual lookup
- Scalable to handle large engineering datasets

#### How It Works

**Input**: CSV with the following columns:
- X (m) – Easting (ITM)
- Y (m) – Northing (ITM)

**Processing**:
- Transform coordinates with pyproj
- Query the elevation API for each converted (lat, lon) pair
- Append results to the dataset

**Output**:
- A new CSV with an extra column: Elevation (Ground) (m)

#### Tech Stack

- Python
- Pandas – CSV parsing & data manipulation
- NumPy – numerical support
- PyProj – coordinate transformation (ITM → WGS84)
- Requests – elevation API integration

#### Example

**Input CSV**:
```
Label	X (m)	Y (m)	ID
MH-398	206190.57	745708.35	4444
```

**Output CSV (after script run)**:
```
Label	X (m)	Y (m)	ID	Elevation (Ground) (m)
MH-398	206190.57	745708.35	4444	3.0
```

#### Impact

- Reduced task time from hours of manual work to seconds of automated processing
- Improved data accuracy and consistency for engineering decision-making
- Streamlined the workflow for generating sewage pipe flow maps

---

*For detailed documentation and usage instructions, see the individual project README files in each project folder.*