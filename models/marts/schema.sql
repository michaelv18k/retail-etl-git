version: 2

models:
  - name: fct_sales
    description: "Daily sales aggregated by store and product. Source of truth for revenue reporting."
    columns:
      - name: store_id
        description: "Unique store identifier"
        tests:
          - not_null
      - name: product_id
        description: "Unique product identifier"
        tests:
          - not_null
      - name: transaction_date
        description: "Date of the transactions"
        tests:
          - not_null
      - name: total_revenue
        description: "Total revenue for the store-product-date combination"
        tests:
          - not_null