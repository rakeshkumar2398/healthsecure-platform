resource "aws_vpc" "healthsecure_vpc" {

  cidr_block = "10.0.0.0/16"

  enable_dns_support = true

  enable_dns_hostnames = true

  tags = merge(
    local.common_tags,
    {
      Name = "healthsecure-vpc"
    }
  )
}
resource "aws_subnet" "public_subnet_a" {

  vpc_id = aws_vpc.healthsecure_vpc.id

  cidr_block = "10.0.1.0/24"

  availability_zone = data.aws_availability_zones.available.names[0]

  map_public_ip_on_launch = true

  tags = merge(
    local.common_tags,
    {
      Name = "public-subnet-a"
    }
  )
}
resource "aws_subnet" "public_subnet_b" {

  vpc_id = aws_vpc.healthsecure_vpc.id

  cidr_block = "10.0.2.0/24"

  availability_zone = data.aws_availability_zones.available.names[1]

  map_public_ip_on_launch = true

  tags = merge(
    local.common_tags,
    {
      Name = "public-subnet-b"
    }
  )
}
resource "aws_subnet" "private_subnet_a" {

  vpc_id = aws_vpc.healthsecure_vpc.id

  cidr_block = "10.0.3.0/24"

  availability_zone = data.aws_availability_zones.available.names[0]

  tags = merge(
    local.common_tags,
    {
      Name = "private-subnet-a"
    }
  )
}
resource "aws_subnet" "private_subnet_b" {

  vpc_id = aws_vpc.healthsecure_vpc.id

  cidr_block = "10.0.4.0/24"

  availability_zone = data.aws_availability_zones.available.names[1]

  tags = merge(
    local.common_tags,
    {
      Name = "private-subnet-b"
    }
  )
}
resource "aws_internet_gateway" "healthsecure_igw" {
  vpc_id = aws_vpc.healthsecure_vpc.id

  tags = merge(
    local.common_tags,
    {
      Name = "healthsecure-igw"
    }
  )
}
resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.healthsecure_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.healthsecure_igw.id
  }

  tags = merge(
    local.common_tags,
    {
      Name = "healthsecure-public-rt"
    }
  )
}
resource "aws_route_table_association" "public_subnet_a_association" {
  subnet_id      = aws_subnet.public_subnet_a.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_route_table_association" "public_subnet_b_association" {
  subnet_id      = aws_subnet.public_subnet_b.id
  route_table_id = aws_route_table.public_route_table.id
}
resource "aws_security_group" "healthsecure_ec2_sg" {
  name        = "healthsecure-ec2-sg"
  description = "Allow SSH, Jenkins, SonarQube, and app traffic"
  vpc_id      = aws_vpc.healthsecure_vpc.id

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Jenkins"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SonarQube"
    from_port   = 9000
    to_port     = 9000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Backend App"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    local.common_tags,
    {
      Name = "healthsecure-ec2-sg"
    }
  )
}
