#!/usr/bin/env python3.6

import sys
import json
import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('url', help='URL to store the content of')
parser.add_argument('filename', help='the filename to store the content under')
parser.add_argument('--content-type', '-c',
                    default='html',
                    choices=['html', 'json'],
                    help='the content-type of the URL being requested')

args = parser.parse_args()

res = requests.get(args.url)

if res.status_code >= 400:
    print(f"Error code received: {res.status_code}")
    sys.exit(1)

if args.content_type == 'json':
    try:
        content = json.dumps(res.json())
    except ValueError:
        print("Error: content is not JSON")
        sys.exit(1)
else:
    content = res.text
    print(content)

with open('args.filename', 'w', encoding='UTF-8') as f:
    f.write(content)
    print(f"Content written to '{args.filename}'")
