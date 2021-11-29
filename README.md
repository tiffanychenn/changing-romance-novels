# changing-romance-novels
This project aims to subvert the expectations of heterosexual couples in romance novels by changing genders of main characters in famous romance novels (mostly from the Romantic era). By doing so, this project also comments on common romance novel tropes (e.g. the Byronic hero) and gender norms of the time.

There are a few changes:
- Changing the gender of the main love interest (in `/modified-love-interest-text`)
- Making all characters male or female (in `/modified-all-male-text` and `/modified-all-female-text`)
- Changing the gender of all characters in the story (in `/modified-all-genders-text`)
 
Texts modified:
- Anna Karenina, by Leo Tolstoy (replaced Vronsky)
- Emma, by Jane Austen (replaced Mr. Knightley)
- Jane Eyre, by Charlotte Bronte (replaced Mr. Rochester)
- Persuasion, by Jane Austen (replaced Mr. Wentworth)
- Pride and Prejudice, by Jane Austen (replaced Mr. Darcy)
- Sense and Sensibility, by Jane Austen (replaced Mr. Willoughby)
- Wuthering Heights, by Emily Bronte (replaced Catherine)

General bugs:
- I'm still unsure how to tackle when someone of the same gender is thinking of the love interest.
- em-dashes are regular dashes in the text files
- doesn't work well with passive tense (e.g. his name was Willoughby)
- mrs vs miss distinction when changing genders from mr 
- the way that names currently work is the text finds all names it can find in this names database I imported and check if a work is a name in that database. doesn't work well with foreign texts (e.g. Anna Karenina) so it would be good to do it through a database of character names? (but sadly that is very hard to find online because it is... a very niche necessity lol)
  - also currently some last names change but since they all change to the same last name i don't really think this is a bug

Future potential things to do:
- Romeo and Juliet

Thank you to Project Gutenberg for the text!