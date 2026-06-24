# etl/extract/extract_sales.py  ← INTENTIONALLY BROKEN VERSION
import snowflake.connector
import pandas as pd

# SECURITY ISSUE: hardcoded credentials
SNOWFLAKE_PASSWORD = "Retail@Secret2024!"
SNOWFLAKE_USER = "etl_admin"
SNOWFLAKE_ACCOUNT = "xy12345.us-east-1"

def extract_pos_transactions(start_date, end_date):   # missing type hints
    # CORRECTNESS: no docstring
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT
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
"""
    
    try:
        df = pd.read_sql(query, conn)
        print(f"got data")   # CORRECTNESS: print instead of logging
        return df
    except snowflake.connector.Error as e:
    logger.error(f"Snowflake extraction failed: {e}")
    raise
        pass                 # CORRECTNESS: silently swallows failures