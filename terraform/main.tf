provider "aws" {
  region = "us-east-2"
}

resource "aws_s3_bucket" "bucket" {
  bucket = "dev-image-repo-bucket"

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["PUT", "POST"]
    allowed_origins = ["*"]
    expose_headers  = ["x-amz-server-side-encryption", "x-amz-request-id", "x-amz-id-2"]
    max_age_seconds = 3000
  }

  tags = {
    Name        = "Dev Image Repo Bucket"
    Environment = "Dev"
  }
}

resource "aws_cognito_user_pool" "image_repo_pool" {
  name = "imagerepopool"

  auto_verified_attributes = ["email"]

  verification_message_template {
    default_email_option = "CONFIRM_WITH_CODE"
  }
}

resource "aws_cognito_user_pool_client" "client" {
  name = "image-repo-app-client"

  user_pool_id = aws_cognito_user_pool.image_repo_pool.id
}

output "UserPoolId" {
  value = aws_cognito_user_pool.image_repo_pool.id
}

output "UserPoolArn" {
  value = aws_cognito_user_pool.image_repo_pool.arn
}

output "ClientId" {
  value = aws_cognito_user_pool_client.client.id
}
