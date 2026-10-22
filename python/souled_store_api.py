import requests
import json
import csv

url = "https://api.thesouledstore.com/api/v2/pre-order/products/listing"

payload = {
    "artist": "",
    "category": "",
    "filters": {},
    "gender_type": 1,
    "is_exclusive": 0,
    "offset": 24,
    "page": 1,
    "tags": "men-all-linen",
    "tiptitle": 1
}

try:
    response = requests.post(
        url,
        json=payload,
        timeout=30
    )

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        # Display API response
        print("API data fetched successfully!")

        # Save data to JSON file
        with open(
            "souled_store_products.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("Data saved successfully!")
        print("File: souled_store_products.json")
        # Save products to CSV
        products = data.get("products", [])

        if products:
            with open(
                "souled_store_products.csv",
                "w",
                newline="",
                encoding="utf-8"
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "id",
                        "title",
                        "price",
                        "exclusive_price",
                        "stock",
                        "artist",
                        "category",
                        "product_slug"
                    ],
                    extrasaction="ignore"
                )

                writer.writeheader()

                for product in products:
                    row = product.copy()
                    row["category"] = ", ".join(
                        row.get("category", [])
                    )
                    writer.writerow(row)

            print("CSV saved successfully!")
            print("File: souled_store_products.csv")

    else:
        print("API request failed.")
        print(response.text[:1000])

except requests.RequestException as error:
    print("Error:", error)

except json.JSONDecodeError:
    print("Error: API response is not valid JSON.")
