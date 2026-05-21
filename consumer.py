import json
import os
from kafka import KafkaConsumer

CONSUMED_DATA_FILE = "live_metrics.json"

# Initialize local array to hold incoming state
processed_events = []

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    api_version=(7, 5, 0)  # <-- ADD THIS LINE
)

print("🎧 Consumer listening for streaming events from Kafka...")

try:
    for message in consumer:
        event = message.value
        
        # Transformation & Filtering Stage
        # In modern streaming architectures, we validate and augment events on the fly.
        if event['status'] == 'SUCCESS':
            clean_event = {
                'id': event['transaction_id'],
                'time': event['timestamp'],
                'user': f"User_{event['user_id']}",
                'amount_usd': event['amount'],
                'type': event['payment_method']
            }
            processed_events.append(clean_event)
            
            # Keep only the latest 100 entries to prevent memory bloating
            if len(processed_events) > 100:
                processed_events.pop(0)
                
            # Write atomic state change out to disk for the UI frontend
            with open(CONSUMED_DATA_FILE, "w") as f:
                json.dump(processed_events, f)
                
            print(f"Processed & Stored Clean Event: {clean_event['id']}")
except KeyboardInterrupt:
    print("\n🛑 Consumer shut down safely.")