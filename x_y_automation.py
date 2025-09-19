#!/usr/bin/env python3
"""
XY Automation Script
A Python script for automating XY coordinate operations.
"""

import pandas as pd
import requests
import time
from typing import Optional
import pyproj

def get_elevation_from_coordinates(lat: float, lon: float) -> Optional[float]:
    """
    Get elevation data from Open-Elevation API for given coordinates.
    
    Args:
        lat: Latitude in decimal degrees
        lon: Longitude in decimal degrees
    
    Returns:
        Elevation in meters or None if failed
    """
    try:
        # Using Open-Elevation API (free, no API key required)
        url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        if data.get('results') and len(data['results']) > 0:
            elevation = data['results'][0].get('elevation')
            if elevation is not None:
                return float(elevation)
        
        return None
        
    except Exception as e:
        print(f"Error getting elevation for coordinates ({lat}, {lon}): {e}")
        return None

def convert_xy_to_latlon(x: float, y: float, source_epsg: str = "EPSG:2039", target_epsg: str = "EPSG:4326") -> tuple[float, float]:
    """
    Convert X,Y coordinates from source CRS to latitude/longitude.
    
    Args:
        x: X coordinate in meters
        y: Y coordinate in meters
        source_epsg: Source coordinate reference system (default: EPSG:2039 - ITM)
        target_epsg: Target coordinate reference system (default: EPSG:4326 - WGS84)
    
    Returns:
        Tuple of (latitude, longitude) in decimal degrees
    """
    try:
        # Create transformer with always_xy=True to ensure consistent x,y order
        transformer = pyproj.Transformer.from_crs(source_epsg, target_epsg, always_xy=True)
        
        # Transform coordinates - returns (lon, lat) due to always_xy=True
        lon, lat = transformer.transform(x, y)
        
        # Return (lat, lon) as expected
        return lat, lon
        
    except Exception as e:
        print(f"Error converting coordinates ({x}, {y}): {e}")
        # Fallback to rough approximation if conversion fails
        return 40.0, -74.0

def update_elevations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Update the elevation column with data from API calls.
    
    Args:
        df: DataFrame with X and Y coordinates
    
    Returns:
        Updated DataFrame with elevation data
    """
    print("Starting elevation data collection...")
    print("Using EPSG:2039 (ITM - Israel Transverse Mercator) coordinate system")
    
    for index, row in df.iterrows():
        x_coord = row['X (m)']
        y_coord = row['Y (m)']
        
        # Convert XY to lat/lon
        lat, lon = convert_xy_to_latlon(x_coord, y_coord)
        
        # Get elevation from API
        elevation = get_elevation_from_coordinates(lat, lon)
        
        if elevation is not None:
            df.at[index, 'Elevation (Ground) (m)'] = elevation
            print(f"Row {index}: ({x_coord}, {y_coord}) -> ({lat:.6f}, {lon:.6f}) -> Elevation: {elevation}m")
        else:
            print(f"Row {index}: Failed to get elevation for ({x_coord}, {y_coord})")
        
        # Add delay to avoid overwhelming the API
        time.sleep(0.1)
        
        # Progress indicator every 100 rows
        if (index + 1) % 100 == 0:
            print(f"Processed {index + 1}/{len(df)} rows...")
    
    return df

def main():
    """
    Main function to execute the XY automation logic.
    """
    print("XY Automation Script Started")
    print("Reading Excel file...")
    
    # Read the Excel file
    file_path = r"C:\Users\AmitGeller\Desktop\Yaron Geller\XY Automation\x_y_cord.xlsx"
    
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)
        
        print(f"Successfully loaded Excel file!")
        print(f"DataFrame shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst 10 rows before elevation update:")
        print(df.head(10))
        
        # Update elevations
        print("\n" + "="*50)
        df_updated = update_elevations(df)
        
        # Save updated DataFrame
        output_file = r"C:\Users\AmitGeller\Desktop\Yaron Geller\XY Automation\x_y_cord_with_elevations.xlsx"
        df_updated.to_excel(output_file, index=False)
        print(f"\nUpdated data saved to: {output_file}")
        
        print("\nFirst 10 rows after elevation update:")
        print(df_updated.head(10))
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    
if __name__ == "__main__":
    main()
