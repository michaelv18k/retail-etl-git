import os
import logging
import snowflake.connector
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_pos_transactions(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Extract POS transactions from Snowflake for a given date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
    Returns:
        DataFrame with POS transaction records
    """
    conn = snowflake.connector.connect(
        user=os.environ.get("SNOWFLAKE_USER"),
        password=os.environ.get("SNOWFLAKE_PASSWORD"),
        account=os.environ.get("SNOWFLAKE_ACCOUNT")
    )
query = """
SELECT transaction_id, store_id, product_id, quantity, unit_price, transaction_date
FROM RETAIL_DB.RAW.POS_TRANSACTIONS
WHERE transaction_date BETWEEN %(start)s AND %(end)s
"""
    try:
        df = pd.read_sql(query, conn, params={"start": start_date, "end": end_date})
        logger.info(f"Extracted {len(df)} rows from POS_TRANSACTIONS")
        return df
    except snowflake.connector.Error as e:
        logger.error(f"Snowflake extraction failed: {e}")
        raise
    finally:
        conn.close()
