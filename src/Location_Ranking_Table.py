import pandas as pd

data_dir = "../data"
results = f"{data_dir}/results"

df = pd.read_csv(f"{results}/All_Location_Summary.csv")

group = df.groupby(["location"])

location_ranking_df = group.agg(
    mean_rssi = ("mean_rssi", "mean"),
    std_rssi = ("std_rssi", "mean")
).reset_index()

location_ranking_df = location_ranking_df.sort_values(
    by="mean_rssi",
    ascending=False
).reset_index(drop=True)

location_ranking_df["recommendation"] = [
    "Optimal",
    "Acceptable",
    "Acceptable",
    "Poor",
    "Poor",
    "Poor"
]

location_ranking_df.insert(
    0,
    "rank",
    range(1, len(location_ranking_df) + 1)
)

print(location_ranking_df)

location_ranking_df.to_csv(
    f"{results}/Location_Ranking.csv",
    index=False
)