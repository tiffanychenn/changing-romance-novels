import string
import bisect
import json

male_to_female = {"he": "she", "him": "her", "his": "her", "himself": "herself", "boy": "girl", "man": "woman", "gentleman": "lady", "son": "daughter", "sons": "daughters", "he's": "she's", "he'll": "she'll", "husband": "wife"}
female_to_male = {y:x for x,y in male_to_female.items()}

male_to_female_prefix = {"Mr": "Mrs", "Count": "Countess"}
female_to_male_prefix = {y:x for x,y in male_to_female_prefix.items()}

with open("names.json", "r") as f:
    names_json = json.loads(f.read())
    male_names = sorted(names_json["men"])
    female_names = sorted(names_json["women"])

pride_and_prejudice = "pride-and-prejudice"
jane_eyre = "jane-eyre"
anna_karenina = "anna-karenina"
persuasion = "persuasion"
emma = "emma"
sense_and_sensibility = "sense-and-sensibility"
wuthering_heights = "wuthering-heights"

"""
Changes the gender for the main love interest (but also any character really)

Parameters:
- filename (required): string of the filename in original-text directory
- other_characters (required): set of other characters with the same gender as the character to change genders
- original_name (required): original character name to compare
- character_name (required): last name of character
- character_new_name (required): new last name of character
- male_to_female_bool (required): whether the gender is switching from male to female or from female to male
- character_other_names (optional, default = None): other names that the character goes by
- character_new_other_names (optional, default = None): new other names that the character goes by
- update_modified_text (optional, default = False): whether to take the original text or the modified text to then edit
"""
def change_gender(filename, other_characters, original_name, character_name, character_new_name, male_to_female_bool, character_other_names = None, character_new_other_names = None, update_modified_text = False):
    if update_modified_text:
        text_file = 'modified-love-interest-text/' + filename + '.txt'
    else:
        text_file = 'original-text/' + filename + '.txt'
    with open(text_file, 'r') as f:
        text = f.read()
        replaced_text = text.replace(character_name, character_new_name)
        replaced_text = replaced_text.replace(character_name.upper(), character_new_name.upper())
        if character_other_names and character_new_other_names and len(character_other_names) == len(character_new_other_names):
            for i in range(len(character_other_names)):
                replaced_text = replaced_text.replace(character_other_names[i], character_new_other_names[i])
                replaced_text = replaced_text.replace(character_other_names[i].upper(), character_new_other_names[i].upper())
        replaced_text = replaced_text.replace("“", "\"")
        replaced_text = replaced_text.replace("”", "\"")
        replaced_text = replaced_text.replace("’", "'")
        new_text = ""
        at_love_interest_no_dialogue = False
        at_love_interest_dialogue = False
        in_dialogue = False
        for paragraph in replaced_text.split("\n"):
            for word in paragraph.split(" "):
                new_word = word.replace("_", "")
                if len(new_word) > 0 and new_word[0] == "\"":
                    in_dialogue = True
                start_punc = ""
                end_punc = ""
                if len(new_word) > 0 and new_word[0] in string.punctuation:
                    start_punc = new_word[0]
                    new_word = new_word[1:]
                if len(new_word) > 1 and new_word[-1] in string.punctuation and new_word[-2] in string.punctuation:
                    end_punc = new_word[-2:]
                    new_word = new_word[:-2]
                elif len(new_word) > 0 and new_word[-1] in string.punctuation:
                    end_punc = new_word[-1]
                    new_word = new_word[:-1]
                if (at_love_interest_no_dialogue and not in_dialogue) or (at_love_interest_dialogue and in_dialogue) :
                    if male_to_female_bool and new_word.lower() in male_to_female:
                        new_gender_word = male_to_female[new_word.lower()]
                        if ord(new_word[0]) < 96:
                            new_word = chr(ord(new_gender_word[0]) - 32) + new_gender_word[1:]
                        else:
                            new_word = new_gender_word
                    elif not male_to_female_bool and new_word.lower() in female_to_male:
                        new_gender_word = female_to_male[new_word.lower()]
                        if ord(new_word[0]) < 96:
                            new_word = chr(ord(new_gender_word[0]) - 32) + new_gender_word[1:]
                        else:
                            new_word = new_gender_word
                if in_dialogue:
                    if original_name in new_word:
                        at_love_interest_dialogue = True
                    elif new_word.strip(string.punctuation) in other_characters:
                        at_love_interest_dialogue = False
                if not in_dialogue:
                    if original_name in new_word:
                        at_love_interest_no_dialogue = True
                    elif new_word.strip(string.punctuation) in other_characters:
                        at_love_interest_no_dialogue = False
                if len(end_punc) > 0 and end_punc[-1] == "\"":
                    in_dialogue = False
                new_text += start_punc + new_word + end_punc + " "
            new_text = new_text[:-1] + "\n"
        textfile = open("modified-love-interest-text/" + filename + '.txt', "w")
        textfile.write(new_text)
        
change_gender(pride_and_prejudice, set(["Bennet", "Bingley", "Wickham", "Collins", "Gardiner"]), "Darcy", "Mr. Darcy", "Miss Darcy", True, ["Mr. Fitzwilliam"], ["Miss Fiona"])
change_gender(jane_eyre, set(["Lloyd", "Brocklehurst", "Mason", "Leaven", "Rivers", "Oliver", "Reed"]), "Rochester", "Mr. Rochester", "Miss Rochester", True, ["Edward"], ["Edna"])
change_gender(anna_karenina, set(["Alexandrovitch", "Stiva", "Levin", "Sergey", "Philip", "Mihail", "Oblonsky", "Seryozha", "Arkadyevitch", "Stepan"]), "Vronsky", "Count Vronsky", "Countess Vronsky", True, ["Count Alexey Kirillovitch Vronsky", "Alexey Vronsky", "Count Alexey Kirillovitch", "Alexey Kirillovitch"], ["Countess Olesia Kirillovitcha Vronsky", "Olesia Vronsky", "Countess Olesia Kirillovitcha", "Olesia Kirillovitcha"])
change_gender(persuasion, set(["Elliot", "Musgrove", "Croft", "Benwick", "Harville"]), "Wentworth", "Mr Wentworth", "Miss Wentworth", True, ["Frederick"], ["Freya"])
change_gender(emma, set(["Churchill", "Martin", "Elton", "Weston", "Woodhouse", "John"]), "Knightley", "Mr. Knightley", "Miss Knightley", True)
change_gender(sense_and_sensibility, set(["Ferrars", "Brandon", "Dashwood", "Middleton", "Palmer", "Harris", "Pratt"]), "Willoughby", "Mr. Willoughby", "Miss Willoughby", True, ["John Willoughby"], ["Jane Willoughby"])
change_gender(wuthering_heights, set(["Nelly", "Cathy", "Isabella", "Frances", "Zillah"]), "Cade", "Catherine", "Cade", False)

"""
Changes all genders

Parameters:
- filename (required): string of the filename in original-text directory
- change_males (optional, default = True): boolean for whether to change male gender
- change_females (optional, default = True): boolean for whether to change female gender
- given_male_names (optional, default = None): set of male names in the text
- given_female_names (optional, default = None): set of female names in the text
"""
def change_genders(filename, change_males = True, change_females = True, given_male_names = None, given_female_names = None):
    if not change_males and not change_females:
        return
    text_file = 'original-text/' + filename + '.txt'
    with open(text_file, 'r') as f:
        text = f.read()
        new_text = ""
        for paragraph in text.split("\n"):
            for word in paragraph.split(" "):
                new_word = word.replace("_", "")
                start_punc = ""
                end_punc = ""
                if len(new_word) > 0 and new_word[0] in string.punctuation:
                    start_punc = new_word[0]
                    new_word = new_word[1:]
                if len(new_word) > 1 and new_word[-1] in string.punctuation and new_word[-2] in string.punctuation:
                    end_punc = new_word[-2:]
                    new_word = new_word[:-2]
                elif len(new_word) > 0 and new_word[-1] in string.punctuation:
                    end_punc = new_word[-1]
                    new_word = new_word[:-1]
                if change_females and new_word.lower() in female_to_male:
                    new_gender_word = female_to_male[new_word.lower()]
                    if ord(new_word[0]) < 96:
                        new_word = chr(ord(new_gender_word[0]) - 32) + new_gender_word[1:]
                    else:
                        new_word = new_gender_word
                elif change_males and new_word.lower() in male_to_female:
                    new_gender_word = male_to_female[new_word.lower()]
                    if ord(new_word[0]) < 96:
                        new_word = chr(ord(new_gender_word[0]) - 32) + new_gender_word[1:]
                    else:
                        new_word = new_gender_word
                elif change_females and new_word.lower() in female_to_male_prefix:
                    new_gender_word = female_to_male_prefix[new_word.lower()]
                    if ord(new_word[0]) < 96:
                        new_word = chr(ord(new_gender_word[0]) - 32) + new_gender_word[1:]
                    else:
                        new_word = new_gender_word
                elif change_males and new_word.lower() in male_to_female_prefix:
                    new_gender_word = male_to_female_prefix[new_word.lower()]
                    if ord(new_word[0]) < 96:
                        new_word = chr(ord(new_gender_word[0]) - 32) + new_gender_word[1:]
                    else:
                        new_word = new_gender_word
                new_text += start_punc + new_word + end_punc + " "
            new_text = new_text[:-1] + "\n"
        if change_males and given_male_names:
            for name in male_names:
                new_name = female_names[bisect.bisect_left(female_names)]
                new_text = new_text.replace(name, new_name)
                new_text = new_text.replace(name.upper(), new_name.upper())
        if change_females and given_female_names:
            for name in female_names:
                new_name = male_names[bisect.bisect_left(male_names)]
                new_text = new_text.replace(name, new_name)
                new_text = new_text.replace(name.upper(), new_name.upper())
        if change_males and change_females:
            textfile = open("modified-all-genders-text/" + filename + '.txt', "w")
        elif change_males:
            textfile = open("modified-all-male-text/" + filename + '.txt', "w")
        else:
            textfile = open("modified-all-female-text/" + filename + '.txt', "w")
        textfile.write(new_text)

change_genders(pride_and_prejudice)
change_genders(jane_eyre)
change_genders(anna_karenina)
change_genders(persuasion)
change_genders(emma)
change_genders(sense_and_sensibility)
change_genders(wuthering_heights)

# only change males
change_genders(pride_and_prejudice, change_females=False)
change_genders(jane_eyre, change_females=False)
change_genders(anna_karenina, change_females=False)
change_genders(persuasion, change_females=False)
change_genders(emma, change_females=False)
change_genders(sense_and_sensibility, change_females=False)
change_genders(wuthering_heights, change_females=False)

# only change females
change_genders(pride_and_prejudice, change_males=False)
change_genders(jane_eyre, change_males=False)
change_genders(anna_karenina, change_males=False)
change_genders(persuasion, change_males=False)
change_genders(emma, change_males=False)
change_genders(sense_and_sensibility, change_males=False)
change_genders(wuthering_heights, change_males=False)