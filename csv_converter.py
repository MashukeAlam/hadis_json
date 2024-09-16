import json
import csv

def json_to_csv(json_file, csv_file):
    # Open and load the JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        hadith_data = json.load(f)
    
    # Open the CSV file for writing
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write the CSV header based on the keys from the first hadith entry
        header = ['narrator', 'english_text', 'hadith_link', 'reference']
        writer.writerow(header)
        
        # Write each hadith entry to the CSV file
        for hadith in hadith_data:
            writer.writerow([
                hadith.get('narrator', ''),
                hadith.get('english_text', ''),
                hadith.get('hadith_link', ''),
                hadith.get('reference', '')
            ])

    print(f"Data has been written to {csv_file}")

if __name__ == "__main__":
    # Convert the JSON file to CSV
    json_to_csv('hadith_data.json', 'hadith_data.csv')
