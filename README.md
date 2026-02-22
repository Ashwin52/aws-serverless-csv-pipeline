# AWS Serverless CSV Processing Pipeline 🚀

An event-driven serverless data pipeline built using AWS services.

When a CSV file is uploaded to Amazon S3:
- S3 triggers AWS Lambda
- Lambda parses the CSV and counts rows
- Metadata is stored in DynamoDB
- SNS sends real-time email alerts
- CloudWatch logs are generated for monitoring

---

## 🏗 Architecture

S3 → Lambda → DynamoDB → SNS → Email

---

## 🔹 Features

- Automatic trigger on CSV upload
- Real-time row count calculation
- Metadata storage in DynamoDB
- Email notification via SNS
- Fully serverless architecture
- Low-cost, free-tier friendly setup

---

## 🛠 Tech Stack

- AWS S3
- AWS Lambda (Python 3.10)
- Amazon DynamoDB
- Amazon SNS
- Amazon CloudWatch
- Python (boto3)

---

## 📂 Project Structure
aws-serverless-csv-pipeline/
│
├── lambda/
│ └── lambda_function.py
│
├── architecture/
│ └── architecture-diagram.png
│
└── README.md


---

## ⚙ How It Works

1. User uploads a CSV file to S3.
2. S3 event triggers Lambda.
3. Lambda:
   - Reads the file
   - Counts rows
   - Stores file metadata in DynamoDB
   - Publishes SNS notification
4. Email alert is sent to subscribed users.

---

## 💡 Use Case

Automated monitoring and processing of uploaded CSV files in real time.  
Can be extended for data validation, ETL pipelines, analytics workflows, and monitoring systems.

---

## 📈 Future Improvements

- Row-threshold alerting (e.g., alert if rows > 100)
- Daily summary reports
- Error alerting system
- S3 lifecycle automation

---

Built as part of hands-on Cloud Engineering practice.
