variable "cluster_name"      { default = "fintech-eks-prod" }
variable "region"            { default = "eu-central-1"   }
variable "vpc_cidr"          { default = "10.0.0.0/16"    }
variable "instance_types"    { default = ["t3.medium"]      }
variable "desired_size"      { default = 3                   }
