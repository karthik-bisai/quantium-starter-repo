import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")


csv_files = list(DATA_DIR.glob("*.csv"))
dfs = [pd.read_csv(f) for f in csv_files]

combined_df = pd.concat(dfs, ignore_index=True)

combined_df["product"] = (
    combined_df["product"]
    .str.strip()
    .str.lower()
)


pink_df = combined_df[combined_df["product"] == "pink morsel"].copy()

#float conversion
pink_df["price"] = (
    pink_df["price"]
    .str.replace("$", "", regex=False)
    .astype(float)
)


pink_df["quantity"] = pink_df["quantity"].astype(int)


pink_df["Sales"] = pink_df["price"] * pink_df["quantity"]

final_df = pink_df[["Sales", "date", "region"]].rename(
    columns={"date": "Date", "region": "Region"}
)

final_df.to_csv("pink_morsel_sales.csv", index=False)

print("CSV created")
print(final_df.head())
