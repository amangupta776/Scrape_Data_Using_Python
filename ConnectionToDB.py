import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# Get environment variables
user=os.getenv("USER")
password=os.getenv('password')
host=os.getenv('host')
port=os.getenv('port')
database=os.getenv('database')


def insert_data_into_db(data):
    try:
        # Connect to the PostgreSQL server
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        print("Database 'ipl_data' connected successfully!")

        # Create a cursor
        cursor = connection.cursor()

        # Create the table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS data (
            "Year" text,
            "Winner" text,
            "Runner Up" text,
            "Final Match Venue" text,
            "Captain" text,
            "Teams" text,
            "Player of the Series" text,
            "Man of the Match" text
        );
        """
        cursor.execute(create_table_query)
        connection.commit()

        # Insert data into the table
        insert_query = """
        INSERT INTO data ("Year", "Winner", "Runner Up", "Final Match Venue", "Captain", "Teams", "Player of the Series", "Man of the Match")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, data)
        connection.commit()

        print("Data inserted successfully!")

    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Connection closed.")

