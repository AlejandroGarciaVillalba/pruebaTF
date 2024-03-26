from google.cloud import storage
import airflow
from datetime import datetime
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from airflow.operators.dummy_operator import DummyOperator
from io import BytesIO
from io import StringIO
import io

DAG_ID = "raw-bronze"

BUCKET_NAME_SRC = "bucket_raw_parrvilla"
BUCKET_NAME_DST = "bucket_bronze_parrvilla"
OBJECT_SRC = "Clientes 1.csv"
COL_NAME = "FECHA_NACIMIENTO"
OBJECT_DST = "Clientes 1_Clean.csv"

def  delete_null():
    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME_SRC)

    # blob = bucket.blob(OBJECT_SRC)
    
    # contenido_bytes = blob.download_as_bytes()

    #df = pd.read_csv(BytesIO(contenido_bytes))

    urls_list = bucket.blob(OBJECT_SRC).download_as_text()
    csv_io = io.StringIO(urls_list)
    df = pd.read_csv(csv_io)

    print(df.head(5))
    df = df.dropna (subset=[COL_NAME])
    return df

def insert_bronze_function(df):

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    # Convertir el contenido CSV en bytes
    contenido_bytes = csv_buffer.getvalue().encode()

    # Inicializar cliente de Google Cloud Storage
    client = storage.Client()

    # Obtener el bucket
    bucket = client.bucket(BUCKET_NAME_DST)

    # Crear un nuevo blob (archivo) en el bucket
    blob = bucket.blob(OBJECT_DST)

    # Subir el contenido CSV al blob
    blob.upload_from_string(contenido_bytes)

with airflow.DAG(
    DAG_ID,
    schedule="0 0 1 * *",
    start_date=datetime(2024, 3, 25),
) as dag:
    delete_null_task = PythonOperator(
        task_id="delete_null_task",
        python_callable=delete_null(),
    )

    insert_bronze = PythonOperator(
        task_id="insert_bronze",
        python_callable=insert_bronze_function(),
        op_kwargs = {'df': delete_null_task.output}
    )
    

    start = DummyOperator(task_id='start')

        
    end = DummyOperator(task_id='end')

    # Definir la secuencia de tareas
    start >> delete_null_task >> insert_bronze >> end
    





