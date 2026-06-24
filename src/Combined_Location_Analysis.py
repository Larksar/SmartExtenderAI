import pandas as pd

results_dir = "../data/results"

kitchen_df = pd.read_csv(f"{results_dir}/Kitchen_Summary.csv")
living_room_df = pd.read_csv(f"{results_dir}/Living_Room_Summary.csv")
upstairs_hallway_df = pd.read_csv(f"{results_dir}/Upstairs_Hallway_Summary.csv")
bedroom_df = pd.read_csv(f"{results_dir}/Bedroom_Summary.csv")
master_df = pd.read_csv(f"{results_dir}/Master_Bedroom_Summary.csv")
spare_room_df = pd.read_csv(f"{results_dir}/Spare_Room_Summary.csv")

all_locations_df = pd.concat(
    [kitchen_df, living_room_df, upstairs_hallway_df, bedroom_df, master_df, spare_room_df], 
    ignore_index=True
)

print(all_locations_df)

all_locations_df.to_csv(f"{results_dir}/All_Location_Summary.csv",
                        index=False)