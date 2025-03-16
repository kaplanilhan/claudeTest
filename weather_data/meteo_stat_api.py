import http.client
import json
import os
from typing import Dict, Any, Optional, List
from config.config import config

class MeteoStatAPI:
    def __init__(self):
        """
        Initialisiert die MeteoStatAPI-Klasse mit den Konfigurationsparametern aus der .env-Datei.
        """
        self.api_key = config.METEO_STAT_API_KEY
        self.api_host = config.METEO_STAT_API_HOST
        self.base_url = "meteostat.p.rapidapi.com"
        
    def fetch_monthly_data(self, lat: float, lon: float, alt: int, start_date: str, end_date: str) -> Dict[str, Any]:
        """
        Ruft monatliche Wetterdaten für einen bestimmten Standort und Zeitraum ab.
        
        Args:
            lat: Breitengrad des Standorts
            lon: Längengrad des Standorts
            alt: Höhe des Standorts in Metern
            start_date: Startdatum im Format YYYY-MM-DD
            end_date: Enddatum im Format YYYY-MM-DD
            
        Returns:
            Ein Dictionary mit den Wetterdaten oder einer Fehlermeldung
        """
        try:
            conn = http.client.HTTPSConnection(self.base_url)
            
            headers = {
                'x-rapidapi-key': self.api_key,
                'x-rapidapi-host': self.api_host
            }
            
            endpoint = f"/point/monthly?lat={lat}&lon={lon}&alt={alt}&start={start_date}&end={end_date}"
            conn.request("GET", endpoint, headers=headers)
            
            response = conn.getresponse()
            data = response.read().decode("utf-8")
            
            # Schließe die Verbindung
            conn.close()
            
            # Parse JSON-Antwort
            json_data = json.loads(data)
            
            # Formatiere die Daten für Kafka
            formatted_data = {
                "source": "meteostat",
                "type": "monthly",
                "location": {
                    "latitude": lat,
                    "longitude": lon,
                    "altitude": alt
                },
                "time_range": {
                    "start": start_date,
                    "end": end_date
                },
                "data": json_data
            }
            
            return formatted_data
            
        except Exception as e:
            return {"error": str(e)}
    
    def fetch_daily_data(self, lat: float, lon: float, alt: int, start_date: str, end_date: str) -> Dict[str, Any]:
        """
        Ruft tägliche Wetterdaten für einen bestimmten Standort und Zeitraum ab.
        
        Args:
            lat: Breitengrad des Standorts
            lon: Längengrad des Standorts
            alt: Höhe des Standorts in Metern
            start_date: Startdatum im Format YYYY-MM-DD
            end_date: Enddatum im Format YYYY-MM-DD
            
        Returns:
            Ein Dictionary mit den Wetterdaten oder einer Fehlermeldung
        """
        try:
            conn = http.client.HTTPSConnection(self.base_url)
            
            headers = {
                'x-rapidapi-key': self.api_key,
                'x-rapidapi-host': self.api_host
            }
            
            endpoint = f"/point/daily?lat={lat}&lon={lon}&alt={alt}&start={start_date}&end={end_date}"
            conn.request("GET", endpoint, headers=headers)
            
            response = conn.getresponse()
            data = response.read().decode("utf-8")
            
            # Schließe die Verbindung
            conn.close()
            
            # Parse JSON-Antwort
            json_data = json.loads(data)
            
            # Formatiere die Daten für Kafka
            formatted_data = {
                "source": "meteostat",
                "type": "daily",
                "location": {
                    "latitude": lat,
                    "longitude": lon,
                    "altitude": alt
                },
                "time_range": {
                    "start": start_date,
                    "end": end_date
                },
                "data": json_data
            }
            
            return formatted_data
            
        except Exception as e:
            return {"error": str(e)}
    
    def fetch_hourly_data(self, lat: float, lon: float, alt: int, start_date: str, end_date: str) -> Dict[str, Any]:
        """
        Ruft stündliche Wetterdaten für einen bestimmten Standort und Zeitraum ab.
        
        Args:
            lat: Breitengrad des Standorts
            lon: Längengrad des Standorts
            alt: Höhe des Standorts in Metern
            start_date: Startdatum im Format YYYY-MM-DD HH:MM:SS
            end_date: Enddatum im Format YYYY-MM-DD HH:MM:SS
            
        Returns:
            Ein Dictionary mit den Wetterdaten oder einer Fehlermeldung
        """
        try:
            conn = http.client.HTTPSConnection(self.base_url)
            
            headers = {
                'x-rapidapi-key': self.api_key,
                'x-rapidapi-host': self.api_host
            }
            
            endpoint = f"/point/hourly?lat={lat}&lon={lon}&alt={alt}&start={start_date}&end={end_date}"
            conn.request("GET", endpoint, headers=headers)
            
            response = conn.getresponse()
            data = response.read().decode("utf-8")
            
            # Schließe die Verbindung
            conn.close()
            
            # Parse JSON-Antwort
            json_data = json.loads(data)
            
            # Formatiere die Daten für Kafka
            formatted_data = {
                "source": "meteostat",
                "type": "hourly",
                "location": {
                    "latitude": lat,
                    "longitude": lon,
                    "altitude": alt
                },
                "time_range": {
                    "start": start_date,
                    "end": end_date
                },
                "data": json_data
            }
            
            return formatted_data
            
        except Exception as e:
            return {"error": str(e)}
    
    def fetch_nearby_stations(self, lat: float, lon: float, radius: int = 50, limit: int = 10) -> Dict[str, Any]:
        """
        Ruft Wetterstationen in der Nähe eines bestimmten Standorts ab.
        
        Args:
            lat: Breitengrad des Standorts
            lon: Längengrad des Standorts
            radius: Radius in Kilometern (Standard: 50)
            limit: Maximale Anzahl der zurückzugebenden Stationen (Standard: 10)
            
        Returns:
            Ein Dictionary mit den Stationsdaten oder einer Fehlermeldung
        """
        try:
            conn = http.client.HTTPSConnection(self.base_url)
            
            headers = {
                'x-rapidapi-key': self.api_key,
                'x-rapidapi-host': self.api_host
            }
            
            endpoint = f"/stations/nearby?lat={lat}&lon={lon}&radius={radius}&limit={limit}"
            conn.request("GET", endpoint, headers=headers)
            
            response = conn.getresponse()
            data = response.read().decode("utf-8")
            
            # Schließe die Verbindung
            conn.close()
            
            # Parse JSON-Antwort
            json_data = json.loads(data)
            
            # Formatiere die Daten für Kafka
            formatted_data = {
                "source": "meteostat",
                "type": "nearby_stations",
                "location": {
                    "latitude": lat,
                    "longitude": lon
                },
                "radius": radius,
                "data": json_data
            }
            
            return formatted_data
            
        except Exception as e:
            return {"error": str(e)}
    
    def fetch_station_data(self, station_id: str) -> Dict[str, Any]:
        """
        Ruft Informationen über eine bestimmte Wetterstation ab.
        
        Args:
            station_id: ID der Wetterstation
            
        Returns:
            Ein Dictionary mit den Stationsdaten oder einer Fehlermeldung
        """
        try:
            conn = http.client.HTTPSConnection(self.base_url)
            
            headers = {
                'x-rapidapi-key': self.api_key,
                'x-rapidapi-host': self.api_host
            }
            
            endpoint = f"/stations/meta?id={station_id}"
            conn.request("GET", endpoint, headers=headers)
            
            response = conn.getresponse()
            data = response.read().decode("utf-8")
            
            # Schließe die Verbindung
            conn.close()
            
            # Parse JSON-Antwort
            json_data = json.loads(data)
            
            # Formatiere die Daten für Kafka
            formatted_data = {
                "source": "meteostat",
                "type": "station",
                "station_id": station_id,
                "data": json_data
            }
            
            return formatted_data
            
        except Exception as e:
            return {"error": str(e)}
    
    def search_stations(self, query: str, limit: int = 10) -> Dict[str, Any]:
        """
        Sucht nach Wetterstationen basierend auf einem Suchbegriff.
        
        Args:
            query: Suchbegriff (z.B. Stadtname)
            limit: Maximale Anzahl der zurückzugebenden Ergebnisse
            
        Returns:
            Ein Dictionary mit den gefundenen Stationen oder einer Fehlermeldung
        """
        try:
            conn = http.client.HTTPSConnection(self.base_url)
            
            headers = {
                'x-rapidapi-key': self.api_key,
                'x-rapidapi-host': self.api_host
            }
            
            endpoint = f"/stations/search?query={query}&limit={limit}"
            conn.request("GET", endpoint, headers=headers)
            
            response = conn.getresponse()
            data = response.read().decode("utf-8")
            
            # Schließe die Verbindung
            conn.close()
            
            # Parse JSON-Antwort
            json_data = json.loads(data)
            
            # Formatiere die Daten für Kafka
            formatted_data = {
                "source": "meteostat",
                "type": "station_search",
                "query": query,
                "data": json_data
            }
            
            return formatted_data
            
        except Exception as e:
            return {"error": str(e)}

# Beispiel für die Verwendung der Klasse
if __name__ == "__main__":
    api = MeteoStatAPI()
    
    # Beispiel: Monatliche Daten für Berlin (2020)
    berlin_data = api.fetch_monthly_data(
        lat=52.5244, 
        lon=13.4105, 
        alt=43, 
        start_date="2020-01-01", 
        end_date="2020-12-31"
    )
    
    print(json.dumps(berlin_data, indent=2))
