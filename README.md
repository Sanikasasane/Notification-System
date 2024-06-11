# Notification-System
A simple Publisher-Subscriber notification system implemented in Python using Flask. This system allows subscribers to subscribe to topics and receive notifications when publishers publish messages to those topics. It's designed to be lightweight, scalable, and easy to use.

## Endpoints

### 1. Subscribe
- **Method**: POST
- **URL**: `/subscribe`
- **Description**: Subscribes a subscriber to a topic.
- **Request Body**:
  ```json
  {
    "topicId": "string",
    "subscriberId": "string"
  }
- **Example Body**:
  ```json
  {
  "message": "Subscriber subscribed to topic successfully"
  }
### 2. Notify
- **Method**: GET
- **URL**: `/notify/{topicId}`
- **Description**: Sends notifications to all subscribers of the specified topic.
- **URL Parameters**: `topicId` (string): The ID of the topic to notify subscribers about.
- **Example Response**:
  ```json
  {
  "message": "Notifications sent successfully"
  }
### 3.Unsubscribe
- **Method**: POST
- **URL**: `/unsubscribe`
-**Description**: Unsubscribes a subscriber from a topic.
-**Request Body**:
  ```json
  {
  "topicId": "string",
  "subscriberId": "string"
  }
- **Example Response**:
  ```json
  {
  "message": "Subscriber unsubscribed from topic successfully"
  }
  
- **Hosting on AWS**
- Select EC2 from the Services Menu
- Select Launch Instance and Create an EC2 Instance. 
Choose appropriate OS. I have used AWS Linux
Create a Key Pair. (This .pem/ppk file will be the specific key whose presence will enable you to login from anywhere)
We have successfully created & launched the instance.
After initializing the EC2 Instance, we will have to connect it to the VM.
For this we have three methods:
 1. We will use the PuTTY to convert .pem file(The key which we downloaded while creating the instance) to .ppk and launch it on our local  System/machine
 2. If we have downloaded the .ppk file then we can directly initialize the VM on our local Machine/System.
 3. We will directly connect to the VM through the AWS platform
 I have used the 3rd method.
 After connecting with the Instance, we will run the following commands on the console:
 1. sudo su -
 2. yum update -y
 3. yum install -y httpd
 4. systemctl status httpd
 5. mkdir aws_company
 6. cd aws_company
 7. For this assignment we have created a API SERVER which we have uploaded on Github.com.
 8. Copy the Download Link for the .zip file of the portfolio
 9. using the wget command, download the zip file to the folder.
 10. unzip the main.zip file and navigate in to the Notification-System-main folder using the cd command.
 11. move all the contents from the folder to “/var/www/html/”

- Edit the Inbound Rules
- Check the status of httpd and then enable & start httpd using the following commands
  systemctl status httpd
  systemctl enable httpd
  systemctl start httpd
- Now open the public ipv4 address allocated to the EC2 instance we created in new tab. We will be able to see the Website.

- We have Successfully Deployed the API Server on AWS Cloud!

  

