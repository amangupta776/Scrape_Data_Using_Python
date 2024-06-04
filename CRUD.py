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

def retrieve_data_from_db():
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

        # Execute the SELECT query
        select_query = """
        SELECT * FROM data;
        """
        cursor.execute(select_query)

        # Fetch all rows
        datas = cursor.fetchall()

        #print data 
        for data in datas:
            print(data)


    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Connection closed.")

def update_data_in_db():
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
        
        new_winner=input("Enter new winner : ")
        year=input("Enter year : ")

        # Update the winner for a specific year
        update_query = """
        UPDATE data SET "Winner" = %s WHERE "Year" = %s;
        """
        cursor.execute(update_query, (new_winner, year))
        connection.commit()

        print(f"Data updated successfully for year {year}!")

    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Connection closed.")

def delete_data_from_db():
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

        year=input("Enter year : ")
   
        # Delete data for a specific year
        delete_query = """
        DELETE FROM data WHERE "Year" = %s;
        """
        cursor.execute(delete_query, (year,))
        connection.commit()

        print(f"Data deleted successfully for year {year}!")

    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Connection closed.")


def insert_data():
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

        # Take input from user
        Year = input("Enter Year: ")
        Winner = input("Enter Winner: ")
        Runner_Up = input("Enter Runner Up: ")
        Final_Match_Venue = input("Enter Final Match Venue: ")
        Captain = input("Enter Captain: ")
        Teams = input("Enter Teams: ")
        Player_of_the_Series = input("Enter Player of the Series: ")
        Man_of_the_Match = input("Enter Man of the Match: ")

        # Insert data into the table
        insert_query = """
        INSERT INTO data ("Year", "Winner", "Runner Up", "Final Match Venue", "Captain", "Teams", "Player of the Series", "Man of the Match")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (Year, Winner, Runner_Up, Final_Match_Venue, Captain, Teams, Player_of_the_Series, Man_of_the_Match))
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


