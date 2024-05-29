from google.cloud import storage
import os

def download_bucket(bucket_name, destination_dir):
  """Downloads all files from a Google Cloud Storage bucket to a local directory.

  Args:
    bucket_name: The name of the bucket to download from.
    destination_dir: The local directory to download the files to.
  """
  # Authenticate to Google Cloud Storage
  storage_client = storage.Client(project="project_code")

  # Get the bucket object
  bucket = storage_client.bucket(bucket_name)

  # Iterate through all blobs in the bucket
  for blob in bucket.list_blobs():
    # Construct the local filename (consider preserving directory structure)
    filename = blob.name.strip("/")  # Remove leading/trailing slashes
    local_path = os.path.join(destination_dir, filename)

    # Download the blob to the local file
    blob.download_to_filename(local_path)
    print(f"Downloaded: {blob.name} to {local_path}")

# Replace with your bucket name and desired download directory
#bucket_name = "your-bucket-name"
bucket_name = "bucket-name"
destination_dir = "C:/Users/local/path"

download_bucket(bucket_name, destination_dir)