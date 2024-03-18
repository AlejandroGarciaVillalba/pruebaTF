terraform {
  backend "gcs" {
    bucket  = "tf_backend_parrvill"
    prefix  = "tfstate-platform_storage"
  }
}