#!/usr/bin/env python
"""Setup script - automatically downloads all project data"""

import pandas as pd
import os
import sys

def download_data():
    """Downloads all necessary data for the project (demand, solar, wind)"""
    
    # Create data folders if they don't exist
    os.makedirs("data/Load", exist_ok=True)
    os.makedirs("data/Ireland_En_DH", exist_ok=True)
    
    print("=" * 60)
    print("DOWNLOADING PROJECT DATA")
    print("=" * 60)
    
    # Check if demand data already exists
    demand_file = "data/Load/time_series_60min_singleindex.csv"
    
    if os.path.exists(demand_file):
        print("\n[1/1] Checking demand data...")
        print(f"     ✓ Demand data already exists: {demand_file}")
        print("\n" + "=" * 60)
        print("✓ DATA ALREADY DOWNLOADED")
        print("=" * 60)
        return True
    
    try:
        # Download electricity demand data
        print("\n[1/1] Downloading electricity demand (this takes ~5 minutes)...")
        url_demand = "https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv"
        df_demand = pd.read_csv(url_demand)
        df_demand.to_csv(demand_file, index=False)
        print("     ✓ Demand data downloaded (125 MB)")
        
    except Exception as e:
        print(f"     ✗ Error downloading demand: {e}")
        print("     Please download manually from:")
        print("     https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv")
        return False
    
    print("\n" + "=" * 60)
    print("✓ DATA DOWNLOAD COMPLETED")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = download_data()
    sys.exit(0 if success else 1)