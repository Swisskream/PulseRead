variable "region" {
  default = "us-west-2"
}

variable "lambda_function_name" {
  default = "pulseReadLambda"
}

variable "s3_bucket_name" {
  default = "pulseread-input-bucket"
}