from nwsclient import NWSClient
from forecast import Forecast
from visual import NWSVisual
from config import Config

def main():
    client = NWSClient()

    forecast_url = client.get_forecast_url()

    raw_forecast = client.get_forecast(forecast_url)

    forecast = Forecast(raw_forecast)
    labels, temps = forecast.get_labels_and_temps()

    for period in forecast.periods:
        print(period)

    visualizer = NWSVisual()
    visualizer.plot_bar_chart(labels, temps)

if __name__ == "__main__":
    main()