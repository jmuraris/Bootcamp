# Terraform EC2 demo

This folder contains a minimal Terraform configuration that creates an EC2 instance in the default VPC, a security group allowing SSH (22) and HTTP (80), and uploads a public SSH key as an AWS key pair.

Prerequisites
- Terraform 1.0+ installed
- AWS credentials configured (environment variables or AWS CLI profile)
- A local SSH key pair (public key) to upload

Quick start (PowerShell)

1. Generate an SSH key pair if you don't have one:

```powershell
ssh-keygen -t rsa -b 4096 -f $env:USERPROFILE\.ssh\terraform_demo -N ""
```

2. Initialize Terraform:

```powershell
cd "c:\Users\Admin\Downloads\Bootcamp\terraform-ec2"
terraform init
```

3. Plan and apply (replace the public_key_path with your .pub path):

```powershell
terraform plan -var "public_key_path=$env:USERPROFILE\.ssh\terraform_demo.pub"
terraform apply -var "public_key_path=$env:USERPROFILE\.ssh\terraform_demo.pub" -auto-approve
```

4. After apply, outputs will show the public IP and DNS. SSH with the corresponding private key file:

```powershell
ssh -i $env:USERPROFILE\.ssh\terraform_demo ec2-user@<public_ip>
```

Notes
- The configuration uses the default VPC in the selected region.
- You must provide a valid public key path so Terraform can create the key pair.
- AWS credentials: set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as environment variables or use `AWS_PROFILE`.

Next steps (optional):
- Use an SSM-enabled AMI and an IAM role to avoid SSH keys.
- Add user-data for automated provision (install web server).
