from googletrans import Translator

class Google_Translator:
    destinations = set(['en', 'ja'])
    
    def __init__(self, out_lang='en'):
        if out_lang in Google_Translator.destinations:
            self.out_lang = out_lang
        else:
            self.out_lang = 'en'
        self.translator = Translator()

    def translate(self, text):
        translated = self.translator.translate(text, dest=self.out_lang)
        return translated.text
