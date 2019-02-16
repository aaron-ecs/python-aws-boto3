resource "aws_s3_bucket" "b" {
  bucket = "aaron-williams-s3-bucket"
  acl    = "private"

  tags = {
    Name        = "learning-exercise"
    Environment = "Test"
  }
}