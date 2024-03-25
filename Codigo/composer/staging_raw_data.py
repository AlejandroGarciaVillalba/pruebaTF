import airflow
from datetime import datetime
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
DAG_ID = "staging_raw"

BUCKET_NAME_SRC = "bucket_stag_parrvilla"
BUCKET_NAME_DST = "bucket_raw_parrvilla"
OBJECT_SRC = "Clientes 1.csv"

with airflow.DAG(
    DAG_ID,
    schedule="0 0 1 * *",
    start_date=datetime(2024, 3, 19),
) as dag:
     copy_single_file = GCSToGCSOperator(
        task_id="copy_single_gcs_file",
        source_bucket=BUCKET_NAME_SRC,
        source_object=[OBJECT_SRC],
        destination_bucket=BUCKET_NAME_DST,  # If not supplied the source_bucket value will be used
        destination_object=OBJECT_SRC,  # If not supplied the source_object value will be used
    )
     copy_single_file