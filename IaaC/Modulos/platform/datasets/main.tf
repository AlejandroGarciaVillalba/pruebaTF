provider "google" {
  project     = var.id_project_platform
  region      = var.region
}
 
resource "google_bigquery_dataset" "dataset_silver" {
  dataset_id                  = "silver"
  friendly_name               = "silver"
  description                 = "Dataset silver format"
  location                    = var.region
  default_table_expiration_ms = 3600000
}

resource "google_bigquery_dataset" "dataset_golden" {
  dataset_id                  = "golden"
  friendly_name               = "golden"
  description                 = "Dataset golden format"
  location                    = var.region
  default_table_expiration_ms = 3600000
}