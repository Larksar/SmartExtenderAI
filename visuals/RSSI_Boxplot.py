import matplotlib.pyplot as plt
import pandas as pd

data_dir = "../data"
processed_dir = f"{data_dir}/processed"

kitchen_df = pd.read_csv(f"{processed_dir}/Kitchen_Combined.csv")
living_room_df = pd.read_csv(f"{processed_dir}/Living_Room_Combined.csv")
upstairs_hallway_df = pd.read_csv(f"{processed_dir}/Upstairs_Hallway_Combined.csv")

plt.boxplot(
    [
        kitchen_df["rssi"],
        living_room_df["rssi"],
        upstairs_hallway_df["rssi"]
    ],
    labels=[
        "Kitchen",
        "Living Room",
        "Upstairs Hallway"
    ]
)

plt.title("RSSI Distribution by Location")
plt.ylabel("RSSI (dBm)")
plt.xlabel("Location")

plt.show()