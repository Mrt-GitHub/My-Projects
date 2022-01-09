#! /bin/bash
yum update -y
yum install python3 -y
pip3 install flask
pip3 install flask_mysql
yum install git -y
cd /home/ec2-user && git clone https://github.com/Mrt-GitHub/My-Projects.git && rm -r My-Projects/!(devops)
python3 /home/ec2-user/My-Projects/devops/202-Terraform-Phonebook-Application-deployed-on-AWS/phonebook-app.py