'''
We are making two functions to translate texts
'''

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('qbvniaiHI46OGcnEHU_CYNF3VtavHSMrSkqUx2MjPpnY')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
def translate(fromL,to,textIN):
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/c23a576f-5c4d-4cc4-a1fd-40bb57934225')

    translation = language_translator.translate(
        text=textIN,
        model_id=f'{fromL}-{to}').get_result()

    return translation['translations'][0]['translation']




def english_to_french(english_text):
    '''this translate english to french'''
    french_text=translate("en",'fr',english_text)
    return french_text

def french_to_english(french_text):
    '''this translate french to english'''
    english=translate("fr",'en',french_text)
    return english
