variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "gcp_project" {
  description = "GCP project ID"
  type        = string
}

variable "gcp_region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}

variable "s3_bucket" {
  description = "Name of S3 bucket for sales data"
  type        = string
}

variable "bq_dataset" {
  description = "BigQuery dataset ID"
  type        = string
}

variable "bq_table" {
  description = "BigQuery table ID"
  type        = string
}
