-- Fact table: daily sales by store and product
-- Used by: Sales dashboard, Finance reporting

WITH transactions AS (
    SELECT * FROM {{ ref('stg_pos_transactions') }}
),

final AS (
    SELECT
        store_id,
        product_id,
        transaction_date,
        SUM(quantity)              AS total_quantity,
        SUM(revenue)               AS total_revenue,
        COUNT(transaction_id)      AS transaction_count
    FROM transactions
    GROUP BY
        store_id,
        product_id,
        transaction_date
)

SELECT * FROM final
