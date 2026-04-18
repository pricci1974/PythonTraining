import matplotlib.pyplot as plt


class NWSVisual:
    def plot_bar_chart(self, labels, temps):
        plt.figure()

        plt.bar(labels, temps)

        plt.title("7 Day Forecast (Temperature °F)")
        plt.xlabel("Day")
        plt.ylabel("Temperature °F")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.savefig("forecast.jpg")