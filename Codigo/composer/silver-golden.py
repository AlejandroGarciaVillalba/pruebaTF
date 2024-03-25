import os
from datetime import datetime
import airflow
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator
 
DAG_ID = "silver-golden"
DATASET_NAME_SRC = "silver"
TABLE_NAME = "silver_hot"
DATASET_NAME_DST = "silver"