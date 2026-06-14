import pandas as pd

data_dir = "../data"
processed_dir = f"{data_dir}/processed"
results_dir = f"{data_dir}/results"

df = pd.read_csv(f"{processed_dir}/Kitchen_Combined.csv", index_col=0)

group1 = df.groupby(["location", "run_id"])

summary_df = group1["rssi"].mean()

print(summary_df)