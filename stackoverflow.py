import requests
import json
from pprint import pprint
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# Gets all the questions on the site with tag PYTHON
todate = date.today()
fromdate = todate - relativedelta(days=+2)

header = {'Content-Type': 'application/json'}
params = {
        'fromdate': fromdate,
        'todate': todate,
        'order':'desc',
        'sort': 'creation',
        'tagged': 'python',
        'site': 'stackoverflow'
}

url = 'https://api.stackexchange.com/2.3/questions'
response = requests.get(url, headers=header, params=params)
result = json.loads(response.text)

for item in result['items']:
    owner = item['owner']['display_name']
    title = item['title']
    link = item['link']
    creation_date = datetime.fromtimestamp(item['creation_date']).strftime('%Y-%m-%d %H:%M:%S')
    print('============')
    print(f'Creation_date: {creation_date}\
        \nOwner: {owner}\
        \nQuestion : {title}\
        \nLink to question: {link}')
    print('============')