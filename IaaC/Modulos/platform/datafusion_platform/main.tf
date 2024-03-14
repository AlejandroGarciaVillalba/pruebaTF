provider "google" {
  project     = var.id_project_platform
  region      = var.region
}
 
resource "google_data_fusion_instance" "datafusion_platform" {
  name    = var.name_datafusion_platform  
  region  = var.region 
  type    = "BASIC"                  
}