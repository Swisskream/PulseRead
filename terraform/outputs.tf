output "lambda_function_arn" {
  value = aws_lambda_function.pulse_lambda.arn
}

output "s3_input_bucket" {
  value = aws_s3_bucket.input_bucket.bucket
}

output "s3_summary_bucket" {
  value = aws_s3_bucket.summary_bucket.bucket
}