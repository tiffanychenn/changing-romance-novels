import string

"""
Helper function to clean up text (i.e. make all characters ascii)

Parameters:
- text (required): text to clean up
"""
def clean_up_text(text):
    text = text.replace("“", "\"")
    text = text.replace("”", "\"")
    text = text.replace("’", "'")
    text = text.replace("—", " ")
    return text

"""
Helper function to get start_punc, word, and end_punc

Parameters:
- text (required): word to divide into start_punc, word, and end_punc
"""
def get_word_separation(word):
    start_punc = ""
    end_punc = ""
    new_word = word
    if len(new_word) > 1 and new_word[0] in string.punctuation and new_word[1] in string.punctuation:
        start_punc = new_word[:2]
        new_word = new_word[2:]
    elif len(new_word) > 0 and new_word[0] in string.punctuation:
        start_punc = new_word[0]
        new_word = new_word[1:]
    if len(new_word) > 2 and new_word[-1] in string.punctuation and new_word[-2] in string.punctuation and new_word[-3] in string.punctuation:
        end_punc = new_word[-3:]
        new_word = new_word[:-3]
    elif len(new_word) > 1 and new_word[-1] in string.punctuation and new_word[-2] in string.punctuation:
        end_punc = new_word[-2:]
        new_word = new_word[:-2]
    elif len(new_word) > 0 and new_word[-1] in string.punctuation:
        end_punc = new_word[-1]
        new_word = new_word[:-1]
    return start_punc, new_word, end_punc

"""
Helper function to get correct word mapping

Parameters:
- word (required): word to change
- mapping (required): 
"""
def get_new_word(word, mapping):
    new_word = mapping[word.lower()]
    if ord(word[0]) < 96:
        return chr(ord(new_word[0]) - 32) + new_word[1:]
    return new_word
