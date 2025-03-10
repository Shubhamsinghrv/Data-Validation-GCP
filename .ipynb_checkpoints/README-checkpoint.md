# Data Validation on Google Cloud Platform (GCP)

## Overview
This project performs data validation between a source file (CSV) and a target file (JSON) stored in Google Cloud Storage (GCS). It compares records, detects mismatches, and generates reports.

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
├── notebook/                 # Jupyter notebooks for analysis
├── requirements.txt          # List of dependencies
```

## Installation
Ensure you have Python installed, then install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the validation script:
```bash
python main.py
```
This will:
- Read the source CSV file from GCS.
- Read the target JSON file from GCS.
- Compare records and detect mismatches.
- Generate `data_quality_summary.csv` and `detailed_mismatches.csv`.
- Log results in `data_quality_test_*.log`.

## Configuration
Modify `main.py` to set:
- `source_bucket`: GCS bucket containing the source CSV.
- `source_path`: Path to the source file.
- `target_bucket`: GCS bucket containing the target JSON.
- `target_path`: Path to the target file.
- `delimiter`: Field separator in the CSV (default `|`).

## Reports
- **`data_quality_summary.csv`**: Provides an overview of record counts and completeness percentage.
- **`detailed_mismatches.csv`**: Logs specific column mismatches with source and target values.
- **Logs**: Each validation run generates a log file (`data_quality_test_*.log`).
- **More than 20+ data quality checks** were performed, and results were listed in `data_quality_summary.csv`.

## Deployment
To containerize the application with Docker:
```bash
docker build -t data-validation .
docker run data-validation
```

## Visualization
Use the Jupyter notebooks in `notebook/` to analyze mismatch trends with Pandas and Matplotlib.

## License
MIT License.

---
For issues or contributions, open a pull request!

