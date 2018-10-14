#!/home/user/sample/venvs/experiment/bin/python

import os
import requests
import sys

from argparse import ArgumentParser

parser = ArgumentParser(description='get the current weather info for your zipcode')

parser.add_argument('zip', help='zip/postal code to get weather for')

parser.add_argument('--country', default='us', help='country zip/postal belogs to, default is "us"')

args = parser.parse_args()

api_key = os.getenv("OWM_API_KEY")

if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res = requests.get(url)

if res.status_code != 200:
    print(f"Error talkinf to weather provided: {res.status_code}")
    sys.exit(1)

print(res.json())

