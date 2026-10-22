# Souled Store E-Commerce Data Engineering Project

## Project Overview

This project extracts product data from The Souled Store listing endpoint using Python, cleans the data, and stores the original and cleaned CSV files in Azure Blob Storage.

## Architecture

API → Python Extraction → CSV → Azure Blob Storage → Python Data Cleaning → Cleaned CSV → Azure Blob Storage

## Technologies Used

* Python
* Requests
* CSV and JSON
* Microsoft Azure Blob Storage
* Azure CLI
* Azure Identity SDK
* Azure Storage Blob SDK
* Git and GitHub

## Project Workflow

1. Extract product listing data using Python.
2. Save the extracted data as JSON and CSV files.
3. Upload the original CSV to Azure Blob Storage.
4. Download the CSV from Azure using Python.
5. Clean the product data by trimming whitespace, validating product IDs and titles, and checking prices.
6. Upload the cleaned CSV back to Azure Blob Storage.
7. Verify the cleaned file contains 24 valid product records.

## Azure Storage Details

* Storage account: `stsouledstore2026`
* Container: `souled-store-data`
* Original file: `souled_store_products.csv`
* Cleaned file: `souled_store_products_cleaned.csv`

## Run the Project

Install the required packages:

```bash
python -m pip install requests azure-storage-blob azure-identity
```

Run the extraction script:

```bash
python python/souled_store_api.py
```

Read the original CSV from Azure:

```bash
python python/read_from_azure.py
```

Clean the data and upload the result:

```bash
python python/clean_data.py
```

Azure CLI authentication must be configured before running the Azure scripts.

## Notes

* The current run produced 24 valid product records.
* The product listing endpoint may change or restrict access. Confirm permission to use it before automating data extraction.
* Do not commit credentials, access keys, tokens, or `.env` files to GitHub.
* Azure resources may incur charges. Review the Azure cost and resource status when finished.
