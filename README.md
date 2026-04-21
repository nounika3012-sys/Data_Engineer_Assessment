# Description
This Python script downloads hospital-related datasets from the CMS provider data API. It filters datasets by the theme "hospital," downloads the CSV files, converts column headers to snake_case, and saves them locally in a `data` directory. The script uses multithreading to speed up downloads.

#Features
- Fetches datasets from CMS API
- Filters datasets with "hospital" in their theme
- Downloads CSV files and cleans column names
- Saves processed files in a local folder
- Uses ThreadPoolExecutor for parallel downloads

# Requirements
- Python 3.7 or higher
- `requests` library
- `pandas` library

# Installation
Install dependencies using pip:

```bash
pip install requests pandas
Usage
Run the script:

bashpython your_script_name.py
Downloaded CSV files will be saved in the data folder.

Functions
to_snake_case(name): Converts strings to snake_case format.
load_last_run(): Loads the timestamp of the last run (not currently used).
save_last_run(timestamp): Saves the timestamp of the last run (not currently used).
get_hospitals_datasets(): Fetches and filters hospital datasets from the API.
download_dataset(dataset): Downloads and processes a single dataset CSV.
main(): Coordinates dataset fetching and parallel downloading.


# Restaurant Business Data Model

This project also includes a data model designed for a restaurant business that plans to expand into multiple locations, food trucks, and franchise operations. The goal of the model is to support data-driven decision making by capturing operational and transactional data across the business.

The model tracks important entities such as customers, orders, menu items, employees, inventory, suppliers, and franchise ownership.

Two levels of modeling are included:

Logical Data Model

The logical model represents the high-level business entities and relationships without implementation details. It focuses on how core business concepts interact, such as customers placing orders, orders containing menu items, and locations managing employees and inventory.

Physical Data Model

The physical model defines the actual database schema, including tables, columns, primary keys, foreign keys, and relationships. This model is designed to support operational reporting and analytics for restaurant operations.

The schema supports the following business capabilities:
	•	Tracking customer orders and payments
	•	Managing menu items and categories
	•	Monitoring inventory and ingredient usage
	•	Managing restaurant locations and food trucks
	•	Supporting franchise ownership structures
	•	Tracking employee assignments per location
	•	Analyzing sales and operational performance

An ER diagram representing the physical database model is included in this repository.


