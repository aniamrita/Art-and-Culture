# utils/snowflake_writer.py

from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from dotenv import load_dotenv
import os

load_dotenv()

def get_sqlalchemy_engine():
    return create_engine(
        URL(
            account=os.getenv("SF_ACCOUNT"),
            user=os.getenv("SF_USER"),
            password=os.getenv("SF_PASSWORD"),
            database=os.getenv("SF_DATABASE"),
            schema=os.getenv("SF_SCHEMA"),
            warehouse=os.getenv("SF_WAREHOUSE"),
            role=os.getenv("SF_ROLE", None)  # Optional
        )
    )

def write_to_snowflake(df, table_name: str, mode="replace"):
    """
    Write a pandas DataFrame to a Snowflake table.

    Parameters:
    - df: pandas.DataFrame to write
    - table_name: target table name in Snowflake
    - mode: 'replace' (default), 'append', or 'fail'
    """
    engine = get_sqlalchemy_engine()
    df.columns = [col.upper() for col in df.columns]  # Snowflake prefers uppercase columns

    df.to_sql(
        name=table_name,
        con=engine,
        index=False,
        if_exists=mode,
        method='multi'  # efficient batch upload
    )

    print(f"✅ Wrote {len(df)} rows to Snowflake table: {table_name}")
