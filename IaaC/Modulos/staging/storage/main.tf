provider "google" {
  project     = var.id_project_staging
  region      = var.region
}
 
resource "google_storage_bucket" "bucket_staging" {
  name          = var.name_bucket_staging 
  location      = var.region     
  force_destroy = true               
}