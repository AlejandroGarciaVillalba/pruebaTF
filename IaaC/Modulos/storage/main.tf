provider "google" {
  project     = var.id_project_platform
  region      = var.region
}
 
resource "google_storage_bucket" "bucket_raw" {
  name          = var.name_bucket_raw 
  location      = var.region     
  force_destroy = true               
}