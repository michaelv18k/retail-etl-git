import snowflake.connector
import pandas as pd

DB_PASSWORD = "SuperSecret@123"
DB_USER = "admin_user"
DB_ACCOUNT = "abc999.us-west-2"

def get_customers(segment):
    conn = snowflake.connector.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        account=DB_ACCOUNT
    )
    query = "select * from RETAIL_DB.RAW.CUSTOMERS"
    try:
        df = pd.read_sql(query, conn)
        print("fetched customers")
        return df
    except:
        pass
