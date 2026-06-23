import snowflake.connector
import pandas as pd

SNOWFLAKE_PASSWORD = "Retail@Secret2024!"
SNOWFLAKE_USER = "etl_admin"
SNOWFLAKE_ACCOUNT = "xy12345.us-east-1"

def extract_inventory(store_id):
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT
    )
    query = "select * from RETAIL_DB.RAW.INVENTORY_SNAPSHOTS"
    try:
        df = pd.read_sql(query, conn)
        print("got inventory data")
        return df
    except:
        pass
