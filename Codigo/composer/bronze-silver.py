import os
from datetime import datetime
import airflow
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator
 
DAG_ID = "bronze-silver"
BUCKET_NAME_SRC = "bucket_bronze_parrvilla"
OBJECT_SRC = "Clientes 1.csv"
DATASET_NAME = "silver"
TABLE_NAME = "silver_hot"
 
def check_dataset_function():
    if True:
        return "load_csv"
    else:
        return "notify_error"
 
default_args={
    'retries': 0,
    'owner': "Parrondo"
}
 
with airflow.DAG(
    dag_id=DAG_ID,
    schedule="0 0 1 * *",
    default_args=default_args,
    start_date=datetime(2024, 3, 20),
) as dag:
   
    start_task = DummyOperator(task_id="start_task")
 
    check_dataset = BranchPythonOperator(
        task_id="check_dataset",
        python_callable=check_dataset_function
    )
   
    end_task = DummyOperator(task_id="end_task")
   
    notify_error = DummyOperator(task_id="notify_error")
 
    load_csv = GCSToBigQueryOperator(
        task_id="load_csv",
        bucket= BUCKET_NAME_SRC,
        source_objects=[OBJECT_SRC],
        destination_project_dataset_table=f"{DATASET_NAME}.{TABLE_NAME}",
        schema_fields=[
            {"name": "ID","type": "STRING", "mode": "NULLABLE"},
            {"name": "DNI","type": "STRING", "mode": "NULLABLE"},
            {"name": "NOMBRE","type": "STRING", "mode": "NULLABLE"},
            {"name": "APELLIDOS","type": "STRING", "mode": "NULLABLE"},
            {"name": "GENERO","type": "STRING", "mode": "NULLABLE"},
            {"name": "DIRECCION","type": "STRING", "mode": "NULLABLE"},
            {"name": "MUNICIPIO","type": "STRING", "mode": "NULLABLE"},
            {"name": "CIUDAD","type": "STRING", "mode": "NULLABLE"},
            {"name": "CODIGO_POSTAL","type": "STRING", "mode": "NULLABLE"},
            {"name": "TELEFONO","type": "STRING", "mode": "NULLABLE"},
            {"name": "X","type": "STRING", "mode": "NULLABLE"},
            {"name": "FECHA_NACIMIENTO","type": "STRING", "mode": "NULLABLE"},
            {"name": "FECHA_FALLECIMIENTO","type": "STRING", "mode": "NULLABLE"},
            {"name": "CORREO","type": "STRING", "mode": "NULLABLE"}
        ],
        write_disposition="WRITE_TRUNCATE",
    )
 
    start_task >> check_dataset >> [load_csv, notify_error]
    load_csv >> end_task