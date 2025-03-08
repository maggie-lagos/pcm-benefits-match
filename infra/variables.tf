# variables.tf

variable "aws_region" {
  description = "The AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "pcm-match"
}

variable "environment" {
  description = "Environment (dev, staging, production)"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for the private subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for the public subnets"
  type        = list(string)
  default     = ["10.0.101.0/24", "10.0.102.0/24"]
}

variable "db_instance_class" {
  description = "RDS instance class"
  type        = string
  default     = "db.t3.micro"
}

variable "db_allocated_storage" {
  description = "Allocated storage for the RDS instance in GB"
  type        = number
  default     = 20
}

variable "database_name" {
  description = "Name of the database"
  type        = string
}

variable "database_username" {
  description = "Database master username"
  type        = string
  sensitive   = true
}

variable "database_password" {
  description = "Database master password"
  type        = string
  sensitive   = true
}

variable "django_secret_key" {
  description = "Django secret key"
  type        = string
  sensitive   = true
}

variable "debug" {
  description = "Django debug mode"
  type        = string
  default     = "False"
}

variable "django_loglevel" {
  description = "Django log level"
  type        = string
  default     = "INFO"
}

variable "fargate_cpu" {
  description = "Fargate CPU units"
  type        = string
  default     = "256"
}

variable "fargate_memory" {
  description = "Fargate memory in MiB"
  type        = string
  default     = "512"
}

variable "app_count" {
  description = "Number of Docker containers to run"
  type        = number
  default     = 2
}

variable "app_min_count" {
  description = "Minimum number of Docker containers"
  type        = number
  default     = 2
}

variable "app_max_count" {
  description = "Maximum number of Docker containers"
  type        = number
  default     = 10
}

variable "use_fargate_spot" {
  description = "Use Fargate Spot capacity provider"
  type        = bool
  default     = false
}

variable "tags" {
  description = "A map of tags to add to all resources"
  type        = map(string)
  default = {
    Terraform   = "true"
    Environment = "dev"
  }
}