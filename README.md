# changing-romance-novels
This project aims to subvert the gender and heterosexual expectations in romance novels by changing genders of main characters in famous romance novels (mostly from the Romantic era). By doing so, this project also comments on common romance novel tropes (e.g. the Byronic hero) and gender norms of the time.

My short bio is above (and also can be found in `BIO.md`). My poetics can be found in `POETICS.md`. This README acts as a hub for documentation, since this project is very technical.

There are a few changes:
- Changing the gender of the main love interest (in `/modified-love-interest-text`)
- Making all characters male or female (in `/modified-all-male-text` and `/modified-all-female-text`)
- Changing the gender of all characters in the story (in `/modified-all-genders-text`)
- Making everyone nonbinary (in `/modified-nonbinary-text`)
 
Texts modified:
- _Anna Karenina_, by Leo Tolstoy (replaced Vronsky)
- _Emma_, by Jane Austen (replaced Mr. Knightley)
- _Jane Eyre_, by Charlotte Bronte (replaced Mr. Rochester)
- _Persuasion_, by Jane Austen (replaced Mr. Wentworth)
- _Pride and Prejudice_, by Jane Austen (replaced Mr. Darcy)
- _Romeo and Juliet_, by William Shakespeare (replaced Juliet)
- _Sense and Sensibility_, by Jane Austen (replaced Mr. Willoughby)
- _Wuthering Heights_, by Emily Bronte (replaced Catherine)

Note that all implementation started with me modifying _Pride and Prejudice_, so it is likely that the changes there are the strongest.

Found bugs:
- I'm still unsure how to tackle when someone of the same gender is thinking of the love interest.
- em-dashes are taken out in the new file and replaced with spaces because the em-dash is not in ascii
- doesn't work well with passive voice (e.g. his name was Willoughby)
- mrs vs miss distinction when changing genders from mr 
- the way that names currently work is the text finds all names it can find in this names database I imported and check if a work is a name in that database, if a set of names is not passed into the function. doesn't work well with foreign texts (e.g. Anna Karenina) so it would be good to do it through a database of character names? (but sadly that is very hard to find online because it is... a very niche necessity lol)
- nicknames are very hard to do with the current way that my project is parsing names.
- her can correspond to his and him
- also currently only supplied sets of names when the character list was relatively short, so the name changes for these titles when changing genders are probably better

Resources:
- Project Gutenberg, for the stories
- https://github.com/aruljohn/popular-baby-names, for the names
- https://www.reddit.com/r/traaaaaaannnnnnnnnns/comments/ep7hhv/gender_netreul_words/, for ideas of gender neutral titles of power
- Wikipedia, for figuring out lists of character names for some of these works