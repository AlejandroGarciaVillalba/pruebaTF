terraform {
  backend "gcs" {
    bucket  = "prueba_tf_backend"
    prefix  = "tfstate-storage_bucket_staging"
  }
}