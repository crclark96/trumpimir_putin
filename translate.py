from google.cloud import translate

def quickstart():
    translate_client = translate.Client.from_service_account_json('service_account.json')
    
    text = u'Hello, world!'
    
    target = 'ru'
    
    translation = translate_client.translate(text,
                                             target_language=target)
    
    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translation['translatedText']))

if __name__ == "__main__":
    quickstart()
