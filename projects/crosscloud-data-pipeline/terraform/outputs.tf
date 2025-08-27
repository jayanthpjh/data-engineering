output "s3_bucket_name" {
  description = "Provisioned S3 bucket"
  value       = aws_s3_bucket.sales.bucket
}

output "bigquery_table" {
  description = "Full BigQuery table name"
  value       = "${google_bigquery_dataset.sales.dataset_id}.${google_bigquery_table.sales.table_id}"
}
