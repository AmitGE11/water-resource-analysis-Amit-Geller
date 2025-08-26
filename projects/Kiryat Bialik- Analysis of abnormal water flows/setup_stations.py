#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import shutil
from pathlib import Path

def setup_station_directories():
    """
    Setup script to create station directories and validate configuration.
    """
    print("="*60)
    print("WATER STATION ANALYSIS SETUP")
    print("="*60)
    
    # Load configuration
    try:
        with open('station_config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: station_config.json not found!")
        return False
    
    base_output_dir = config['base_output_dir']
    stations = config['stations']
    
    print(f"\nBase output directory: {base_output_dir}")
    print(f"Number of stations configured: {len(stations)}")
    
    # Create base output directory if it doesn't exist
    if not os.path.exists(base_output_dir):
        print(f"\nCreating base output directory: {base_output_dir}")
        os.makedirs(base_output_dir, exist_ok=True)
    
    # Check each station
    print("\n" + "="*50)
    print("STATION STATUS CHECK")
    print("="*50)
    
    all_ready = True
    
    for station_id, station_config in stations.items():
        station_name = station_config['name']
        data_dir = station_config['data_dir']
        enabled = station_config.get('enabled', True)
        
        print(f"\n{station_name}:")
        print(f"  ID: {station_id}")
        print(f"  Data directory: {data_dir}")
        print(f"  Enabled: {enabled}")
        
        if not enabled:
            print(f"  Status: DISABLED (skipping)")
            continue
        
        # Check if data directory exists
        if os.path.exists(data_dir):
            # Count CSV files
            try:
                csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
                print(f"  Status: READY ({len(csv_files)} CSV files found)")
                if csv_files:
                    print(f"  Files: {', '.join(csv_files[:3])}{'...' if len(csv_files) > 3 else ''}")
            except Exception as e:
                print(f"  Status: ERROR accessing directory - {str(e)}")
                all_ready = False
        else:
            print(f"  Status: MISSING DATA DIRECTORY")
            print(f"  Action: Please create directory and add CSV files")
            all_ready = False
        
        # Create station output directory
        station_output_dir = os.path.join(base_output_dir, station_name.replace(' ', '_'))
        if not os.path.exists(station_output_dir):
            print(f"  Creating output directory: {station_output_dir}")
            os.makedirs(station_output_dir, exist_ok=True)
    
    # Check rain data directory
    rain_data_dir = config['rain_data_dir']
    print(f"\nRain data directory: {rain_data_dir}")
    if os.path.exists(rain_data_dir):
        try:
            rain_files = [f for f in os.listdir(rain_data_dir) if f.endswith('.csv')]
            print(f"Status: READY ({len(rain_files)} CSV files found)")
            if rain_files:
                print(f"Files: {', '.join(rain_files)}")
        except Exception as e:
            print(f"Status: ERROR accessing directory - {str(e)}")
            all_ready = False
    else:
        print("Status: MISSING RAIN DATA DIRECTORY")
        all_ready = False
    
    print("\n" + "="*50)
    if all_ready:
        print("✅ SETUP COMPLETE - All stations ready for analysis!")
        print("\nTo run the analysis:")
        print("  python water_station_analyzer.py")
    else:
        print("❌ SETUP INCOMPLETE - Please fix the issues above")
        print("\nCommon fixes:")
        print("  1. Create missing data directories")
        print("  2. Add CSV files to station directories")
        print("  3. Update paths in station_config.json if needed")
        print("  4. Set 'enabled': false for stations you don't want to analyze")
    
    print("="*50)
    return all_ready

def create_sample_structure():
    """
    Create sample directory structure for demonstration.
    """
    print("\nCreating sample directory structure...")
    
    base_dir = r"C:\Users\AmitGeller\Desktop\Yaron Geller\Water_Analysis"
    
    # Create sample station directories
    sample_stations = ["חרושת דרום", "חרושת צפון", "יוסף לוי", "יוסף לוי מערב", "מאסף שפרעם", "שוחת אצל - הבנים", "שוחת כניסה לתש קדמת ביאליק"]
    
    for station in sample_stations:
        station_dir = os.path.join(base_dir, station)
        if not os.path.exists(station_dir):
            os.makedirs(station_dir, exist_ok=True)
            print(f"Created: {station_dir}")
            
            # Create a sample README file
            readme_content = f"""# {station} Data Directory

This directory should contain CSV files with water level measurements.

Expected CSV format:
- Date column
- Time column  
- Water level column (or numeric column with level data)

Example files:
- January.csv
- February.csv
- March.csv
- etc.

Each CSV should contain measurements for one month.
"""
            readme_path = os.path.join(station_dir, "README.txt")
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
    
    print("\nSample structure created!")
    print("Please add your CSV data files to each station directory.")

if __name__ == "__main__":
    print("Water Station Analysis Setup")
    print("Choose an option:")
    print("1. Check current setup")
    print("2. Create sample directory structure")
    print("3. Both")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice in ['1', '3']:
        setup_station_directories()
    
    if choice in ['2', '3']:
        create_sample_structure()
    
    if choice not in ['1', '2', '3']:
        print("Invalid choice. Running setup check...")
        setup_station_directories()
