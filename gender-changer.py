import string

other_male_characters = set(["Mr. Bennet", "Mr. Bingley", "Mr. Wickham", "Mr. Collins", "Mr. Gardiner"])
male_to_female = {"he": "she", "him": "her", "his": "hers", "himself": "herself", "He": "She", "Him": "Her", "His": "Her", "Himself": "Herself"}

with open('original-text/pride-and-prejudice.txt', 'r') as f:
    text = f.read()
    replaced_text = text.replace("Mr. Darcy", "Ms. Darcy")
    replaced_text = replaced_text.replace("Fitzwilliam", "Fiona")
    replaced_text = replaced_text.replace("“", "\"")
    replaced_text = replaced_text.replace("”", "\"")
    new_text = ""
    last_word = ""
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
            if at_darcy and new_word in male_to_female:
                new_word = male_to_female[new_word]
            if "Darcy" in word:
                at_darcy = True
            elif last_word == "Mr." and "Darcy" not in new_word:
                at_darcy = False
            new_text += new_word + punc + " "
        new_text = new_text[:-1] + "\n"
    textfile = open("modified-text/pride-and-prejudice.txt", "w")
    textfile.write(new_text)