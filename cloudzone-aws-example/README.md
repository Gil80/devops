# cloudzone-aws-example

1. Login to the AWS Account:

2. Account ID: 547824763104 IAM User Name: candidate Password: m2BBj68[

3. Access the EC2 Console:
   Within the EC2 Console, you will find 3 instances named Web-1, Web-2, and World-Access.
   Web-1 and Web-2 are currently running Nginx websites on port 80.

4. Establish a Connection to Web Instances via Session Manager:
   Use Session Manager to securely connect to the Web Instances.

5. Access World-Access Instance via RDP:
   Use an RDP client to access the World-Access Instance with the following credentials:
   Username: Administrator
   Password: CloudZ0Ne!!!

6. Access Web Sites on Web Instances via Private Network:
   Open a web browser on the World-Access Instance and navigate to the following URLs:
   Web-1: http://`Web-1-Instance-IP`/index.html
   
   Web-2: http://`Web-2-Instance-IP`/index.html
   Both of the instances should publish same website

7. Configure ALB (Application Load Balancer):
   Configure the ALB to publish the websites hosted on the Web Instances on port 80.

8. Restrict Access to ALB from World-Access Instance Only:
   Ensure that the ALB's DNS can only be accessed from the World-Access Instance.

9. Block External Access to Instances:
    Implement security measures to block all external access to the instances. Only the ALB should be allowed to forward traffic to these instances.


---

Notes:
1. web-1 is in a private subnet
2. web-2 is in a public subnet

   
## 4. How to establish a connection to Web Instances via Session Manager?

1. To connect to an instance using Session Manager, Systems Manager requires an IAM instance profile. You can create an instance profile and assign it to your instance by using a Systems Manager Quick Setup host management configuration.
2. Following this doco to configure required security roles and on my EC2 instance WEB-1
3. However, I noticed that the EC2 web-2 is using the same IAM role as web-1, and since I can use SSM with web-2 I realized it's not a permission issue. After further investigation, I found that I need to setup VPC endpoints because web-1 is in a private subnet.
4. Creating 3 VPC endpoint for web-1: ssm, ec2messages and ssmmessages. Each endpoint is using the same subnet and vpc of the private EC2 instance.
5. Restarted the machine
6. Session manager is now avaliable.

## 5. Access World-Access Instance via RDP
1. Open the EC2 instance connection tab
2. Select RDP
3. Download the file and run it to connect.
4. I validated that the SG for that instance is allowing connection on port 3389 for RDP

## 6. Access Web Sites on Web Instances via Private Network
1. the ec2 web-1 doesn't have nginx installed and doesn't have internet connectivity
2. the routing of the web-1 server is via igw. I rerouted it to NAT to be the same as web-2 server.
3. I followed this guide to install nginx on web-1: https://devcoops.com/install-nginx-on-aws-ec2-amazon-linux/
4. I then ran `sudo systemctl enable nginx` followed by `sudo systemctl start nginx`
5. I compared web-1 with web-2, and found that /usr/share/nginx/index.html is edited to show Cloudzone logo, so I copied index.html content to web-1 and now both sites are matching.

## 7. Configure ALB (Application Load Balancer):
1. Add two public subnets in the same AZ of each of the EC2 web instances.
2. Created a new load balancer with default settings and using the same AZ as the web EC2 instances and their public subnets
3. Associated the target group with the newly created load balancer.
4. In the Windows instance brower, I entered http://web-lb-v1-211572693.us-east-1.elb.amazonaws.com/index.html and got the page loading.
5. The site is also avaiable outside of the VPC

## 8. Restrict Access to ALB from World-Access Instance Only
1. Had to change the load balancer to internal instead of internet facing
2. Changed the LB security group Inbound rule to allow only from `world-access` instance
3. Using the Windows instance, I was able to access the web app via `internal-web-alb-v2-1651936645.us-east-1.elb.amazonaws.com/index.html`

## 9. Block External Access to Instances:
1. Removed the inbound rule from the sg of web-1 and web-2 to allow access from `world-access`.
2. Added an inbound rule to allow access only from the ALB sg.



   
