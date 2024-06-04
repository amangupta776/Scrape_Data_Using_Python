IPL Database Management and Scraping Application
Overview:
This application performs CRUD (Create, Read, Update, Delete) operations on an IPL database and scrapes IPL winners' data from a web page to insert it into the database. It consists of the following main components:

scrape_data.py: Scrapes data from a specified URL and saves it to a PostgreSQL database and a CSV file.
connectionToDb.py: Contains the function to insert data into the PostgreSQL database and create the table if it does not exist.
crud.py: Contains functions for CRUD operations on the PostgreSQL database.
generate_csv.py: Contains the function to generate a CSV file from the scraped data.
Prerequisites
Python 3.x
PostgreSQL
psycopg2 library
dotenv library
beautifulsoup4 library
requests library

Setup
Step 1: Install Required Libraries
Install the required libraries using pip:
pip install psycopg2-binary python-dotenv beautifulsoup4 requests dotenv
Step 2: Set Up the Database
Create a PostgreSQL database named ipl_data.

Step 3: Environment Variables
Create a .env file in the root directory of your project and add your PostgreSQL database credentials:

USER=your_db_user
password=your_db_password
host=your_db_host
port=your_db_port
database=ipl_data
Replace the placeholders (your_db_user, your_db_password, etc.) with your actual PostgreSQL credentials.

Usage
Scraping and Inserting Data
Run the scrape_data.py script to scrape data from the specified URL and insert it into the PostgreSQL database and save it to a CSV file:

python scrape_data.py
CRUD Operations
The CRUD operations are defined in crud.py. You can uncomment the desired function calls at the bottom of scrape_data.py to perform specific operations:

python
Copy code
# Uncomment the desired function(s) to execute
# CRUD.delete_data_from_db()
# CRUD.update_data_in_db()
# CRUD.retrieve_data_from_db()
# CRUD.insert_data()
Each CRUD function can also be called directly from an interactive Python session or another script.

Retrieve Data
To retrieve all data from the database, call the retrieve_data_from_db function:

import CRUD
CRUD.retrieve_data_from_db()
Update Data
To update data in the database, call the update_data_in_db function and follow the prompts:

import CRUD
CRUD.update_data_in_db()
Delete Data
To delete data from the database, call the delete_data_from_db function and follow the prompts:


import CRUD
CRUD.delete_data_from_db()
Insert Data
To insert new data into the database, call the insert_data function and follow the prompts:

import CRUD
CRUD.insert_data()
Files Description
scrape_data.py: This script scrapes data from the given URL and inserts it into the PostgreSQL database. It also writes the scraped data to a CSV file using the generateCSV function from generate_csv.py.
connectionToDb.py: This script contains functions to connect to the PostgreSQL database, create the data table if it doesn't exist, and insert data into the database.
crud.py: This script contains functions for performing CRUD operations on the data table in the PostgreSQL database.
generate_csv.py: This script contains a function to generate a CSV file from the provided data.
Note
Ensure your PostgreSQL server is running and the database credentials in the .env file are correct before running any scripts.