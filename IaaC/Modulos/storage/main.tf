provider "google" {
  project     = var.id_project
  region      = var.region
}
 
resource "google_storage_bucket" "bucket1" {
  name          = var.name_bucket1  
  location      = var.region     
  force_destroy = true               
}