import logging
import pandas as pd

logger = logging.getLogger(__name__)

def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform raw POS transactions.
    
    Args:
        df: Raw POS transactions DataFrame
    Returns:
        Cleaned and transformed DataFrame
    """
    df = df.dropna(subset=["transaction_id", "store_id", "product_id"])
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    df = df[df["quantity"] > 0]
    logger.info(f"Transformed {len(df)} valid sales records")
    return df