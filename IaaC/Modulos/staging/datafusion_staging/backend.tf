terraform {
  backend "gcs" {
    bucket  = "tf_backend_parrvill"
    prefix  = "tfstate-datafusion_staging"
  }
}