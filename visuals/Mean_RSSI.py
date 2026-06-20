import matplotlib.pyplot as plt
import pandas as pd

data_dir = "../data"
results_dir = f"{data_dir}/results"

all_location_df = pd.read_csv(f"{results_dir}/All_Location_Summary.csv")

location_group = all_location_df.groupby("location")["mean_rssi"].mean().reset_index()

plt.barh(location_group["location"], location_group["mean_rssi"], color="skyblue")

plt.title("MEAN_RSSI BY LOCATION")
plt.xlabel("Mean_RSSI (dBm)")
plt.ylabel("Location")
plt.tight_layout()

plt.show()