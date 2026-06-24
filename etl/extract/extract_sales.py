# etl/extract/extract_sales.py  ← INTENTIONALLY BROKEN VERSION
import snowflake.connector
import pandas as pd

# SECURITY ISSUE: hardcoded credentials
SNOWFLAKE_PASSWORD = "secret"
SNOWFLAKE_USER = "etl_admin"
SNOWFLAKE_ACCOUNT = "xy12345.us-east-1" 

def extract_pos_transactions(start_date, end_date):   # missing type hints
    # CORRECTNESS: no docstring
conn = snowflake.connector.connect(
    user=os.environ.get("SNOWFLAKE_USER"),
    password=os.environ.get("SNOWFLAKE_PASSWORD"),
    account=os.environ.get("SNOWFLAKE_ACCOUNT")
)
    # PERFORMANCE: SELECT * with no WHERE clause = full table scan
    query = """
    SELECT
        transaction_id,
        store_id,
        product_id,
        quantity,
        unit_price,
        transaction_date
    FROM RETAIL_DB.RAW.POS_TRANSACTIONS
    WHERE transaction_date BETWEEN %(start)s AND %(end)s
"""
    
    try:
        df = pd.read_sql(query, conn)
        print(f"got data")   # CORRECTNESS: print instead of logging
        return df
    except:                  # SECURITY: bare except hides all errors
        pass                 # CORRECTNESS: silently swallows failures
