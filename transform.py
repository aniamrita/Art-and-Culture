from  read_snowflake_tables import read_table

#Reading All the five tables
tourism_df = read_table("STATE_WISE_TOURISM")
print(tourism_df.head())
govt_contri_df = read_table("GOVT_CONTRIBUTION_STATEWISE")
print(govt_contri_df.head())
cult_event_df = read_table("CULTURAL_EVENT")
print(cult_event_df.head())