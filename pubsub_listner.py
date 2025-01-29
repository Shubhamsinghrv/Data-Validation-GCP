import json
import os
from google.cloud import pubsub_v1
from data_quality_tester import DataQualityTester
from collections import defaultdict

# Set GCP Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/shubhamsingh/desktop/big-data-engin-e0ea9f6af799.json"

# Pub/Sub subscription details
PROJECT_ID = "big-data-engin"
SUBSCRIPTION_NAME = "trigger-jupyter-sub"

# Track uploaded files by org folder
uploaded_files = defaultdict(list)

def process_files(org_folder, files):
    """Trigger the data quality test when both source and target files are available."""
    if len(files) == 2:
        print(f"Processing files for org_folder: {org_folder}")

        # Assign the first file as source and the second as target
        source_file = files[0]
        target_file = files[1]

        print(f"Source file: {source_file}, Target file: {target_file}")

        tester = DataQualityTester(
            source_bucket="samplebucketvrs",
            source_path=source_file,
            target_bucket="samplebucketvrs",
            target_path=target_file,
            delimiter="|"
        )

        results = tester.run_quality_test()
        print(f"Data Quality Test Completed: {results}")
        
        # Clear the files for this folder after processing
        uploaded_files[org_folder] = []

def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()  # Acknowledge the message

    # Load Pub/Sub message as JSON
    event_data = json.loads(message.data.decode("utf-8"))
    file_name = event_data.get("name", "")

    if file_name:  # If a file was uploaded
        print(f"New file uploaded: {file_name}")
        
        # Extract organization folder from file path
        # Expected path format: "Data_Validation/org1/filename"
        parts = file_name.split('/')
        if len(parts) >= 3:
            org_folder = parts[1]  # Second part is the org folder (e.g., 'org1')
        else:
            print("Invalid file path format. Skipping...")
            return

        # Add file to the list of uploaded files for this folder
        uploaded_files[org_folder].append(file_name)

        # Process files if two are present in the org_folder
        process_files(org_folder, uploaded_files[org_folder])

# Start Pub/Sub listener
def listen_for_messages():
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_NAME)
    
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}...")

    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()
        subscriber.close()

if __name__ == "__main__":
    listen_for_messages()
