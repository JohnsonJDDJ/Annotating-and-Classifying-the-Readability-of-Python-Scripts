# image_uri extractor
import requests
from bs4 import BeautifulSoup
import time

import json

api_url = 'http://127.0.0.1:3000/items'

# Get the current list of daily items from the API
response = requests.get(api_url)
items = response.json()

updated_count = 0
skipped_count = 0

last_attempted_item = 0

# Go through each item and update the image URI
for item in items:
    if item['id'] < 57722:
        continue
    if last_attempted_item is not None and item['id'] < last_attempted_item:
        continue
    if item['valid_status'] is True:
        skipped_count += 1
        continue
    while True:
        try:
            search_url = f"https://rl.insider.gg/en/pc/search?q={item['name'].replace(' ', '+')}"
            search_response = requests.get(search_url)
            search_html = search_response.text
            search_soup = BeautifulSoup(search_html, 'html.parser')
            search_items = search_soup.find_all('div', class_='item')
            for search_item in search_items:
                if search_item.find('span', class_='itemName').text.lower() == item['name'].lower():
                    img_uri = search_item['data-uri']
                    if "import/import" in img_uri:
                        img_uri = img_uri.replace("import/import", "import")
                    item['image_uri'] = img_uri
                    patch_response = requests.patch(api_url+'/'+str(item['id']), json={'image_uri': img_uri})
                    print(f"{item['id']} Image URI updated")
                    updated_count += 1
                    break
            else:
                print(f"{item['id']} No image URI found")
                skipped_count += 1
            last_attempted_item = item['id']
            break
        except Exception as e:
            print(f"Error updating item {item['id']}: {e}")
            print(f"Retrying in 5 minutes...")
            time.sleep(5 * 60)
            continue

print(f"Updated {updated_count} items")
print(f"Skipped {skipped_count} items")