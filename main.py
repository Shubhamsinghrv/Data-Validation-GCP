from fastapi import FastAPI, HTTPException
from google.cloud import storage
from fastapi.responses import StreamingResponse
import pandas as pd
from io import StringIO

# Initialize the FastAPI app
app = FastAPI()

# GCS bucket and file name
BUCKET_NAME = "intelli-ana-bucket"
CSV_FILE_NAME = "detailed_mismatches.csv"

# Initialize the Google Cloud Storage client
storage_client = storage.Client()

@app.get("/")
def root():
    return {"message": "API is running and connected to GCS"}

@app.get("/get-csv-content")
def get_csv_content():
    try:
        # Get the bucket and blob (file) from GCS
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(CSV_FILE_NAME)

        # Download the content of the CSV file
        csv_data = blob.download_as_text()

        # Convert the CSV content to a Pandas DataFrame
        df = pd.read_csv(StringIO(csv_data))

        # Convert the DataFrame to a JSON-like format and return
        return df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching CSV content: {e}")


@app.get("/download-csv")
def download_csv():
    """
    Provide the CSV file as a downloadable stream.
    """
    try:
        # Get the bucket and blob (file) from GCS
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(CSV_FILE_NAME)

        # Stream the file content
        csv_data = blob.download_as_text()
        response = StreamingResponse(
            iter([csv_data]),
            media_type="text/csv"
        )
        response.headers["Content-Disposition"] = f"attachment; filename={CSV_FILE_NAME}"
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error downloading CSV file: {e}")
