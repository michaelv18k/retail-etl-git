import os
import logging
import snowflake.connector
import pandas as pd

logger = logging.getLogger(__name__)

def load_to_snowflake(df: pd.DataFrame, target_table: str) -> None:
    """
    Load transformed DataFrame into Snowflake target table.
    
    Args:
        df: Transformed DataFrame to load
        target_table: Target Snowflake table name
    """
    conn = snowflake.connector.connect(
        user=os.environ.get("SNOWFLAKE_USER"),
        password=os.environ.get("SNOWFLAKE_PASSWORD"),
        account=os.environ.get("SNOWFLAKE_ACCOUNT")
    )
    try:
        from snowflake.connector.pandas_tools import write_pandas
        success, chunks, rows, _ = write_pandas(conn, df, target_table)
        logger.info(f"Loaded {rows} rows into {target_table}")
    except snowflake.connector.Error as e:
        logger.error(f"Load failed: {e}")
        raise
    finally:
        conn.close()