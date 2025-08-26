# Professional Water Station Analysis System

A scalable, configuration-driven water level analysis system that can handle multiple monitoring stations efficiently.

## 🎯 Why This Professional Approach?

### ✅ **Single File, Multiple Stations**
- **One codebase** to maintain
- **Consistent analysis** across all stations
- **Easy updates** and bug fixes
- **Professional logging** and error handling

### ✅ **Configuration-Driven**
- **JSON configuration** for easy station management
- **Enable/disable stations** without code changes
- **Custom thresholds** per station
- **Flexible paths** and settings

### ✅ **Scalable Architecture**
- **Object-oriented design** for maintainability
- **Modular functions** for reusability
- **Professional logging** for debugging
- **Error handling** for robustness

## 📁 File Structure

```
water_analysis/
├── water_station_analyzer.py    # Main analysis engine
├── station_config.json          # Station configuration
├── setup_stations.py            # Setup and validation script
├── Hans_Moller.py              # Original single-station script (for reference)
└── README.md                   # This file
```

## 🚀 Quick Start

### 1. Setup and Validation
```bash
python setup_stations.py
```

This will:
- Check all station directories
- Validate CSV files
- Create output directories
- Show setup status

### 2. Configure Your Stations
Edit `station_config.json` to match your actual station paths:

```json
{
    "stations": {
        "hans_moller": {
            "name": "Hans Moller",
            "data_dir": "C:\\Users\\AmitGeller\\Desktop\\Yaron Geller\\Water_Analysis\\הנס מולר",
            "threshold": 0.5,
            "enabled": true
        },
        "your_station_2": {
            "name": "Your Station 2",
            "data_dir": "C:\\path\\to\\your\\station2\\data",
            "threshold": 0.5,
            "enabled": true
        }
    }
}
```

### 3. Run Analysis
```bash
python water_station_analyzer.py
```

## 📊 What You Get

For each station, the system creates:

### 📈 **Charts (2 versions per month)**
- **Dots version**: Rain data as scatter points
- **Bars version**: Rain data as bars
- **Water level trends** with threshold highlighting
- **Rain correlation** visualization

### 📋 **Excel Analysis File**
- **All_Measurements**: Complete dataset
- **High_Levels**: Readings above threshold
- **Statistics**: Summary statistics
- **Charts**: Embedded visualizations

### 📁 **Organized Output**
```
Water_Analysis/
├── Hans_Moller/
│   ├── Hans_Moller_Analysis.xlsx
│   └── charts/
├── Station_2/
│   ├── Station_2_Analysis.xlsx
│   └── charts/
└── ...
```

## ⚙️ Configuration Options

### Station Settings
- `name`: Display name for the station
- `data_dir`: Path to CSV files
- `threshold`: Water level threshold (default: 0.5m)
- `enabled`: Enable/disable analysis
- `description`: Optional description

### Analysis Settings
- `chart_dpi`: Chart resolution (default: 300)
- `chart_figsize`: Chart dimensions
- `cleanup_temp_files`: Auto-cleanup (default: true)
- `logging_level`: Log detail level

## 🔧 Advanced Usage

### Analyze Specific Stations Only
```python
# In station_config.json, set enabled: false for stations you don't want
"station_3": {
    "enabled": false  # This station will be skipped
}
```

### Custom Thresholds
```python
# Different thresholds for different stations
"station_1": {
    "threshold": 0.3  # Lower threshold
},
"station_2": {
    "threshold": 0.7  # Higher threshold
}
```

### Batch Processing
```python
# The system automatically processes all enabled stations
# No need to run separate scripts for each station
```

## 🆚 Comparison: Professional vs. Multiple Files

| Aspect | Professional Approach | Multiple Files |
|--------|---------------------|----------------|
| **Maintenance** | ✅ One codebase | ❌ 8+ files to maintain |
| **Consistency** | ✅ Same analysis logic | ❌ Risk of inconsistencies |
| **Updates** | ✅ Fix once, apply everywhere | ❌ Update each file |
| **Configuration** | ✅ JSON config | ❌ Hard-coded paths |
| **Scalability** | ✅ Easy to add stations | ❌ Manual file creation |
| **Error Handling** | ✅ Centralized logging | ❌ Scattered error handling |
| **Testing** | ✅ Test once | ❌ Test each file |

## 🛠️ Troubleshooting

### Common Issues

1. **"Directory not found"**
   - Check paths in `station_config.json`
   - Run `setup_stations.py` to validate

2. **"No CSV files found"**
   - Ensure CSV files are in station directories
   - Check file extensions (.csv)

3. **"Error processing CSV"**
   - Verify CSV format (Date, Time, Level columns)
   - Check for encoding issues

### Debug Mode
```python
# Set logging level to DEBUG in station_config.json
"logging_level": "DEBUG"
```

## 📈 Performance Benefits

- **Parallel processing** ready (can be extended)
- **Memory efficient** (processes one station at a time)
- **Automatic cleanup** of temporary files
- **Professional logging** for monitoring

## 🔮 Future Enhancements

The modular design makes it easy to add:
- **Parallel processing** for faster analysis
- **Database integration** for large datasets
- **Web interface** for configuration
- **Email notifications** for high water levels
- **Real-time monitoring** capabilities

## 📞 Support

This professional system is designed to be:
- **Self-documenting** with clear code structure
- **Easy to modify** with configuration files
- **Robust** with comprehensive error handling
- **Scalable** for future growth

---

**Recommendation**: Use this professional approach for all 8 stations. It's the industry standard for multi-station analysis systems.
