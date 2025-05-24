import os
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Function to create a Snowflake connection
def get_snowflake_connection():
    return snowflake.connector.connect(
        user=os.getenv("SF_USER"),
        password=os.getenv("SF_PASSWORD"),
        account=os.getenv("SF_ACCOUNT"),
        warehouse=os.getenv("SF_WAREHOUSE"),
        database=os.getenv("SF_DATABASE"),
        schema=os.getenv("SF_SCHEMA")
    )


#read any table
def read_table(table_name: str, transform: bool = True) -> pd.DataFrame:
    conn = get_snowflake_connection()
    try:
        database = "ART_AND_TORUSM"     # e.g., ART_AND_TORUSM
        schema = os.getenv("SF_SCHEMA")         # e.g., PUBLIC

        # Fully qualified table name WITH double quotes
        full_table_name = f'"{database}"."{schema}"."{table_name}"'
        query = f"SELECT * FROM {full_table_name}"

        print(f"Executing query: {query}")  # Optional debug
        df = pd.read_sql(query, conn)
        return df
    finally:
        conn.close()
