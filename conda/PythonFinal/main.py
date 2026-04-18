# This is the main program that calls all the functions to 
# produce the intended output

from nwsclient import NWSClient
from forecast import Forecast
from visual import NWSVisual

def main():
    client = NWSClient() # Creats the NWSClient object

    forecast = client.get_forecast() # obtains the forecast (as long as the NWS server works!)

    forecast_refined = Forecast(forecast) # Refines the data
    labels, temps = forecast_refined.get_labels_and_temps() # Generates labels for visual

    # This displays the text of the forecast
    for period in forecast_refined.periods:
        print(period)

    # Creates the visual object
    visualizer = NWSVisual() 
    # Creates the actual display from the object using the labels
    visualizer.plot_bar_chart(labels, temps)

if __name__ == "__main__":
    main()