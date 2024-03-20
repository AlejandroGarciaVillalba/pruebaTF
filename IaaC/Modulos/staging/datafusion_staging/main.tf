provider "google" {
  project     = var.id_project_staging
  region      = var.region
}
 
resource "google_data_fusion_instance" "datafusion_staging" {
  name    = var.name_datafusion_staging  
  region  = var.region 
  type    = "BASIC"                  
}