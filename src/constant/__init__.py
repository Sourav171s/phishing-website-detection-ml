from datetime import datetime
import os

AWS_S3_BUCKET_NAME = "phishing-classifier"
MONGO_DATABASE_NAME = "phising_db"

TARGET_COLUMN = "Result"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder_name = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
artifact_folder = os.path.join("artifacts", artifact_folder_name)


''' What is an AWS S3 Bucket?
Amazon S3 (Simple Storage Service) is a cloud storage service provided by AWS.
 An S3 Bucket is like a folder on the cloud where you can store files (data, models, logs, etc.).

 Why Do We Use AWS_S3_BUCKET_NAME in ML Projects?
We define the variable AWS_S3_BUCKET_NAME to store the name of the S3 bucket we want to use. This is important for:
Task
Purpose
 Uploading
Store trained models, datasets, logs, etc. on cloud
 Downloading
Load data or models from cloud when needed
 Backup
Keep backups of your models and data versions
 Sharing
Share your outputs easily with other team members or services
 MLOps
Required for automating pipelines using tools like SageMaker, Airflow, etc.


 How It Fits in a Typical ML Pipeline
🛠 Local Workflow:
You run your training code → generate models, data splits, evaluation files.


These outputs are saved in artifacts/.


☁️ Cloud Workflow:
Then you upload those artifacts to S3 using the AWS_S3_BUCKET_NAME.


This allows you to access those files from any environment (your PC, server, AWS Lambda, SageMaker, etc.)



📁 Example Files You Might Upload to S3:
File
Purpose
model.pkl
Trained machine learning model
data.csv
Input or cleaned dataset
metrics.json
Accuracy, precision, recall, etc.
log.txt
Logs for debugging or audits


🔒 Bonus: Why Not Just Use Local Storage?
Local Storage
Cloud (S3)
Only on your machine
Accessible from anywhere
Lost if machine fails
Safely stored in cloud
Hard to scale or automate
Easily used in MLOps pipelines


✅ Final Summary
AWS_S3_BUCKET_NAME = "sensorpw" tells your code which S3 bucket to use.


You use it to upload or download files like models, datasets, or logs.


It's crucial for cloud storage, backups, collaboration, and production pipelines.


'''