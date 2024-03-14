terraform {
  backend "gcs" {
    bucket  = "tf_backend"
    prefix  = "tfstate-storage"
  }
}