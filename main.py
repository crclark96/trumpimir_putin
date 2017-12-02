from google.cloud import translate
import twitter
import sys
import json

with open('twitter_auth.json','r') as f:
    CREDENTIALS = json.load(f)
TRANSLATE_CLIENT = translate.Client.from_service_account_json('service_account.json')
TWITTER_API = twitter.Api(CREDENTIALS['consumer_key'],
                          CREDENTIALS['consumer_secret'],
                          CREDENTIALS['access_token'],
                          CREDENTIALS['access_token_secret'])

def to_russian(text):
    print "text: {}".format(text)
    try:
        text = text.encode('utf-8')
        target = 'ru'
        translation = TRANSLATE_CLIENT.translate(text,
                                                 target_language=target)
    except:
        print sys.exc_info()[0]
    print u"translation: {}".format(translation['translatedText'])
    return translation['translatedText']

def tweet(text):
    print u"tweeting: {}".format(text)
    try:
        status = TWITTER_API.PostUpdate(text)
        print "success"
    except Exception as e:
        print e
        return 0

    return status

def follow(user):
    if "@" not in user:
        return 0
    name = user.replace("@","")
    for line in TWITTER_API.GetUserStream(replies=None,
                                          withuser=user,
                                          filter_level=None):
        print u"received tweet: {}".format(line)
        if 'user' in line.keys() and line['user']['screen_name'] == name:
            status = to_russian(line['text'])
            tweet(status)

if __name__ == "__main__":
    follow("@realDonaldTrump")
