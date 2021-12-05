import string
import bisect
import json
from helper import *

male_to_female = {"he": "she", "him": "her", "his": "her", "himself": "herself", "boy": "girl", "man": "woman", "son": "daughter", "lad": "lass", "he's": "she's", "he'll": "she'll", "husband": "wife"}
female_to_male = {y:x for x,y in male_to_female.items()}

male_to_female_prefix = {"Mr": "Miss", "Sir": "Madam", "Count": "Countess", "Prince": "Princess", "King": "Queen", "Duke": "Duchess", "Lord": "Lady", "Baron":"Baroness"}
female_to_male_prefix = {y:x for x,y in male_to_female_prefix.items()}
female_to_male_prefix["Mrs"] = "Mr"

other_male_to_female = {"brother": "sister", "brothers": "sisters", "sons": "daughters", "boys": "girls", "men": "women", "gentlemen": "ladies", "gentleman": "lady"}
other_female_to_male =  {y:x for x,y in other_male_to_female.items()}

gendered_to_nonbinary = {"brother": "sibling", "sister": "sibling", "brothers": "siblings", "sisters": "siblings", "sons": "children", "daughters": "children", "boys": "children", "girls":"children", "men": "people", "women": "people", "gentlemen": "people", "ladies": "people", "he": "they", "she": "they", "him": "them", "her": "them", "his": "their", "himself": "themself", "herself": "themself", "boy": "child", "girl": "child", "man": "person", "woman": "person", "gentleman": "person", "lady": "person", "son": "child", "daughter": "child", "lad": "child", "lass": "child", "he's": "they're", "she's": "they're", "he'll": "they'll", "she'll": "they'll", "husband": "partner", "wife": "partner"}
gendered_to_nonbinary_prefix = {"Mr": "Mx", "Miss": "Mx", "Mrs": "Mx", "Count": "Earl", "Countess": "Earl", "Prince": "Heir", "Princess": "Heir", "King": "Monarch", "Queen": "Monarch", "Duke": "Jarl", "Duchess": "Jarl", "Lord": "Noble", "Lady": "Noble", "Baron": "Chief", "Baroness" : "Chief", "Sir": "Person", "Madam": "Person"}

with open("names.json", "r") as f:
    names_json = json.loads(f.read())
    male_names_list = sorted(names_json["boys"])
    female_names_list = sorted(names_json["girls"])
    male_names_set = set(names_json["boys"])
    female_names_set = set(names_json["girls"])

pride_and_prejudice = "pride-and-prejudice"
jane_eyre = "jane-eyre"
anna_karenina = "anna-karenina"
persuasion = "persuasion"
emma = "emma"
sense_and_sensibility = "sense-and-sensibility"
wuthering_heights = "wuthering-heights"
romeo_and_juliet = "romeo-and-juliet"

"""
Changes the gender for the main love interest (but also any character really)

Parameters:
- filename (required): string of the filename in original-text directory
- other_characters (required): set of other characters with the same gender as the character to change genders
- original_name (required): original character name to compare
- character_name (required): last name of character
- character_new_name (required): new last name of character
- male_to_female_bool (required): whether the gender is switching from male to female or from female to male
- play_bool (required): whether the text modified is a play
- character_other_names (optional, default = None): other names that the character goes by
- character_new_other_names (optional, default = None): new other names that the character goes by
"""
def change_gender(filename, other_characters, original_name, character_name, character_new_name, male_to_female_bool, play_bool, character_other_names = None, character_new_other_names = None):
    text_file = 'original-text/' + filename + '.txt'
    with open(text_file, 'r') as f:
        text = f.read()
        replaced_text = text.replace(character_name, character_new_name)
        replaced_text = replaced_text.replace(character_name.upper(), character_new_name.upper())
        if character_other_names and character_new_other_names and len(character_other_names) == len(character_new_other_names):
            for i in range(len(character_other_names)):
                replaced_text = replaced_text.replace(character_other_names[i], character_new_other_names[i])
                replaced_text = replaced_text.replace(character_other_names[i].upper(), character_new_other_names[i].upper())
        replaced_text = clean_up_text(replaced_text)
        new_text = ""
        at_love_interest_no_dialogue = False
        at_love_interest_dialogue = False
        in_dialogue = False
        for paragraph in replaced_text.split("\n"):
            for word in paragraph.split(" "):
                new_word = word.replace("_", "")
                if len(new_word) > 0 and new_word[0] == "\"":
                    in_dialogue = True
                start_punc, new_word, end_punc = get_word_separation(word)
                if (at_love_interest_no_dialogue and not in_dialogue) or (at_love_interest_dialogue and in_dialogue):
                    if male_to_female_bool and new_word.lower() in male_to_female:
                        new_word = get_new_word(new_word, male_to_female)
                    elif not male_to_female_bool and new_word.lower() in female_to_male:
                        new_word = get_new_word(new_word, female_to_male)
                if in_dialogue:
                    if original_name in new_word:
                        at_love_interest_dialogue = True
                    elif new_word.strip(string.punctuation) in other_characters:
                        at_love_interest_dialogue = False
                if not in_dialogue:
                    if original_name in new_word and (not play_bool or (play_bool and ord(new_word[1]) >= 96)):
                        at_love_interest_no_dialogue = True
                    elif new_word.strip(string.punctuation) in other_characters:
                        at_love_interest_no_dialogue = False
                if len(end_punc) > 0 and end_punc[-1] == "\"":
                    in_dialogue = False
                new_text += start_punc + new_word + end_punc + " "
            new_text = new_text[:-1] + "\n"
        textfile = open("modified-love-interest-text/" + filename + '.txt', "w")
        textfile.write(new_text)
        
change_gender(pride_and_prejudice, set(["Bennet", "Bingley", "Wickham", "Collins", "Gardiner"]), "Darcy", "Mr. Darcy", "Miss Darcy", True, False, ["Mr. Fitzwilliam"], ["Miss Fiona"])
change_gender(jane_eyre, set(["Lloyd", "Brocklehurst", "Mason", "Leaven", "Rivers", "Oliver", "Reed"]), "Rochester", "Mr. Rochester", "Miss Rochester", True, False, ["Edward"], ["Edna"])
change_gender(anna_karenina, set(["Alexandrovitch", "Stiva", "Levin", "Sergey", "Philip", "Mihail", "Oblonsky", "Seryozha", "Arkadyevitch", "Stepan"]), "Vronsky", "Count Vronsky", "Countess Vronsky", True, False, ["Count Alexey Kirillovitch Vronsky", "Alexey Vronsky", "Count Alexey Kirillovitch", "Alexey Kirillovitch"], ["Countess Olesia Kirillovitcha Vronsky", "Olesia Vronsky", "Countess Olesia Kirillovitcha", "Olesia Kirillovitcha"])
change_gender(persuasion, set(["Elliot", "Musgrove", "Croft", "Benwick", "Harville"]), "Wentworth", "Mr Wentworth", "Miss Wentworth", True, False, ["Frederick"], ["Freya"])
change_gender(emma, set(["Churchill", "Martin", "Elton", "Weston", "Woodhouse", "John"]), "Knightley", "Mr. Knightley", "Miss Knightley", True, False)
change_gender(sense_and_sensibility, set(["Ferrars", "Brandon", "Dashwood", "Middleton", "Palmer", "Harris", "Pratt"]), "Willoughby", "Mr. Willoughby", "Miss Willoughby", True, False, ["John Willoughby"], ["Jane Willoughby"])
change_gender(wuthering_heights, set(["Nelly", "Cathy", "Isabella", "Frances", "Zillah"]), "Charles", "Catherine", "Charles", False, False)
change_gender(romeo_and_juliet, set(["Rosaline", "Lady", "Nurse"]), "Julius", "Juliet", "Julius", False, True)

"""
Changes all genders

Parameters:
- filename (required): string of the filename in original-text directory
- change_males (optional, default = True): boolean for whether to change male gender
- change_females (optional, default = True): boolean for whether to change female gender
- male_character_names (optional, default = None): set of male character names in original text to replace. if specified, overrides check if the name is in the names database.
- female_character_names (optional, default = None): set of female character names in original text to replace. if specified, overrides check if the name is in the names database.
"""
def change_genders(filename, change_males = True, change_females = True, male_character_names=None, female_character_names=None):
    if not change_males and not change_females:
        return
    text_file = 'original-text/' + filename + '.txt'
    with open(text_file, 'r') as f:
        text = clean_up_text(f.read())
        new_text = ""
        name_changes = {}
        for paragraph in text.split("\n"):
            for word in paragraph.split(" "):
                start_punc, new_word, end_punc = get_word_separation(word)
                if change_females and new_word.lower() in female_to_male:
                    new_word = get_new_word(new_word, female_to_male)
                elif change_males and new_word.lower() in male_to_female:
                    new_word = get_new_word(new_word, male_to_female)
                elif change_females and new_word.lower() in other_female_to_male:
                    new_word = get_new_word(new_word, other_female_to_male)
                elif change_males and new_word.lower() in other_male_to_female:
                    new_word = get_new_word(new_word, other_male_to_female)
                elif change_females and new_word in female_to_male_prefix:
                    new_word = female_to_male_prefix[new_word]
                elif change_males and new_word in male_to_female_prefix:
                    new_word = male_to_female_prefix[new_word]
                elif change_males and len(new_word) > 0 and new_word not in name_changes and ((male_character_names is not None and (new_word in male_character_names or new_word[0] + new_word[1:].lower() in male_character_names)) or (male_character_names is None and (new_word in male_names_set or new_word[0] + new_word[1:].lower() in male_names_set))):
                    new_name = female_names_list[bisect.bisect_left(female_names_list, new_word)]
                    name_changes[new_word.upper()] = new_name.upper()
                    name_changes[new_word[0] + new_word[1:].lower()] = new_name
                elif change_females and len(new_word) > 0 and new_word not in name_changes and ((female_character_names is not None and (new_word in female_character_names or new_word[0] + new_word[1:].lower() in female_character_names)) or (female_character_names is None and (new_word in female_names_set or new_word[0] + new_word[1:].lower() in female_names_set))):
                    new_name = male_names_list[bisect.bisect_left(male_names_list, new_word)]
                    name_changes[new_word.upper()] = new_name.upper()
                    name_changes[new_word[0] + new_word[1:].lower()] = new_name
                new_text += start_punc + new_word + end_punc + " "
            new_text = new_text[:-1] + "\n"
        for name in name_changes:
            new_text = new_text.replace(name, name_changes[name])
        if change_males and change_females:
            textfile = open("modified-all-genders-text/" + filename + '.txt', "w")
        elif change_females:
            textfile = open("modified-all-male-text/" + filename + '.txt', "w")
        else:
            textfile = open("modified-all-female-text/" + filename + '.txt', "w")
        textfile.write(new_text)

change_genders(pride_and_prejudice, male_character_names=set(["Fitzwilliam", "Charles", "George", "William", "Edward"]), female_character_names=set(["Elizabeth", "Lizzy", "Eliza", "Jane", "Lydia", "Kitty", "Catherine", "Mary", "Caroline", "Georgiana", "Charlotte"]))
change_genders(jane_eyre)
change_genders(anna_karenina)
change_genders(persuasion)
change_genders(emma)
change_genders(sense_and_sensibility)
change_genders(wuthering_heights)
change_genders(romeo_and_juliet)

# only change males
change_genders(pride_and_prejudice, change_females=False, male_character_names=set(["Fitzwilliam", "Charles", "George", "William", "Edward"]), female_character_names=set(["Elizabeth", "Lizzy", "Eliza", "Jane", "Lydia", "Kitty", "Catherine", "Mary", "Caroline", "Georgiana", "Charlotte"]))
change_genders(jane_eyre, change_females=False)
change_genders(anna_karenina, change_females=False)
change_genders(persuasion, change_females=False)
change_genders(emma, change_females=False)
change_genders(sense_and_sensibility, change_females=False)
change_genders(wuthering_heights, change_females=False)
change_genders(romeo_and_juliet, change_females=False)

# only change females
change_genders(pride_and_prejudice, change_males=False, male_character_names=set(["Fitzwilliam", "Charles", "George", "William", "Edward"]), female_character_names=set(["Elizabeth", "Lizzy", "Eliza", "Jane", "Lydia", "Kitty", "Catherine", "Mary", "Caroline", "Georgiana", "Charlotte"]))
change_genders(jane_eyre, change_males=False)
change_genders(anna_karenina, change_males=False)
change_genders(persuasion, change_males=False)
change_genders(emma, change_males=False)
change_genders(sense_and_sensibility, change_males=False)
change_genders(wuthering_heights, change_males=False)
change_genders(romeo_and_juliet, change_males=False)

"""
Changes all genders to nonbinary

Parameters:
- filename (required): string of the filename in original-text directory
"""
def change_nonbinary(filename):
    text_file = 'original-text/' + filename + '.txt'
    with open(text_file, 'r') as f:
        text = clean_up_text(f.read())
        new_text = ""
        for paragraph in text.split("\n"):
            for word in paragraph.split(" "):
                start_punc, new_word, end_punc = get_word_separation(word)
                if new_word.lower() in gendered_to_nonbinary:
                    new_word = get_new_word(new_word, gendered_to_nonbinary)
                elif new_word in gendered_to_nonbinary_prefix:
                    new_word = gendered_to_nonbinary_prefix[new_word]
                new_text += start_punc + new_word + end_punc + " "
            new_text = new_text[:-1] + "\n"
        textfile = open("modified-nonbinary-text/" + filename + '.txt', "w")
        textfile.write(new_text)

change_nonbinary(pride_and_prejudice)
change_nonbinary(jane_eyre)
change_nonbinary(anna_karenina)
change_nonbinary(persuasion)
change_nonbinary(emma)
change_nonbinary(sense_and_sensibility)
change_nonbinary(wuthering_heights)
change_nonbinary(romeo_and_juliet)