import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        hadith_data = json.load(f)
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        header = ['narrator', 'english_text', 'hadith_link', 'reference']
        writer.writerow(header)
        
        for hadith in hadith_data:
            writer.writerow([
                hadith.get('narrator', ''),
                hadith.get('english_text', ''),
                hadith.get('hadith_link', ''),
                hadith.get('reference', '')
            ])

    print(f"Data has been written to {csv_file}")

if __name__ == "__main__":
    json_to_csv('hadith_data.json', 'hadith_data.csv')
