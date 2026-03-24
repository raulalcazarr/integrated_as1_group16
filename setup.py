#!/usr/bin/env python
"""Setup script - automatically downloads all project data"""

import pandas as pd
import requests
import os
import sys

# Simulate a real browser to avoid 403 errors from renewables.ninja
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

def download_data():
    """Downloads all necessary data for the project (demand, solar, wind)"""
    
    # Create data folders if they don't exist
    os.makedirs("data/Load", exist_ok=True)
    os.makedirs("data/Ireland_En_DH", exist_ok=True)
    os.makedirs("data/Germany_En_DH", exist_ok=True)
    
    print("=" * 60)
    print("DOWNLOADING PROJECT DATA")
    print("=" * 60)
    
    all_ok = True

    # ------------------------------------------------------------------ #
    # [1/2] Electricity demand data                                        #
    # ------------------------------------------------------------------ #
    demand_file = "data/Load/time_series_60min_singleindex.csv"
    print("\n[1/2] Checking demand data...")

    if os.path.exists(demand_file):
        print(f"     ✓ Demand data already exists: {demand_file}")
    else:
        try:
            print("     Downloading electricity demand (this takes ~5 minutes)...")
            url_demand = (
                "https://data.open-power-system-data.org/time_series/2020-10-06/"
                "time_series_60min_singleindex.csv"
            )
            df_demand = pd.read_csv(url_demand)
            df_demand.to_csv(demand_file, index=False)
            print("     ✓ Demand data downloaded (125 MB)")
        except Exception as e:
            print(f"     ✗ Error downloading demand: {e}")
            print("     Please download manually from:")
            print("     https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv")
            all_ok = False

    # ------------------------------------------------------------------ #
    # [2/2] Germany onshore wind data (renewables.ninja)                  #
    # Note: requires browser-like User-Agent to avoid 403 Forbidden       #
    # ------------------------------------------------------------------ #
    wind_de_file = "data/Germany_En_DH/ninja-wind-country-DE-current_onshore-merra2.csv"
    print("\n[2/2] Checking Germany onshore wind data...")

    if os.path.exists(wind_de_file):
        print(f"     ✓ Germany wind data already exists: {wind_de_file}")
    else:
        try:
            print("     Downloading Germany onshore wind data...")
            url_wind_de = (
                "https://www.renewables.ninja/country_downloads/DE/"
                "ninja-wind-country-DE-current_onshore-merra2.csv"
            )
            response = requests.get(url_wind_de, headers=HEADERS)
            response.raise_for_status()

            with open(wind_de_file, "wb") as f:
                f.write(response.content)

            print(f"     ✓ Germany wind data downloaded → {wind_de_file}")
        except Exception as e:
            print(f"     ✗ Error downloading Germany wind data: {e}")
            print("     Please download manually from:")
            print("     https://www.renewables.ninja/country_downloads/DE/ninja-wind-country-DE-current_onshore-merra2.csv")
            all_ok = False

    # ------------------------------------------------------------------ #
    print("\n" + "=" * 60)
    if all_ok:
        print("✓ ALL DATA DOWNLOADED SUCCESSFULLY")
    else:
        print("✗ SOME DOWNLOADS FAILED — see messages above")
    print("=" * 60)
    return all_ok


if __name__ == "__main__":
    success = download_data()
    sys.exit(0 if success else 1)
