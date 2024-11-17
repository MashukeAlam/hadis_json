import requests
from bs4 import BeautifulSoup
import json

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL {url}: {e}")
        return None

def parse_hadith_page(html_content):
    # Initialize BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # List to hold all hadith data
    hadith_list = []

    # Find all hadith containers
    hadith_containers = soup.find_all('div', class_='actualHadithContainer')

    for container in hadith_containers:
        hadith_data = {}
        
        # Extract the English hadith text
        english_container = container.find('div', class_='english_hadith_full')
        if english_container:
            narrator = english_container.find('div', class_='hadith_narrated')
            text_details = english_container.find('div', class_='text_details')
            
            hadith_data['narrator'] = narrator.text.strip() if narrator else None
            hadith_data['english_text'] = text_details.text.strip() if text_details else None
        
        # Extract the Arabic hadith text (if needed)
        # arabic_container = container.find('div', class_='arabic_hadith_full')
        # if arabic_container:
        #     arabic_text = arabic_container.find('span', class_='arabic_text_details')
        #     hadith_data['arabic_text'] = arabic_text.text.strip() if arabic_text else None

        # Extract hadith link
        reference_td = container.find('td', string=lambda text: text and 'Reference' in text)
        if reference_td:
            next_td = reference_td.find_next_sibling('td')
            if next_td:
                link = next_td.find('a')
                if link:
                    href = link.get('href')
                    hadith_data['hadith_link'] = href
        
        # Extract hadith reference
        reference = container.find('div', class_='hadith_reference_sticky')
        hadith_data['reference'] = reference.text.strip() if reference else None

        # Add hadith data to the list
        hadith_list.append(hadith_data)

    return hadith_list

def main():
    base_url = 'https://sunnah.com/'

    books = ['bukhari', 'muslim', 'nasai', 'abudawud', 'tirmidhi', 'ibnmajah', 'malik', 'ahmad']
    page_ranges = {
        'bukhari': (1, 98),
        'muslim': (1, 57),
        'nasai': (1, 52),
        'abudawud': (1, 44),
        'tirmidhi': (1, 50),
        'ibnmajah': (1, 38),
        'malik': (1, 62),
        'ahmad': (1, 8)
    }

    all_hadith_data = []

    for book in books:
        for i in range(*page_ranges[book]):
            url = f"{base_url}{book}/{i}"
            print(f"GET: {url}", end='')
            html_content = fetch_html(url)
            
            if html_content:
                print(f" OK.") 
                hadith_data = parse_hadith_page(html_content)
                all_hadith_data.extend(hadith_data)
            
    # Save data to JSON file
    with open('hadith_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_hadith_data, f, ensure_ascii=False, indent=4)
    
    print(f"\nSAVED: hadith_data.json")

if __name__ == "__main__":
    main()
