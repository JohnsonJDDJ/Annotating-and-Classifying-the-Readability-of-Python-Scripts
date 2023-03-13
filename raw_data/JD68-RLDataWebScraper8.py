# for valid status = false && color is empty, rerun S1 to extract images
import requests
from bs4 import BeautifulSoup
import time

api_url = 'http://127.0.0.1:3000/items'

# Get the current list of daily items from the API
response = requests.get(api_url)
items = response.json()

updated_count = 0
skipped_count = 0

last_attempted_item = 0

# Go through each item and update the image
for item in items:
    if last_attempted_item is not None and item['id'] < last_attempted_item:
        continue
    if not item['valid_status'] or item['color']:
        skipped_count += 1
        continue
    while True:
        try:
            img_location = item['image_location']
            img_response = requests.get(img_location)
            img_html = img_response.text
            img_div_start = img_html.find('<div id="itemSummaryImage">')
            if img_div_start != -1:
                img_div_end = img_html.find('</div>', img_div_start)
                img_div = img_html[img_div_start:img_div_end+6]
                img_url_start = img_div.find('<img src="')
                img_url_end = img_div.find('"', img_url_start+10)
                img_url = img_div[img_url_start+10:img_url_end]
                item_data = {'image': img_url, 'valid_status': True}
                patch_response = requests.patch(api_url+'/'+str(item['id']), json=item_data)
                print(f"{item['id']} Image updated")
                updated_count += 1
            else:
                print(f"{item['id']} No image found")
                item_data = {'valid_status': False}
                patch_response = requests.patch(api_url+'/'+str(item['id']), json=item_data)
                skipped_count += 1
            last_attempted_item = item['id']
            break
        except Exception as e:
            print(f"Error updating item {item['id']}: {e}")
            print(f"Retrying in 5 minutes...")
            time.sleep(5 * 60)

print(f"Updated {updated_count} items")
print(f"Skipped {skipped_count} items")