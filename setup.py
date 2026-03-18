#!/usr/bin/env python
"""Setup script - automatically downloads electricity demand data"""

import pandas as pd
import os
import sys

def download_data():
    """Downloads electricity demand data for Ireland"""
    
    # Create data folder if it doesn't exist
    os.makedirs("data/Load", exist_ok=True)
    
    print("=" * 60)
    print("DOWNLOADING ELECTRICITY DEMAND DATA")
    print("=" * 60)
    
    try:
        print("\nDownloading electricity demand (this takes ~5 minutes)...")
        url = "https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv"
        df = pd.read_csv(url)
        df.to_csv("data/Load/time_series_60min_singleindex.csv", index=False)
        print("✓ Demand data downloaded successfully (125 MB)")
        
    except Exception as e:
        print(f"✗ Error downloading: {e}")
        print("Please download manually from:")
        print("https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv")
        return False
    
    print("\n" + "=" * 60)
    print("✓ DOWNLOAD COMPLETED")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = download_data()
    sys.exit(0 if success else 1)