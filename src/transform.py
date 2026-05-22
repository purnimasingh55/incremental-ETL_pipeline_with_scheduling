import pandas as pd

def transform_data(df):
    # Extract date feature
    df["order_month"] = df["order_date"].dt.month
    df["order_year"] = df["order_date"].dt.year

    # create discount flag
    df["discount_applied"] = df["discount_code"].apply(
        lambda x: 0 if x =="no_discount" else 1
    ) 

    # create high value order flag 
    df["high_value"] = df["total_amount"].apply(
        lambda x: 1 if x >= 500 else 0
    )

    # Payment mode grouping
    df["payment_category"] = df["payment_mode"].apply(
        lambda x: "Digital" if x in ["upi", "card", "netbanking"] else "Offline"
    )

    # clean unrealistic values
    df = df[df["total_amount"] > 0]

    # drop unnecessary column
    df = df.drop(columns = ["discount_code"], errors = "coerce")

    # reorder columns
    df = df[
        [
            "order_id",
            "product_id",
            "customer_id",
            "quantity",
            "total_amount",
            "order_date",
            "order_year",
            "order_month",
            "payment_mode",
            "payment_category",
            "discount_applied",
            "high_value"
        ]
    ]

    return df 