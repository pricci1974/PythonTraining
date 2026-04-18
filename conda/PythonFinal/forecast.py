class ForecastPeriod:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def __repr__(self):
        return f"{self.name}: {self.temperature}°F"
    
class Forecast:
    def __init__(self, raw_data):
        self.periods = self._parse(raw_data)

    def _parse(self, raw_data):

        day_periods = [p for p in raw_data if p["isDaytime"]][:7]

        return [
            ForecastPeriod(p["name"], p["temperature"])
            for p in day_periods
        ]
    
    def get_labels_and_temps(self):
        labels = [p.name for p in self.periods]
        temps = [p.temperature for p in self.periods]
        return labels, temps