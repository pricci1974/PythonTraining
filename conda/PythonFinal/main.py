from nwsclient import NWSClient
from forecast import Forecast
from visual import NWSVisual

def main():
    client = NWSClient()

    forecast = client.get_forecast()

    forecast_refined = Forecast(forecast)
    labels, temps = forecast_refined.get_labels_and_temps()

    for period in forecast_refined.periods:
        print(period)

    visualizer = NWSVisual()
    visualizer.plot_bar_chart(labels, temps)

if __name__ == "__main__":
    main()