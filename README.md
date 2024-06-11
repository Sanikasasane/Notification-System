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



  

