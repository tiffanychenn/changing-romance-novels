import string

other_male_characters = set(["Bennet", "Bingley", "Wickham", "Collins", "Gardiner"])
male_to_female = {"he": "she", "him": "her", "his": "her", "himself": "herself", "boy": "girl", "man": "woman", "gentleman": "lady"}

with open('original-text/pride-and-prejudice.txt', 'r') as f:
    text = f.read()
    replaced_text = text.replace("Mr. Darcy", "Ms. Darcy")
    replaced_text = replaced_text.replace("Mr. Fitzwilliam", "Ms. Fiona")
    replaced_text = replaced_text.replace("“", "\"")
    replaced_text = replaced_text.replace("”", "\"")
    new_text = ""
    at_darcy = False
    for paragraph in replaced_text.split("\n"):
        for word in paragraph.split(" "):
            new_word = word.strip("_")
            punc = ""
            if len(new_word) > 1 and new_word[-1] in string.punctuation and new_word[-2] in string.punctuation:
                punc = new_word[-2:]
                new_word = new_word[:-2]
            elif len(new_word) > 0 and new_word[-1] in string.punctuation:
                punc = new_word[-1]
                new_word = new_word[:-1]
            if at_darcy and new_word.lower() in male_to_female:
                female_word = male_to_female[new_word.lower()]
                if ord(new_word.strip(string.punctuation)[0]) < 96:
                    new_word = chr(ord(female_word[0]) - 32) + female_word[1:]
                else:
                    new_word = female_word
            if "Darcy" in new_word:
                at_darcy = True
            elif new_word.strip(string.punctuation) in other_male_characters:
                at_darcy = False
            new_text += new_word + punc + " "
        new_text = new_text[:-1] + "\n"
    textfile = open("modified-text/pride-and-prejudice.txt", "w")
    textfile.write(new_text)