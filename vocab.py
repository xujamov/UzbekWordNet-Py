from PyDictionary import PyDictionary
from vocabulary import Vocabulary as vb
import json


def translate(text):
    try:
        translation = ''
        result = json.loads(vb.translate(text, "en", "hi"))
        for res in result:
            translation += res['text'] + ','
        return translation[:-1] + '\n'
    except:
        return "N/A"


def synonyms(word):
    try:
        synonyms = ''
        result = json.loads(vb.synonym(word))
        for res in result:
            synonyms += res['text'] + ','
        return synonyms[:-1] + '\n'
    except:
        return "N/A"


def antonyms(word):
    try:
        result = vb.antonym(word)
        return ','.join(x for x in result['text']) + '\n'
    except:
        return "N/A"


def usage_example(word):
    try:
        examples = ''
        result = json.loads(vb.usage_example(word))
        for res in result:
            examples += res['text'] + '\n\n'
        if len < 300:
            return examples
        else:
            return examples[:300]
    except:
        return "N/A"


def meaning(word):
    try:
        parts = ''
        result = json.loads(vb.part_of_speech(word))
        for res in result:
            parts += res['text'] + ':' + res[u'example:'] + '\n\n'
        return parts
    except:
        return "N/A"


def pronounce(word):
    try:
        result = vb.pronunciation(word)
        return result[0]['raw'].encode('utf8') + '\n'
    except:
        return "N/A"


def create_result(word):
    result = {}
    result['meaning'] = meaning(word)
    result['pronunciation'] = pronounce(word)
    result['usage'] = usage_example(word)
    result['synonyms'] = synonyms(word)
    result['antonyms'] = antonyms(word)
    result['translation'] = translate(word)
    return result


def get_synonyms(word):
    try:
        dictionary = PyDictionary()
        return ",".join(x for x in dictionary.synonym(word))
    except:
        return "No synonyms available"


def get_antonyms(word):
    try:
        dictionary = PyDictionary()
        return ",".join(x for x in dictionary.antonym(word))
    except:
        return "No antonyms available"


def get_meaning(word):
    try:
        meaning = ''
        dictionary = PyDictionary()
        result = dictionary.meaning(word)
        forms = result.keys()
        for form in forms:
            meaning += 'As a ' + form + ': ' + result[form][0] + '\n'
        return meaning
    except:
        return "Word not found in dictionary."
