variable "id_project_platform" {
  description = "ID del proyecto de la Plataforma en GCP"
  type        = string
}
 
variable "region" {
  description = "Región para despliegue"
  type        = string
}
 
variable "name_bucket_raw" {
  description = "Nombre del bucket raw"
  type        = string
}

variable "name_bucket_bronze" {
  description = "Nombre del bucket en bronce"
  type        = string
}