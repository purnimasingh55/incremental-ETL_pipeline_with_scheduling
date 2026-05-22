import pandas as pd
import logging
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os

from clean import get_clean_csv_data
from transform import transform_data

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)

# SQLite database path
DB_URL = "sqlite:///orders.db"

def get_existing_order_ids(engine):
    try:
        query = "SELECT order_id FROM orders"
        existing_df = pd.read_sql(query, engine)
        return set(existing_df["order_id"])

    except Exception:
        logging.warning("Table may not exist yet. Treating as first run")
        return set()


def load_incremental_to_db(df, engine):
    try:
        df.to_sql(
            "orders",
            engine,
            if_exists="append",
            index=False
        )

        logging.info(f"Loaded {df.shape[0]} new records into database")

    except SQLAlchemyError as e:
        logging.error(f"Database load failed: {e}")
        raise


def run_pipeline(file_path):
    try:
        logging.info("ETL Pipeline started")

        # Extract + Clean
        df_clean = get_clean_csv_data(file_path)
        logging.info(f"Clean data rows: {df_clean.shape[0]}")

        # Transform
        df_transformed = transform_data(df_clean)
        logging.info(f"Transformed data rows: {df_transformed.shape[0]}")

        # DB connection
        engine = create_engine(DB_URL)

        # Existing IDs
        existing_ids = get_existing_order_ids(engine)
        logging.info(f"Existing records in DB: {len(existing_ids)}")

        # Incremental filtering
        new_df = df_transformed[
            ~df_transformed["order_id"].isin(existing_ids)
        ]

        logging.info(f"New records detected: {new_df.shape[0]}")
        logging.info(
            f"Skipped existing records: "
            f"{df_transformed.shape[0] - new_df.shape[0]}"
        )

        # Load new records
        if not new_df.empty:
            load_incremental_to_db(new_df, engine)
        else:
            logging.info("No new records to load")

        logging.info("ETL Pipeline completed successfully\n")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")


def schedule_pipeline(file_path, interval_seconds=60):
    while True:
        run_pipeline(file_path)

        logging.info(
            f"Sleeping for {interval_seconds} seconds...\n"
        )

        time.sleep(interval_seconds)


if __name__ == "__main__":
    FILE_PATH = "data/orders.csv"

    run_pipeline(FILE_PATH)

    # Uncomment for scheduling
    schedule_pipeline(FILE_PATH, interval_seconds=60)