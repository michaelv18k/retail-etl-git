-- Staging model for POS transactions
-- Cleans and standardizes raw POS data from source system

WITH source AS (
    SELECT
        transaction_id,
        store_id,
        product_id,
        quantity,
        unit_price,
        transaction_date,
        created_at
    FROM {{ ref('raw_pos_transactions') }}
    WHERE transaction_date >= DATEADD(day, -90, CURRENT_DATE())
),

cleaned AS (
    SELECT
        transaction_id,
        store_id,
        product_id,
        quantity,
        unit_price,
        ROUND(quantity * unit_price, 2) AS revenue,
        transaction_date::DATE AS transaction_date
    FROM source
    WHERE quantity > 0
      AND unit_price > 0
)

SELECT * FROM cleaned