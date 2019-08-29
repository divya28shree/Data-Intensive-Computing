import urllib
import json
import datetime
import time
import sys, os
import logging
import codecs


def daterange(start_date, end_date):
    if start_date <= end_date:
        for n in range((end_date - start_date).days + 1):
            yield start_date + datetime.timedelta(n)
    else:
        for n in range((start_date - end_date).days + 1):
            yield start_date - datetime.timedelta(n)


json_file_path = '/home/divya/Desktop/DIC/Lab2/NYT/data'
api_key = 'API Key for NYT'
start = datetime.date(2019, 1, 1)
end = datetime.date(2019, 4, 20)
query = 'cathedral'
topic = 'Lens'
i = 1
for date in daterange(start, end):
    print('date:', date)
    print(i)
    i+=1
    date = date.strftime("%Y%m%d")#q=" + query + "
    #+ "begin_date=" + date + "&end_date=" + date
    request_string = "http://api.nytimes.com/svc/search/v2/articlesearch.json?page="+str(i)+"&api-key=" + api_key + "&fq=section_name:(" + topic + ")"
    print (request_string)
    responseNYT = urllib.urlretrieve(request_string)
    content = open(responseNYT[0]).read()
    #print (content)
    json_response = json.loads(content)
    if 'fault' in json_response:
        time.sleep(60)
        i=1
        continue
    if json_response =="":
        continue
    response = json_response['response']
    docs = response['docs']
    for doc in docs:
        if '/2018/' in doc['web_url']:
            continue
        print(doc['web_url'])
        with open('/home/divya/Desktop/DIC/Lab2/NYT/URLs/' + query + 'TTLNew.txt', 'a') as f:
            f.write(doc['web_url']+"\n")
            f.close()
