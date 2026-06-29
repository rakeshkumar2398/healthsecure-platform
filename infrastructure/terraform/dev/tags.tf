locals {

  common_tags = {

    Project = local.project

    Environment = local.environment

    Owner = local.owner

    ManagedBy = "Terraform"
  }

}
