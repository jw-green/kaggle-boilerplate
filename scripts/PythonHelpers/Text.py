import string
import unicodedata
import re

def remove_non_ascii(str):
    """
    Remove any non-ascii characters to prevent errors
    """

    return ''.join(filter(lambda x: x in string.printable, str))

def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', str(text)).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def remove_special_chars(text, remove_digits=False):
    text = re.sub('\\t', ' ', text)
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text