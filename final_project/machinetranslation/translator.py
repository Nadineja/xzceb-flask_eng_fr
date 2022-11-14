import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)


def english_to_french(english_text):
    """Args:
    english_text: any--> (str)
    Function translates string in English into French
    if no input, error message is displayed.
    strips the API's response of all unnecessary information
    """
    if english_text is None:
        french_text = "No string has been entered"
        return french_text

    response = language_translator.translate(text=english_text, model_id="en-fr").get_result()
    f_translation = response['translations'][0]['translation']
    return f_translation


def french_to_english(french_text):
    """ Args:
    french_text: any --> (str)
    function translates string in French into English
    if no input, error message is displayed.
    strips the API's response of all unnecessary information
    """
    if french_text is None:
        english_text = "No string has been entered"
        return english_text

    response = language_translator.translate(text=french_text, model_id="fr-en").get_result()
    e_translation = response['translations'][0]['translation']  
    return e_translation
