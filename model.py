import re
from nltk.corpus import stopwords

def regex_cleaner(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r"@\S+"," ", text) 
    text = re.sub(r"http\S+", " ", text) 
    text = re.sub(r"www\S+"," ", text) 
    text = re.sub(r"^rt ", "", text) 
    text = re.sub(r"[^A-Za-zäüö]", " ", text)
    return text

def stopword_matcher(processed_text):
    lang_matches = {}
    languages = ["english", "french", "russian", "dutch","italian", "german", "spanish","swedish","norwegian"]
    for language in stopwords.fileids():
        lang_matches[language] = 0
        for stopword in stopwords.words(language):
            matches = len(re.findall(r"(^| )"+stopword+"( |$)",processed_text))
            lang_matches[language] = lang_matches[language]+matches
    return lang_matches

def estimate_language(stopword_dict):
    if max(stopword_dict.values()) == 0:
        return "english"
    else:
        return max(stopword_dict,key=stopword_dict.get)

def language(processed_text):
    language_dict = stopword_matcher(processed_text)
    return estimate_language(language_dict)

def language_by_set(processed_text):
    splits = processed_text.split(" ")
    splits = set(splits)
    lang_matches = {}
    languages = ["english", "french", "russian", "dutch",
                "italian", "german", "spanish", "swedish","norwegian"]
    for language in languages:
        words = set(stopwords.words(language))        
        lang_matches[language] = len(words.intersection(splits))
    if max(lang_matches.values()) == 0:
        return "english"
    else:
        return max(lang_matches,key=lang_matches.get)

