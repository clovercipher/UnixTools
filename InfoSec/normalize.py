__author__ = 'cl0v3r'
'''
normalize.py
This file contains classes for regulating and normalizing data
for processing data. Examples include data that is contained within
tags such as HTML and XML.
'''

from HTMLParser import HTMLParser

'''
HTMLParser subclass that strips HTML tags from data. Code borrowed
from StackExchange post:
https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
'''
class MLStripper(HTMLParser):

    def __init__(self):
        self.reset()
        self.output = []

    def handle_data(self, data):
        self.output.append(data)

    def get_data(self):
        return ''.join(self.output)

