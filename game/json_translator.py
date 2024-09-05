import json
from json import JSONDecodeError

class JSONTranslator:

    def __init__(self) -> None:
        self._list_of_languages = self.get_json_keys()
    
    @property
    def list_of_languages(self):
        return self._list_of_languages

    def set_language(self, language):
        if language.upper() not in self._list_of_languages:
            self._language = "ES"
        else:
            self._language = language.upper()

    def get_json_keys(self):
        try:
            with open('textos.json') as f:
                textos_json = json.load(f)
                return list(textos_json.keys())
        except JSONDecodeError as e:
            raise Exception("Error decoding JSON file: Please check the formatting of your 'textos.json'.") from e
        except FileNotFoundError:
            raise FileNotFoundError("JSON file 'textos.json' not found.")
        except Exception as e:
            raise Exception(f"Unexpected error: {e}")

    def read_json(self, name_of_input):
        try:
            with open('textos.json') as f:
                textos_json = json.load(f)
                try:
                    response = textos_json[self._language][name_of_input]
                except KeyError:
                    try:
                        response = textos_json["ES"][name_of_input]
                    except KeyError:
                        raise KeyError(f"Text '{name_of_input}' not found in 'ES' language.")
            return response
        except JSONDecodeError as e:
            raise Exception("Error decoding JSON file: Please check the formatting of your 'textos.json'.") from e
        except FileNotFoundError:
            raise FileNotFoundError("JSON file 'textos.json' not found.")
        except Exception as e:
            raise Exception(f"Unexpected error: {e}")