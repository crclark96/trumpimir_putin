#!/usr/bin/env python

# Copyright 2007-2016 The Python-Twitter Developers

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ----------------------------------------------------------------------

# This file demonstrates how to track mentions of a specific set of users in 
# english language and archive those mentions to a local file. The output
# file will contain one JSON string per line per Tweet.

# To use this example, replace the W/X/Y/Zs with your keys obtained from
# Twitter, or uncomment the lines for getting an environment variable. If you
# are using a virtualenv on Linux, you can set environment variables in the
# ~/VIRTUALENVDIR/bin/activate script.

# If you need assistance with obtaining keys from Twitter, see the instructions
# in doc/getting_started.rst.

import os
import json

from twitter import Api

# Either specify a set of keys here or use os.getenv('CONSUMER_KEY') style
# assignment:

with open('twitter_auth.json','r') as f:
    credentials = json.load(f)

USER = '@thisistotestsom'
NAME = USER.replace("@","")

LANGUAGES = ['en']

api = Api(credentials['consumer_key'],
          credentials['consumer_secret'],
          credentials['access_token'],
          credentials['access_token_secret'])


def main():
    # api.GetStreamFilter will return a generator that yields one status
    # message (i.e., Tweet) at a time as a JSON dictionary.
    for line in api.GetUserStream(replies=None, withuser=USER, filter_level=None):
        print line
        print type(line)
        if 'user' in line.keys() and line['user']['screen_name'] == NAME:
            print line['text']
#         f.write(json.dumps(line))
#         f.write('\n')


if __name__ == '__main__':
    main()
