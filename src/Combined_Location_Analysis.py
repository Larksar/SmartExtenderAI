import pandas as pd

results_dir = "../data/results"

kitchen_df = pd.read_csv(f"{results_dir}/Kitchen_Summary.csv")
living_room_df = pd.read_csv(f"{results_dir}/Living_Room_Summary.csv")
upstairs_hallway_df = pd.read_csv(f"{results_dir}/Upstairs_Hallway_Summary.csv")

all_locations_df = pd.concat(
    [kitchen_df, living_room_df, upstairs_hallway_df], 
    ignore_index=True
)

print(all_locations_df)

all_locations_df.to_csv(f"{results_dir}/All_Location_Summary.csv",
                        index=False)