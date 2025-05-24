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
def read_table(table_name: str, limit: int = 10) -> pd.DataFrame:
    conn = get_snowflake_connection()
    try:
        query = f"SELECT * FROM {table_name} LIMIT {limit}"
        df = pd.read_sql(query, conn)
        return df
    finally:
        conn.close()