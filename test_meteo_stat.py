#!/usr/bin/env python3
"""
Testskript für die Meteostat API.
Dieses Skript demonstriert die Verwendung der MeteoStatAPI-Klasse.
"""

import json
from weather_data.meteo_stat_api import MeteoStatAPI

def main():
    # Initialisiere die API
    api = MeteoStatAPI()
    
    # Beispiel 1: Monatliche Daten für Berlin (2020)
    print("Fetching monthly data for Berlin (2020)...")
    berlin_monthly = api.fetch_monthly_data(
        lat=52.5244, 
        lon=13.4105, 
        alt=43, 
        start_date="2020-01-01", 
        end_date="2020-12-31"
    )
    
    if "error" not in berlin_monthly:
        print("Successfully fetched monthly data for Berlin!")
        if 'data' in berlin_monthly and 'data' in berlin_monthly['data'] and berlin_monthly['data']['data']:
            print(f"Data points: {len(berlin_monthly['data']['data'])}")
        else:
            print("No data points found.")
    else:
        print(f"Error: {berlin_monthly['error']}")
    
    # Beispiel 2: Tägliche Daten für Paris (letzte Woche)
    print("\nFetching daily data for Paris (last week)...")
    paris_daily = api.fetch_daily_data(
        lat=48.8566, 
        lon=2.3522, 
        alt=35, 
        start_date="2023-01-01", 
        end_date="2023-01-07"
    )
    
    if "error" not in paris_daily:
        print("Successfully fetched daily data for Paris!")
        if 'data' in paris_daily and 'data' in paris_daily['data'] and paris_daily['data']['data']:
            print(f"Data points: {len(paris_daily['data']['data'])}")
        else:
            print("No data points found.")
    else:
        print(f"Error: {paris_daily['error']}")
    
    # Beispiel 3: Wetterstationen in der Nähe von München
    print("\nFetching weather stations near Munich...")
    munich_lat = 48.1351
    munich_lon = 11.5820
    munich_stations = api.fetch_nearby_stations(
        lat=munich_lat,
        lon=munich_lon,
        radius=50,
        limit=10
    )
    
    if "error" not in munich_stations:
        print("Successfully fetched nearby stations data!")
        print("Response structure:")
        print(json.dumps(munich_stations, indent=2))
        
        # Versuche, die Stationen zu extrahieren, falls vorhanden
        if 'data' in munich_stations and isinstance(munich_stations['data'], dict) and 'data' in munich_stations['data']:
            stations = munich_stations['data']['data']
            if stations:
                print(f"Number of stations: {len(stations)}")
                
                # Zeige die ersten 3 Stationen an
                for i, station in enumerate(stations[:3]):
                    print(f"Station {i+1}: {station.get('name', 'Unknown')} (ID: {station.get('id', 'Unknown')})")
            else:
                print("No stations found in the specified radius.")
        else:
            print("Stations data not found in the expected format.")
            print("Available keys in response:", munich_stations.keys())
            if 'data' in munich_stations:
                print("Available keys in data:", munich_stations['data'].keys() if isinstance(munich_stations['data'], dict) else "Not a dictionary")
    else:
        print(f"Error: {munich_stations['error']}")
    
    print("\nTest completed successfully!")

if __name__ == "__main__":
    main() 