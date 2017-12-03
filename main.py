from google.cloud import translate
import twitter
import sys
import json
import os

DEBUG = os.getenv("DEBUG")

with open('twitter_auth.json','r') as f:
    CREDENTIALS = json.load(f)
TRANSLATE_CLIENT = translate.Client.from_service_account_json('service_account.json')
TWITTER_API = twitter.Api(CREDENTIALS['consumer_key'],
                          CREDENTIALS['consumer_secret'],
                          CREDENTIALS['access_token'],
                          CREDENTIALS['access_token_secret'])
LOG = open('debug.log','a')


def to_russian(text):
    text = text.encode('utf-8')
    print "text: " + text
    LOG.write("text: " + text)
    try:
        target = 'ru'
        translation = TRANSLATE_CLIENT.translate(text,
                                                 target_language=target)
        translation['translatedText'] = translation['translatedText']\
                                        .encode('utf-8')
        print "translation: " + translation["translatedText"]
        LOG.write("translation: " + translation["translatedText"])
        return translation['translatedText']
    except:
        print sys.exc_info()[0]
        LOG.write(sys.exc_info()[0])
        sys.exit(1)


def tweet(text):
    print "tweeting: " + text
    LOG.write("tweeting: " + text)
    try:
        if DEBUG:
            print text
            return 0
        else:
            status = TWITTER_API.PostUpdate(text)
            return status
        print "success"
        LOG.write("success")
    except Exception as e:
        print e
        LOG.write(e)
        sys.exit(1)


def follow(user):
    if "@" not in user:
        return 0
    name = user.replace("@","")
    for line in TWITTER_API.GetUserStream(replies=None,
                                          withuser=user,
                                          filter_level=None):
        print "received tweet: " + unicode(line)
        LOG.write("received tweet: " + unicode(line))
        if 'user' in line.keys() and line['user']['screen_name'] == name:
            status = to_russian(line['text'])
            tweet(status)

if __name__ == "__main__":
    if DEBUG:
        follow("@thisistotestsom")
    else:
        follow("@realDonaldTrump")
