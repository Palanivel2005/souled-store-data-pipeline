# Souled Store Data Engineering Pipeline

## Project Overview
This project extracts product data from The Souled Store API, stores the data in Azure Blob Storage, and cleans the data using Python.

## Architecture
API → Python Data Extraction → CSV/JSON → Azure Blob Storage → Data Cleaning → Cleaned CSV → Azure Blob Storage

## Technologies Used
- Python
- REST API
- Pandas
- Azure Blob Storage
- Azure Identity
- Azure CLI
- Git and GitHub

## Project Structure

```text
souled store/
├── README.md
├── .gitignore
└── python/
    ├── souled_store_api.py
    ├── read_from_azure.py
    └── clean_data.py
```

## Workflow

### 1. Extract Product Data
The `souled_store_api.py` script retrieves product data from The Souled Store API and saves the response as JSON and CSV files.

### 2. Store Data in Azure
The extracted CSV file is uploaded to Azure Blob Storage.

### 3. Read Data from Azure
The `read_from_azure.py` script connects to Azure Blob Storage using Azure CLI credentials and reads the stored product data.

### 4. Clean Data
The `clean_data.py` script:
- Removes unnecessary whitespace.
- Skips records missing product IDs or titles.
- Filters records with invalid prices.
- Saves the cleaned product data as a CSV file.
- Uploads the cleaned CSV to Azure Blob Storage.

## Azure Storage
- Storage service: Azure Blob Storage
- Container: `souled-store-data`
- Original file: `souled_store_products.csv`
- Cleaned file: `souled_store_products_cleaned.csv`

## Prerequisites
- Python 3
- Azure subscription and Storage Account
- Azure CLI
- Required Python packages

Install the required packages:

```bash
pip install requests pandas azure-storage-blob azure-identity
```

Sign in to Azure:

```bash
az login
```

## Run the Project

Run the scripts from the project root directory:

```bash
python python/souled_store_api.py
python python/read_from_azure.py
python python/clean_data.py
```

Ensure your Azure Storage Account and container are configured correctly and your signed-in Azure identity has the required Blob Storage permissions.

## Security Notes
- Do not commit Azure account keys, passwords, access tokens, or other credentials.
- CSV and JSON data files are excluded from Git using `.gitignore`.
- Azure resources may incur charges depending on usage.

## Future Improvements
- Automate extraction and cleaning on a schedule.
- Add logging and error handling.
- Implement automated data quality checks.
- Orchestrate the pipeline using Azure services.

## Author
Palanivel