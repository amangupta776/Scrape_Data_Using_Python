# main file
from bs4 import BeautifulSoup
import requests
import ConnectionToDB
import psycopg2
import CRUD
import generate_csv

def main():
    try:
        # Define the URL to scrape
        url = "https://www.careerpower.in/ipl-winners-list.html"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Fetch data from the website
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.select("table")[1]
        tr = data.tbody.find_all("tr")

        # Create a list to store the data
        rows = []

        # Extract data from each row
        for i in tr:
            td = i.find_all("td")
            row_data = [t.get_text().replace("\xa0", "") for t in td]  # Replace "\xa0" with ""
            rows.append(row_data)
            
            # Insert data into the database (excluding header row)
            if row_data[0] != 'Year':
                ConnectionToDB.insert_data_into_db(row_data)

        # This Function For Generate CSV File 
        generate_csv.generateCSV(rows)

    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
    # Uncomment the desired function(s) to execute
    # CRUD.delete_data_from_db()
    # CRUD.update_data_in_db()
    # CRUD.retrieve_data_from_db()
    # CRUD.insert_data()
