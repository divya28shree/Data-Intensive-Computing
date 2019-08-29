#!/usr/local/bin/python2.7
import requests
import argparse
import time
import json
import StringIO
import gzip
import csv
import codecs

from bs4 import BeautifulSoup

import sys

domain = 'billboard.com'
index_list = ["2019-13","2019-09","2019-04"]

#print("Hi")
record_list = []


for index in index_list:
        url = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index + "url=%s&matchType=domain&output=json" % domain
        response = requests.get(url)

        if response.status_code == 200:

            records = response.content.splitlines()

            for record in records:
                record_list.append(json.loads(record))

link_list = []
i=0
content_list = []
for record in record_list:

    if '/robotstxt/' in record['filename'] or '/crawldiagnostics/' in record['filename'] :
        continue

    offset, length = int(record['offset']), int(record['length'])
    offset_end = offset + length - 1

    startURL = 'https://commoncrawl.s3.amazonaws.com/'
    responseURL = requests.get(startURL + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})
    raw_data = StringIO.StringIO(responseURL.content)
    f = gzip.GzipFile(fileobj=raw_data)
    data = f.read()

    response = ""

    if len(data):
        try:
            warc, header, response = data.strip().split('\r\n\r\n', 2)
        except:
            pass

    parser = BeautifulSoup(response, "html.parser")
    text = parser.find_all("p")
    textReturn = ''
    if text:
        for p in text:
            # print p.getText()
            textReturn += p.getText()
    else:
        textReturn= 'No Text'
    if textReturn=='No Text' or textReturn=='None' or 'All rights reserved' in textReturn:#Not taking empyt or Copyright data
        continue
    else:
        if textReturn in content_list:
            #No Duplicates
            continue
        i += 1
        content_list.append(textReturn)
    print(text.strip())
    if i==500:
        break

