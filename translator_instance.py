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
