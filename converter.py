import requests
from datetime import datetime
import csv
import os

date = datetime.now().strftime('%d-%m-%Y %H:%M')
converter = 'converter.csv'
file_exists = os.path.isfile(converter)

url = 'https://api.exchangerate-api.com/v4/latest/USD'
response = requests.get(url)
data = response.json()

ngn_rate = f"₦{data['rates']['NGN']}"
gbp_rate = f"£{data['rates']['GBP']}"

with open(converter, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(['Timestamp', 'USD to NGN', 'USD to GBP'])
    writer.writerow([date, ngn_rate, gbp_rate])

print(f'💰 $1 = {ngn_rate}')
print(f'💰 $1 = {gbp_rate}')
print(f'✅ Saved to {converter} at {date}')
