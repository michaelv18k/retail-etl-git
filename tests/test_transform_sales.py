import pandas as pd
import pytest
from etl.transform.transform_sales import transform_sales

def test_removes_null_transactions():
    df = pd.DataFrame({
        "transaction_id": [1, None, 3],
        "store_id": [1, 2, 3],
        "product_id": [1, 2, 3],
        "quantity": [2, 1, 3],
        "unit_price": [10.0, 5.0, 8.0]
    })
    result = transform_sales(df)
    assert len(result) == 2

def test_calculates_revenue():
    df = pd.DataFrame({
        "transaction_id": [1],
        "store_id": [1],
        "product_id": [1],
        "quantity": [5],
        "unit_price": [20.0]
    })
    result = transform_sales(df)
    assert result["revenue"].iloc[0] == 100.0