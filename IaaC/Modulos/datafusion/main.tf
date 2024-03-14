provider "google" {
  project     = var.id_project
  region      = var.region
}
 
resource "google_data_fusion_instance" "datafusion1" {
  name          = var.name_datafusion1  
  location      = var.region 
  type = ""                  
}