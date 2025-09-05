# XY Automation - Coordinate Processing & Elevation Data

A Python automation script for processing XY coordinates, converting coordinate reference systems, and retrieving elevation data for water resource management applications.

## Overview

This project automates the process of:
- Converting XY coordinates from Israel Transverse Mercator (ITM) to WGS84 latitude/longitude
- Retrieving elevation data from Open-Elevation API
- Processing Excel files with coordinate data
- Generating enhanced datasets with elevation information

## Features

- **Coordinate System Conversion**: Converts coordinates from EPSG:2039 (ITM) to EPSG:4326 (WGS84)
- **Elevation Data Retrieval**: Fetches elevation data using the Open-Elevation API
- **Excel File Processing**: Reads and processes Excel files with coordinate data
- **Flexible CRS Support**: Configurable source and target coordinate reference systems
- **Progress Tracking**: Real-time progress indicators during data processing
- **Error Handling**: Robust error handling with fallback mechanisms

## Requirements

### Python Dependencies
```bash
pip install pandas requests pyproj openpyxl
```

### Required Packages
- `pandas` - Data manipulation and Excel file handling
- `requests` - HTTP requests for elevation API
- `pyproj` - Coordinate reference system transformations
- `openpyxl` - Excel file reading/writing support

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure your Excel file is in the correct format (see Input Format section)

## Usage

### Basic Usage
```bash
python x_y_automation.py
```

### Input File Format
The script expects an Excel file (`x_y_cord.xlsx`) with the following columns:
- `X (m)` - X coordinates in meters
- `Y (m)` - Y coordinates in meters
- `Elevation (Ground) (m)` - Elevation column (will be populated by the script)

### Output
The script generates:
- `x_y_cord_with_elevations.xlsx` - Enhanced Excel file with elevation data
- Console output showing processing progress and results

## Configuration

### File Paths
Update the file paths in the `main()` function:
```python
# Input file path
file_path = r"C:\Users\AmitGeller\Desktop\Yaron Geller\XY Automation\x_y_cord.xlsx"

# Output file path
output_file = r"C:\Users\AmitGeller\Desktop\Yaron Geller\XY Automation\x_y_cord_with_elevations.xlsx"
```

### Coordinate Reference Systems
The script uses these default CRS:
- **Source**: EPSG:2039 (Israel Transverse Mercator - ITM)
- **Target**: EPSG:4326 (WGS84 - World Geodetic System)

To use different CRS, modify the function call:
```python
lat, lon = convert_xy_to_latlon(x, y, source_epsg="EPSG:your_source", target_epsg="EPSG:your_target")
```

## API Information

### Open-Elevation API
- **Service**: Free elevation data service
- **Rate Limiting**: 0.1 second delay between requests
- **Timeout**: 10 seconds per request
- **Coverage**: Global elevation data

## Functions

### `convert_xy_to_latlon(x, y, source_epsg, target_epsg)`
Converts XY coordinates between coordinate reference systems.

**Parameters:**
- `x` (float): X coordinate in meters
- `y` (float): Y coordinate in meters
- `source_epsg` (str): Source CRS (default: "EPSG:2039")
- `target_epsg` (str): Target CRS (default: "EPSG:4326")

**Returns:**
- `tuple[float, float]`: (latitude, longitude) in decimal degrees

### `get_elevation_from_coordinates(lat, lon)`
Retrieves elevation data for given coordinates.

**Parameters:**
- `lat` (float): Latitude in decimal degrees
- `lon` (float): Longitude in decimal degrees

**Returns:**
- `Optional[float]`: Elevation in meters or None if failed

### `update_elevations(df)`
Processes a DataFrame to add elevation data.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with X and Y coordinates

**Returns:**
- `pd.DataFrame`: Updated DataFrame with elevation data

## Error Handling

The script includes comprehensive error handling:
- File not found errors
- API request failures
- Coordinate conversion errors
- Fallback values for failed operations

## Performance Considerations

- **API Rate Limiting**: 0.1 second delay between elevation requests
- **Progress Tracking**: Updates every 100 processed rows
- **Memory Efficient**: Processes data row by row
- **Timeout Protection**: 10-second timeout for API requests

## Example Output

```
XY Automation Script Started
Reading Excel file...
Successfully loaded Excel file!
DataFrame shape: (1000, 3)
Columns: ['X (m)', 'Y (m)', 'Elevation (Ground) (m)']

Starting elevation data collection...
Using EPSG:2039 (ITM - Israel Transverse Mercator) coordinate system
Row 0: (123456.78, 654321.09) -> (32.123456, 34.789012) -> Elevation: 45.2m
Row 1: (123457.12, 654322.34) -> (32.123457, 34.789013) -> Elevation: 46.1m
...
Processed 100/1000 rows...
```

## Troubleshooting

### Common Issues

1. **File Not Found Error**
   - Ensure the input Excel file exists at the specified path
   - Check file permissions

2. **API Connection Issues**
   - Verify internet connection
   - Check if Open-Elevation API is accessible

3. **Coordinate Conversion Errors**
   - Verify input coordinates are in the correct format
   - Check if coordinates are within the expected range

4. **Missing Dependencies**
   - Run `pip install -r requirements.txt`
   - Ensure all required packages are installed

## Contributing

This project is part of water resource management automation. For improvements or bug reports, please contact the development team.

## License

This project is developed for Yaron Geller - Planning & Management of Water Resources.

## Author

**Amit Geller**  
Data Analysis & Automation Support Specialist  
Yaron Geller - Planning & Management of Water Resources

---

*Last updated: December 2024*
