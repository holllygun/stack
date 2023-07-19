import requests
from pprint import pprint
url = "https://api.stackexchange.com/2.3/questions?fromdate=1689552000&todate=1689724800&order=desc&sort=activity&tagged=python&site=stackoverflow"
response = requests.get(url).json()
counter = 0
for inf in response['items']:
    print(inf['title'])
    print()
    counter += 1

print(f"Всего вопросов за последние 2 дня: {counter}")
