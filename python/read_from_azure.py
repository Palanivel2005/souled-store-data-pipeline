from azure.identity import AzureCliCredential
from azure.storage.blob import BlobServiceClient

# Azure Storage Account URL
account_url = "https://stsouledstore2026.blob.core.windows.net"

# Authenticate using Azure CLI login
credential = AzureCliCredential()

# Connect to Azure Blob Storage
blob_service_client = BlobServiceClient(
    account_url=account_url,
    credential=credential
)

print("Azure connection successful!")

# Container and file details
container_name = "souled-store-data"
blob_name = "souled_store_products.csv"

# Access the CSV blob
blob_client = blob_service_client.get_blob_client(
    container=container_name,
    blob=blob_name
)

try:
    # Download the CSV file
    data = blob_client.download_blob().readall()

    # Display the first 500 characters
    print("\nCSV data downloaded successfully!")
    print(data.decode("utf-8")[:500])

except Exception as error:
    print("\nError reading Azure Blob Storage:")
    print(error)
