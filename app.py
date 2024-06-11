from flask import Flask, request, jsonify

app = Flask(__name__)

class PubSubSystem:
    def __init__(self):
        self.topics = {}

    def subscribe(self, topicId, subscriberId):
        if topicId not in self.topics:
            self.topics[topicId] = set()
        self.topics[topicId].add(subscriberId)
        return f"Subscriber {subscriberId} subscribed to topic {topicId}"

    def notify(self, topicId):
        if topicId in self.topics and self.topics[topicId]:
            return f"Notifying subscribers of topic {topicId}: {', '.join(self.topics[topicId])}"
        else:
            return f"No subscribers to notify for topic {topicId}"

    def unsubscribe(self, topicId, subscriberId):
        if topicId in self.topics and subscriberId in self.topics[topicId]:
            self.topics[topicId].remove(subscriberId)
            return f"Subscriber {subscriberId} unsubscribed from topic {topicId}"
        else:
            return f"Subscriber {subscriberId} is not subscribed to topic {topicId}"

# Initialize the system
pubsub_system = PubSubSystem()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    topicId = data.get('topicId')
    subscriberId = data.get('subscriberId')
    if topicId and subscriberId:
        message = pubsub_system.subscribe(topicId, subscriberId)
        return jsonify({"message": message})
    return jsonify({"error": "Invalid input"}), 400

@app.route('/notify/<topicId>', methods=['GET'])
def notify(topicId):
    message = pubsub_system.notify(topicId)
    return jsonify({"message": message})

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.json
    topicId = data.get('topicId')
    subscriberId = data.get('subscriberId')
    if topicId and subscriberId:
        message = pubsub_system.unsubscribe(topicId, subscriberId)
        return jsonify({"message": message})
    return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
