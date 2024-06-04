import csv

def generateCSV(data):
            # Define the CSV file name
        csv_file = "ipl_winners.csv"

        # Write the data to the CSV file
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)  # Write data rows

        print(f"Data saved to {csv_file}")