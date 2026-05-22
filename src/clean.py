import pandas as pd

def get_clean_csv_data(file_path):
    # Read the csv file
    df = pd.read_csv(file_path)

    # Remove Duplicates
    df = df.drop_duplicates()

    # standrdize column names
    df.columns = [col.strip().lower() for col in df.columns]

    # convert data types [product_id, quantity, total_amount, order_date]
    df["product_id"] = pd.to_numeric(df["product_id"], errors = "coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors = "coerce")
    df["total_amount"] = pd.to_numeric(df["total_amount"], errors = "coerce")
    df["order_date"] = pd.to_datetime(df["order_date"], errors = "coerce")

    # Handle missing values [order_id, product_id, order_date -> drop]
    df = df.dropna(subset=["order_id", "product_id","order_date" ])

    # fill quantity if missing
    df["quantity"] = df["quantity"].fillna(1)

    # fill payment_mode if missing
    df["payment_mode"] = df["quantity"].fillna("unknown_mode")

    # remove -ve or zero quantity
    df = df[df["quantity"]>0]

    # remove invalid product_id
    df = df[df["product_id"].between(1,20)]

    # remove future_date
    df = df[df["order_date"] <= pd.Timestamp.now()]


    # clean discount column
    df["discount"] = df["discount_code"].fillna("no_discount")

    # validation column -> useful for incremental loading
    df["isValid"] = True

    return df 
