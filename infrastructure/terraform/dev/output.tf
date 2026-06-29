output "vpc_id" {
  description = "HealthSecure VPC ID"
  value       = aws_vpc.healthsecure_vpc.id
}

output "public_subnet_a_id" {
  description = "Public Subnet A ID"
  value       = aws_subnet.public_subnet_a.id
}

output "public_subnet_b_id" {
  description = "Public Subnet B ID"
  value       = aws_subnet.public_subnet_b.id
}

output "private_subnet_a_id" {
  description = "Private Subnet A ID"
  value       = aws_subnet.private_subnet_a.id
}

output "private_subnet_b_id" {
  description = "Private Subnet B ID"
  value       = aws_subnet.private_subnet_b.id
}
output "internet_gateway_id" {
  description = "Internet Gateway ID"
  value       = aws_internet_gateway.healthsecure_igw.id
}
