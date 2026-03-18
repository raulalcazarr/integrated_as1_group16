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
    
    try:
        # Download electricity demand data
        print("\n[1/3] Downloading electricity demand (this takes ~5 minutes)...")
        url_demand = "https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv"
        df_demand = pd.read_csv(url_demand)
        df_demand.to_csv("data/Load/time_series_60min_singleindex.csv", index=False)
        print("     ✓ Demand data downloaded (125 MB)")
        
    except Exception as e:
        print(f"     ✗ Error downloading demand: {e}")
        print("     Please download manually from:")
        print("     https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv")
        return False
    
    try:
        # Download solar data from Renewables Ninja
        print("\n[2/3] Downloading solar data...")
        url_solar = "https://www.renewables.ninja/country_downloads/IE/ninja-pv-country-IE-national-merra2.csv"
        
        df_solar = pd.read_csv(url_solar)
        df_solar.to_csv("data/Ireland_En_DH/ninja-pv-country-IE-national-merra2.csv", index=False)
        print("     ✓ Solar data downloaded")
        
    except Exception as e:
        print(f"     ✗ Error downloading solar: {e}")
        print("     Note: Renewables Ninja may require API key registration")
        print("     Visit: https://www.renewables.ninja/")
    
    try:
        # Download onshore wind data from Renewables Ninja
        print("\n[3/3] Downloading onshore wind data...")
        url_windo = "https://www.renewables.ninja/country_downloads/IE/ninja-wind-country-IE-current_onshore-merra2.csv"
        df_windo = pd.read_csv(url_windo)
        df_windo.to_csv("data/Ireland_En_DH/ninja-wind-country-IE-current_onshore-merra2.csv", index=False)
        print("     ✓ Onshore wind data downloaded")
        
    except Exception as e:
        print(f"     ✗ Error downloading wind: {e}")
        print("     Note: Renewables Ninja may require API key registration")
        print("     Visit: https://www.renewables.ninja/")
        
    try:
        # Download offshore wind data from Renewables Ninja
        print("\n[3/3] Downloading offshore wind data...")
        url_wind = "https://www.renewables.ninja/country_downloads/IE/ninja-wind-country-IE-current_offshore-merra2.csv"
        df_wind = pd.read_csv(url_wind)
        df_wind.to_csv("data/Ireland_En_DH/ninja-wind-country-IE-current_offshore-merra2.csv", index=False)
        print("     ✓ Offshore wind data downloaded")
        
    except Exception as e:
        print(f"     ✗ Error downloading wind: {e}")
        print("     Note: Renewables Ninja may require API key registration")
        print("     Visit: https://www.renewables.ninja/")
    
    print("\n" + "=" * 60)
    print("✓ DATA DOWNLOAD COMPLETED")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = download_data()
    sys.exit(0 if success else 1)