terraform {
  backend "gcs" {
    bucket  = "prueba_tf_backend"
    prefix  = "tfstate-datafusion_staging"
  }
}