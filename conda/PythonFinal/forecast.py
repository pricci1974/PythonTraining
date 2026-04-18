# This file contains the forecast objects needed to produce the temperature results
class ForecastPeriod:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    # This formats the output for the user
    def __repr__(self):
        return f"{self.name}: {self.temperature}°F"
    
class Forecast:
    def __init__(self, raw_data):
        self.periods = self._parse(raw_data) # This creates the periods of data 

    def _parse(self, raw_data): # The data contains bools for daytime/nighttime checks
                                # This assignment ensures only the daily results are included
        day_periods = [p for p in raw_data if p["isDaytime"]][:7]

        # This returns the function for each of the periods
        return [
            ForecastPeriod(p["name"], p["temperature"])
            for p in day_periods
        ]
    
    # This is used to create the visualization with appropriate labels
    def get_labels_and_temps(self):
        labels = [p.name for p in self.periods]
        temps = [p.temperature for p in self.periods]
        return labels, temps