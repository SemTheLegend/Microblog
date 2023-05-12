import json, uuid
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
        not app.config['MS_TRANSLATOR_KEY']:
            return _('Error: the translation service is not configured.')
    auth = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
    # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': "southafricanorth",
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
        # 'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        # 'Ocp-Apim-Subscription-Region': 'southafricanorth'
    }
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com/'
        '/translate?api-version=3.0&from={}&to{}'.format(
            source_language, dest_language
        ), headers=auth, json=[{'Text': text}]
    )
    # if r.status_code != 200:
    #     return _('Error: the translation service failed.')
    return r.json()


def translate2(body, source_lang, trans_lang ):
    import requests, uuid, json, os

# Add your key and endpoint
    key =  os.environ.get('MY_TRANSLATOR_KEY')
    endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = "southafricanorth"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': source_lang,
        'to': trans_lang
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
# You can pass more than one object in body.
    body = body

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    print(json.dumps(response)['translations'])
    