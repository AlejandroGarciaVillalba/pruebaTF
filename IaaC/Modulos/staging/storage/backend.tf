terraform {
  backend "gcs" {
    bucket  = "tf_backend_parrvill"
    prefix  = "tfstate-storage_bucket_staging"
  }
}