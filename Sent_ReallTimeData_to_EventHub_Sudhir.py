from azure.eventhub import EventHubProducerClient, EventData
import json
 
# Event Hub connection string and event hub name
connection_str = ""
event_hub_name = "su"
 
# Create an EventHubProducerClient
producer = EventHubProducerClient.from_connection_string(conn_str=connection_str, eventhub_name=event_hub_name)
 
# Load the JSON data from the file
with open("C:\\Users\\Sudhir.Yadav\\Downloads\\sentdatatoeventhub\\real_time_transactions.json", "r") as f:
    transactions = json.load(f)
 
# Convert the transactions to EventData and send to Event Hub
event_data_batch = producer.create_batch()
 
for transaction in transactions:
    event_data_batch.add(EventData(json.dumps(transaction)))
    print("datasent")
 
# Send the batch to the Event Hub
producer.send_batch(event_data_batch)
 
producer.close()