import airflow
from datetime import datetime
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
DAG_ID = "raw_bronze"

BUCKET_NAME_SRC = "bucket_raw_parrvilla"
BUCKET_NAME_DST = "bucket_bronze_parrvilla"
OBJECT_SRC = "Clientes 1.csv"
COL_NAME = "FECHA_NACIMIENTO"
OBJECT_DST = "Clientes 1_Clean.csv"

def  delete_null(OBJECT_SRC, COL_NAME,OBJECT_DST):
    df = pd.read_csv(OBJECT_SRC)
    df = df.dropna (subset=[COL_NAME])
    df.to_csv(OBJECT_DST, index=False)

with airflow.DAG(
    DAG_ID,
    schedule="0 0 1 * *",
    start_date=datetime(2024, 3, 25),
) as dag:
     delete_null_task = PythonOperator(
          task_id="limpiar_archivo",
          python_callable=delete_null(OBJECT_SRC,COL_NAME,OBJECT_DST),
     )

     copy_single_file = GCSToGCSOperator(
        task_id="copy_single_gcs_file",
        source_bucket=BUCKET_NAME_SRC,
        source_object=[OBJECT_DST],
        destination_bucket=BUCKET_NAME_DST,  # If not supplied the source_bucket value will be used
        destination_object=OBJECT_DST,  # If not supplied the source_object value will be used
    )
     delete_null_task >> copy_single_file
