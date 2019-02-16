# python-aws-boto3
Introduction to using simple terraform scripts and Boto3 API.

## Setup
Please set your AWS access and secret keys by running `aws configure`

Run `pip install boto3`

## Terraform / Boto3
Navigate into a directory of the resource wish to use and run `terraform apply` & then run the test file.

Please ensure you always run `terraform destroy` to bring down anything running.

For example to do this for S3:
- `cd s3/`
- `terraform plan`
- `terraform apply`
- `python -m unittest discover -s s3 -p '*_test.py'`
- `terraform destroy`

## Jargon

**Simple Storage Service (S3)** - online storage through a web service interface

**EC2 (Elastic Compute Cloud)** - virtual computers

**ECS (Elastic Container Service)** - cluster of EC2 instances