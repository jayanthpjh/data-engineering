terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

provider "google" {
  project = var.gcp_project
  region  = var.gcp_region
}

resource "aws_s3_bucket" "sales" {
  bucket        = var.s3_bucket
  force_destroy = true
}

resource "google_bigquery_dataset" "sales" {
  dataset_id = var.bq_dataset
  location   = var.gcp_region
}

resource "google_bigquery_table" "sales" {
  dataset_id          = google_bigquery_dataset.sales.dataset_id
  table_id            = var.bq_table
  deletion_protection = false

  schema = jsonencode([
    {
      name = "order_id"
      type = "STRING"
      mode = "REQUIRED"
    },
    {
      name = "order_date"
      type = "DATE"
      mode = "REQUIRED"
    },
    {
      name = "customer_id"
      type = "STRING"
      mode = "REQUIRED"
    },
    {
      name = "product"
      type = "STRING"
      mode = "REQUIRED"
    },
    {
      name = "amount"
      type = "FLOAT"
      mode = "REQUIRED"
    }
  ])
}
