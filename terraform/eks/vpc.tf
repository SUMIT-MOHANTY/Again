data "aws_vpc" "main" {
  filter { name = "cidr-block"; values = ["10.0.0.0/16"] }
}
data "aws_subnets" "private" {
  filter { name = "vpc-id"; values = [data.aws_vpc.main.id] }
}
