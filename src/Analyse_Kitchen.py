import pandas as pd

data_dir = "../data"
processed_dir = f"{data_dir}/processed"
results_dir = f"{data_dir}/results"

df = pd.read_csv(f"{processed_dir}/Kitchen_Combined.csv", index_col=0)

group1 = df.groupby(["location", "run_id"])

summary_df = group1.agg(
    mean_rssi = ("rssi", "mean"),
    min_rssi = ("rssi", "min"),
    max_rssi = ("rssi", "max"),
    std_rssi = ("rssi", "std"),
    sample_count = ("rssi", "count"),
    detection_rate = ("found", "mean")
).reset_index()

print(summary_df)
