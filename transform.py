from  read_snowflake_tables import read_table
import pandas as pd
from datetime import datetime as dt


def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Summer"
    elif month in [6, 7, 8]:
        return "Monsoon"
    elif month in [9, 10, 11]:
        return "Autumn"
#Reading All the five tables
tourism_df = read_table("STATE_WISE_TOURISM")
# print(tourism_df.head())
govt_contri_df = read_table("GOVT_CONTRIBUTION_STATEWISE")
# print(govt_contri_df.head())
cult_event_df = read_table("CULTURAL_EVENT")
# print(cult_event_df.head())

tourism_df["DTVS_2019"] = tourism_df["DTVS_2019"].fillna(0)
tourism_df["DTVS_2020"] = tourism_df["DTVS_2019"].fillna(0)
tourism_df["DTVS_2021"] = tourism_df["DTVS_2019"].fillna(0)

tourism_df["FTVS_2019"] = tourism_df["FTVS_2019"].fillna(0)
tourism_df["FTVS_2020"] = tourism_df["FTVS_2019"].fillna(0)
tourism_df["FTVS_2021"] = tourism_df["FTVS_2019"].fillna(0)

tourism_df["TOTAL_VISITORS"] = tourism_df["DTVS_2019"] + tourism_df["FTVS_2019"] + tourism_df["DTVS_2020"] + tourism_df["DTVS_2021"] + \
tourism_df["FTVS_2020"] + tourism_df["FTVS_2021"]
tourism_df["STATE_UT"] = tourism_df["STATE_UT"].str.title()

govt_contri_df["C3"] = govt_contri_df["C3"].fillna(0)
govt_contri_df["C1"] = govt_contri_df["C1"].str.title()
merged_df = tourism_df.merge(govt_contri_df, left_on="STATE_UT", right_on="C1")
merged_df = merged_df.drop(columns=["C5", "C6","C1","C2"])
merged_df = merged_df.rename(columns={
    "STATE_UT": "STATE",
    "C3": "ALLOCATION_IN_CR",
    "C4": "INITIATIVE_TAKEN"
})
# Ensure it's string
cult_event_df["DATE"] = cult_event_df["DATE"].astype(str)
# Replace year '0024' with '2024'
cult_event_df["DATE"] = cult_event_df["DATE"].str.replace("^0024", "2024", regex=True)
# Now safely parse as datetime
cult_event_df["DATE"] = pd.to_datetime(cult_event_df["DATE"], errors="coerce")

cult_event_df["ART_FORM"] = cult_event_df["ART_FORM"].str.title()
cult_event_df["STATE"] = cult_event_df["STATE"].str.title()
cult_event_df["DATE"] = pd.to_datetime(cult_event_df["DATE"], errors="coerce")
cult_event_df["MONTH"] = cult_event_df["DATE"].dt.month
cult_event_df["SEASON"] = cult_event_df["MONTH"].apply(lambda x: get_season(x) if pd.notna(x) else None)
# event_counts = cult_event_df.groupby(["STATE", "SEASON"]).size().reset_index(name="EVENT_COUNT")
top_season_by_state = cult_event_df.sort_values("ATTENDANCE", ascending=False).drop_duplicates("STATE")
print(top_season_by_state.head())
merged_df_2 = merged_df.merge(top_season_by_state,on="STATE",how="inner")
print(merged_df_2.head())
merged_df_2 = merged_df_2[["STATE", "TOTAL_VISITORS", "SEASON", "EVENT_NAME","ART_FORM","ATTENDANCE"]]
print(merged_df_2.head())
