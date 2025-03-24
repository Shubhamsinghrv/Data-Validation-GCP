# Data Validation System

## Overview
This Data Validation System ensures data accuracy and consistency by comparing source and target datasets. The system is designed for high performance and scalability, achieving 99.9% accuracy and processing 500,000+ records in under 1 minute using a VM on GCP.

## Project Structure
```
Data-Validation-GCP/
├── Data_Validation.py        # Core data validation script
├── Dockerfile                # Docker configuration for deployment
├── README.md                 # Project documentation
├── data_quality_summary.csv  # Summary of validation results
├── detailed_mismatches.csv   # Detailed mismatch report
├── data_quality_test_*.log   # Log files for debugging
├── main.py                   # Entry point for running validation            
├── requirements.txt          # List of dependencies
```

## 🔄 Workflow

A source file and target file are uploaded to a Google Cloud Storage (GCS) bucket.

This triggers a Pub/Sub event.

The Pub/Sub event activates a Cloud Run container.

The Cloud Run container runs the data validation script.

Validation results and detailed mismatches are stored back in the GCS bucket.

## ✨ Features

Automated Data Validation: Compares source and target data efficiently.

Parallel Processing: Uses concurrent execution for fast validation.

Mismatch Detection: Identifies discrepancies between datasets.

Scalability: Can handle large datasets with ease.

Cloud-Native: Fully integrated with GCP services.

Logging & Reporting: Generates logs and CSV reports for analysis.

## 🛠️ Tech Stack

Google Cloud Platform (GCP) (GCS, Pub/Sub, Cloud Run)

Python

Flask & Flask-SocketIO (for backend processing)

Pandas & NumPy (for data analysis)

Matplotlib (for visualization)

Concurrent.Futures (for parallel processing)

# 📦 Installation & Setup

## 1️⃣ Clone the Repository

git clone https://github.com/shubhamsinghrv/Data-Validation-System.git
cd Data-Validation-System

## 2️⃣ Install Dependencies

pip install -r requirements.txt

## 3️⃣ Run the Validation Script Locally

python data_validation.py

## ☁️ Deployment on GCP

Push the project to GitHub.

Deploy the backend on Cloud Run Container.

Configure Pub/Sub to trigger Cloud Run.

Upload test files to the GCS bucket to trigger validation.

## 📊 Output Reports

Summary Report (data_quality_summary.csv)

Detailed Mismatches (detailed_mismatches.csv)

Mismatch Visualization (Graphical insights into discrepancies)

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.


🚀 Developed with high accuracy and efficiency for large-scale data validation!
