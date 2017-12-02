#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Post a message to twitter'''

from __future__ import print_function

__author__ = 'dewitt@google.com'

try:
    import configparser
except ImportError as _:
    import ConfigParser as configparser

import getopt
import os
import sys
import twitter
import json

def main():

    with open('twitter_auth.json','r') as f:
        credentials = json.load(f)

    message = unicode('Это тест',encoding='utf-8')

    api = twitter.Api(credentials['consumer_key'],
                      credentials['consumer_secret'],
                      credentials['access_token'],
                      credentials['access_token_secret'])

    try:
        status = api.PostUpdate(message)
    except UnicodeDecodeError:
        print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
        print("Try explicitly specifying the encoding with the --encoding flag")
        sys.exit(2)

    print(u"{0} just posted: {1}".format(status.user.name, status.text))

if __name__ == "__main__":
    main()
