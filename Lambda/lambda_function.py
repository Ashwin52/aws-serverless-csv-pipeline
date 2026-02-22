import os
import json
import boto3
import csv
from datetime import datetime

# AWS clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# Config
TABLE_NAME = "file_upload_logs"
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")  # Environment variable

table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    try:
        # Get S3 event details
        record = event['Records'][0]
        bucket_name = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']

        print(f"File uploaded: {file_key}")
        print(f"Bucket name: {bucket_name}")

        # Process only CSV files
        if not file_key.endswith(".csv"):
            print("Not a CSV file. Skipping processing.")
            return {"statusCode": 200, "body": "Not a CSV file"}

        # Read CSV from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8').splitlines()

        reader = csv.reader(content)
        rows = list(reader)

        # Exclude header
        row_count = max(len(rows) - 1, 0)

        print(f"Total rows in CSV: {row_count}")

        # Store metadata in DynamoDB
        table.put_item(
            Item={
                "file_name": file_key,
                "bucket_name": bucket_name,
                "row_count": row_count,
                "uploaded_at": datetime.utcnow().isoformat()
            }
        )

        print("Entry written to DynamoDB successfully")

        # Send SNS notification
        if SNS_TOPIC_ARN:
            message = (
                f"CSV Upload Alert\n\n"
                f"File Name: {file_key}\n"
                f"Bucket: {bucket_name}\n"
                f"Row Count: {row_count}\n"
                f"Uploaded At: {datetime.utcnow().isoformat()}"
            )

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="CSV Upload Alert",
                Message=message
            )

            print("SNS email alert sent successfully")
        else:
            print("SNS_TOPIC_ARN not configured")

        return {
            "statusCode": 200,
            "body": json.dumps("File processed successfully")
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise e
