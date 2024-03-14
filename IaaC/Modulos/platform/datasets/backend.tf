terraform {
  backend "gcs" {
    bucket  = "prueba_tf_backend"
    prefix  = "tfstate-platform_dataset"
  }
}