variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "key_name" {
  description = "Name for the AWS key pair to create"
  type        = string
  default     = "terraform-demo-key"
}

variable "public_key_path" {
  description = "Path to public SSH key (e.g., C:\\Users\\Me\\.ssh\\id_rsa.pub). Terraform will upload this to AWS as a key pair."
  type        = string
  default     = ""
}
