import time
import json
import random
from datetime import datetime
from kafka import KafkaProducer

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Initialize the Kafka Producer pointing to our local Docker cluster
# Initialize the Kafka Producer pointing to our local Docker cluster
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=json_serializer,
    api_version=(7, 5, 0)  # <-- ADD THIS LINE
)

TOPIC_NAME = 'transactions'
payment_methods = ['Credit Card', 'PayPal', 'Apple Pay', 'Crypto']

print("🚀 Real-time Producer started emitting events... Press Ctrl+C to stop.")

try:
    while True:
        # Generate a mock financial transaction event
        data = {
            'transaction_id': random.randint(100000, 999999),
            'timestamp': datetime.utcnow().isoformat(),
            'user_id': random.randint(1, 500),
            'amount': round(random.uniform(5.0, 500.0), 2),
            'payment_method': random.choice(payment_methods),
            'status': random.choices(['SUCCESS', 'FAILED'], weights=[0.92, 0.08])[0]
        }
        
        # Ship it off to Kafka
        producer.send(TOPIC_NAME, data)
        print(f"Sent Event: {data['transaction_id']} | ${data['amount']} via {data['payment_method']}")
        
        # Emit a new event every 0.5 to 1.5 seconds
        time.sleep(random.uniform(0.5, 1.5))
        
except KeyboardInterrupt:
    print("\n🛑 Producer stopped.")
finally:
    producer.close()