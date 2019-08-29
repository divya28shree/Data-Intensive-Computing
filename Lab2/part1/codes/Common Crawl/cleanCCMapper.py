#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
import sys
import emoji
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


punctuations = '''+!()-[]{};:'"#@\,<>./?$%^&*_~'''

stop_words = set(stopwords.words('english'))


def give_emoji_free_text(text):
    emoji_list = map(lambda x: ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
    clean_text = ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text

def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)


for line in sys.stdin:
    filtered_sentence=""
    text = line.lower()
    text = give_emoji_free_text(text)
    text = remove_urls(text)
    line1 = ""
    for char in text:
        if char not in punctuations:
            line1 = line1 + char
    # print(line1)
    words = line1.split()  # word_tokenize(line1)
    for word in words:
        word = lemmatizer.lemmatize(word)
        if word not in stop_words:
            filtered_sentence = filtered_sentence + " " + word
    print(filtered_sentence.encode('utf-8'))