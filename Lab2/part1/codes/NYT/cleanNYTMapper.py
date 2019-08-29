#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
import json
import sys
import urllib
from bs4 import BeautifulSoup
import emoji
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords
lemmatizer = WordNetLemmatizer()

json_file_path = '/home/divya/Desktop/DIC/Lab2/NYT/data'

punctuations = '''!()-[]{};:'"#@\,<>./?$%^&*_~'''

stop_words = set(stopwords.words('english'))

i=1;

def give_emoji_free_text(text):
    emoji_list = map(lambda x: ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
    clean_text = ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text

def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)

for line in sys.stdin:
    filtered_sentence = ""
    url = str(line.strip())
    art = urllib.urlretrieve(url)
    article = open(art[0]).read()
    soup = BeautifulSoup(article, "html.parser")
    body = soup.find('div', {'class': 'StoryBodyCompanionColumn'})
    contentFinal = ""
    words = 0
    # print(body)
    pa = soup.findAll('p', {'class': 'evys1bk0'})

    for p in pa:
        # print p.getText()
        contentFinal += p.getText()
    #print(contentFinal)
    contentFinal = contentFinal.replace('AdvertisementSupported by', '')
    contentFinal = contentFinal.replace('Advertisement', '')
    #print(contentFinal)
    text = contentFinal.lower()
    text = give_emoji_free_text(text.encode('utf8'))
    text = remove_urls(text)
    line1 = ""
    for char in text:
        if char not in punctuations:
            line1 = line1 + char
    #print(line1)
    words = line1.split()#word_tokenize(line1)
    for word in words:
	word = lemmatizer.lemmatize(word)
        if word not in stop_words:
            filtered_sentence=filtered_sentence+" "+word
    print(filtered_sentence.encode('utf-8'))
