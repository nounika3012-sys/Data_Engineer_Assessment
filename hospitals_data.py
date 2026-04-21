import requests
import pandas as pd
import os
import re
import json
from concurrent.futures import ThreadPoolExecutor

API_URL = "https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items"
DATA_DIR = "data"
LAST_RUN_FILE = "last_run.json"

os.makedirs(DATA_DIR, exist_ok=True)


def to_snake_case(name):
    name = re.sub(r"[^\w\s]", "", name)
    name = name.strip().lower()
    name = re.sub(r"\s+", "_", name)
    return name


def load_last_run():
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE) as f:
            return json.load(f)
    return {"last_run": None}


def save_last_run(timestamp):
    with open(LAST_RUN_FILE, "w") as f:
        json.dump({"last_run": timestamp}, f)


def get_hospital_datasets():
    response = requests.get(API_URL)
    data = response.json()

    hospital_datasets = [
    d for d in data
    if "hospital" in (
        " ".join(d.get("theme", [])) if isinstance(d.get("theme", ""), list) else d.get("theme", "")
    ).lower()
        
    ]

    return hospital_datasets


def download_dataset(dataset):
    csv_url = dataset.get("distribution", [{}])[0].get("downloadURL")

    if not csv_url:
        return

    file_name = dataset["title"].replace(" ", "_") + ".csv"
    path = os.path.join(DATA_DIR, file_name)

    df = pd.read_csv(csv_url,dtype=str
                     )

    df.columns = [snake_case(col) for col in df.columns]

    df.to_csv(path, index=False)

    print(f"Downloaded {file_name}")


def main():
    datasets = get_hospital_datasets()

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download_dataset, datasets)


if __name__ == "__main__":
    main()