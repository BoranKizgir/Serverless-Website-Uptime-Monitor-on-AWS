Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
... import urllib3
... import boto3
... import time
... 
... http = urllib3.PoolManager()
... dynamodb = boto3.resource('dynamodb')
... table = dynamodb.Table('WebsiteTime')
... 
... # Kontrol etmek istediğin siteleri buraya ekle
... URLS = ["https://www.google.com", "https://www.amazon.com", "https://vagectim.com"]
... 
... def lambda_handler(event, context):
...     for url in URLS:
...         start_time = time.time()
...         try:
...             # 5 saniye içinde cevap gelmezse hata say
...             response = http.request('GET', url, timeout=5.0)
...             status = response.status
...         except:
...             status = 0 # Site çökmüşse status 0
...         
...         latency = round((time.time() - start_time) * 1000, 2) # Milisaniye cinsinden
...         
...         table.put_item(Item={
...             'URL': url,
...             'Timestamp': int(time.time()),
...             'Status': status,
...             'Latency': str(latency) + "ms"
...         })
...     
