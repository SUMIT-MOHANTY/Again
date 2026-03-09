output "kubeconfig_context" {
  value = "aws eks update-kubeconfig --region ${var.region} --name ${var.cluster_name}"
}
