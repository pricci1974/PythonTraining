# This produces a bar graph to display the temperature
# It is saved in a jpg format
import matplotlib.pyplot as plt


class NWSVisual:
    def plot_bar_chart(self, labels, temps):
        plt.figure()

        plt.bar(labels, temps)

        plt.title("Rochester, NY 7 Day Temperature Forecast")
        plt.xlabel("Day")
        plt.ylabel("Temperature °F")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.savefig("forecast.jpg")