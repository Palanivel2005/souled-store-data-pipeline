import csv
from io import StringIO
from azure.identity import AzureCliCredential
from azure.storage.blob import BlobServiceClient

# Azure Storage connection
account_url = "https://stsouledstore2026.blob.core.windows.net"
container_name = "souled-store-data"
input_blob = "souled_store_products.csv"
output_blob = "souled_store_products_cleaned.csv"

credential = AzureCliCredential()
blob_service = BlobServiceClient(
    account_url=account_url,
    credential=credential
)

# Download original CSV from Azure
blob_client = blob_service.get_blob_client(
    container=container_name,
    blob=input_blob
)
csv_data = blob_client.download_blob().readall().decode("utf-8-sig")

# Clean CSV data
reader = csv.DictReader(StringIO(csv_data))
cleaned_rows = []

for row in reader:
    # Remove extra spaces from text fields
    row = {
        key: value.strip() if value else ""
        for key, value in row.items()
    }

    # Skip rows without product ID or title
    if not row.get("id") or not row.get("title"):
        continue

    # Remove rows with invalid prices
    try:
        row["price"] = str(float(row["price"]))
    except (ValueError, TypeError):
        continue

    cleaned_rows.append(row)

if not cleaned_rows:
    raise ValueError("No valid product rows found. Check the CSV headers and data.")

# Convert cleaned data back to CSV
output = StringIO()
writer = csv.DictWriter(output, fieldnames=cleaned_rows[0].keys())
writer.writeheader()
writer.writerows(cleaned_rows)

# Upload cleaned CSV to Azure
output_client = blob_service.get_blob_client(
    container=container_name,
    blob=output_blob
)
output_client.upload_blob(output.getvalue().encode("utf-8"), overwrite=True)

print(f"Cleaning complete! Valid products: {len(cleaned_rows)}")
print(f"Uploaded to Azure: {output_blob}")
