'''Main functions'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-09-22',
    authenticator=authenticator
)

language_translator.set_service_url(url)



def english_to_french(english_text):
    '''Translate English to french'''
    french_translation=language_translator.translate(
        text=english_text, model_id='en-fr'
        ).get_result()
    return french_translation['translations'][0]['translation']

def french_to_english(french_text):
    '''translate french to english'''
    english_translation=language_translator.translate(
        text=french_text, model_id='fr-en'
        ).get_result()
    return english_translation['translations'][0]['translation']
