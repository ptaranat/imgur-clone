provider "aws" {
  region = "us-east-2"
}

resource "aws_s3_bucket" "image_repo_bucket" {
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
