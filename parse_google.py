import json
import urllib
import urllib.parse
import urllib.request
import time
import os


def parse_google(query):
    google_api_key = 'yourkey'
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query, 'limit': 10, 'indent': True, 'key': google_api_key,
    }
    finalurl = service_url + '?' + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(finalurl).read())
    a = response["itemListElement"][0]['result']['detailedDescription']['articleBody']
    print(a)


if __name__ == '__main__':
    parse_google('obama')

