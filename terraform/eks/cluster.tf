resource "aws_iam_role" "eks_cluster" {
  name = "${var.cluster_name}-cluster-role"
  assume_role_policy = data.aws_iam_policy_document.eks_assume.json
  tags = { Name = var.cluster_name, "fintech-platform" = "true" }
}
data "aws_iam_policy_document" "eks_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals { type = "Service", identifiers = ["eks.amazonaws.com"] }
  }
}
resource "aws_eks_cluster" "fintech" {
  name     = var.cluster_name
  role_arn = aws_iam_role.eks_cluster.arn
  vpc_config {
    subnet_ids = data.aws_subnets.private.ids
  }
  tags = { Name = var.cluster_name, "fintech-platform" = "true" }
}
resource "aws_iam_role" "eks_node" {
  name = "${var.cluster_name}-node-role"
  assume_role_policy = data.aws_iam_policy_document.ec2_assume.json
  tags = { Name = var.cluster_name, "fintech-platform" = "true" }
}
data "aws_iam_policy_document" "ec2_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals { type = "Service", identifiers = ["ec2.amazonaws.com"] }
  }
}
resource "aws_eks_node_group" "main" {
  cluster_name    = aws_eks_cluster.fintech.name
  node_group_name = "main"
  node_role_arn   = aws_iam_role.eks_node.arn
  subnet_ids      = data.aws_subnets.private.ids
  scaling_config {
    desired_size = var.desired_size
    min_size     = 1
    max_size     = 5
  }
  instance_types = var.instance_types
  tags = { Name = var.cluster_name, "fintech-platform" = "true" }
}
