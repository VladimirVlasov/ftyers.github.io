code can be seen in "practical 1" folder
## Spacy and NLTK comprassion
(some examples are from same code, but before I stated random seed)

Looking on this difference we can see that spacy works better with sentenses with '!' and 'i.e.' in the middle, like:

- On 23 April 2009, Depeche Mode performed for the television program "Jimmy Kimmel Live!" at the famed corner of Hollywood Boulevard and Vine Street, drawing more than 12,000 fans, which was the largest audience the program had seen since its 2003 premiere, with a performance by Coldplay.
- Antianginal: Herodotus (484 c BC–425 c BC) attests that the Gandarian mercenaries (i.e. "Gandharans/Kambojans" of Gandari Strapy of Achaemenids) from the 20th strapy of the Achaemenids were recruited in the army of emperor Xerxes

But fails with roman numbers (in the same sentence!):

- Antianginal: Herodotus (484 c BC–425 c BC) attests that the Gandarian mercenaries (i.e. "Gandharans/Kambojans" of Gandari Strapy of Achaemenids) from the 20th strapy of the Achaemenids were recruited in the army of emperor Xerxes I (486-465 BC), which he led against the Hellas.

Also spacy failed to separate: "Two examples of miscellaneous pronunciations which contrast with both standard American and British usages are "data", which may be pronounced with ("dah") instead of ("day"); and "maroon", pronounced with ("own") as opposed to ("oon").\nEffervescents.\nPolitics." and "On 23 April 2009, Depeche Mode performed for the television program "Jimmy Kimmel Live!" at the famed corner of Hollywood Boulevard and Vine Street, drawing more than 12,000 fans, which was the largest audience the program had seen since its 2003 premiere, with a performance by Coldplay.
History."

Nltk fails with 'No.' abbreviation:

- The album only reached No. 12 on the "Billboard" Top Country Albums chart, Brooks' first song in three years to fail to make the top 10.
- Nonetheless, "We Shall Be Free" peaked at No. 22 on the "Billboard" Christian Songs charts through a marketing deal with Rick Hendrix Company, and earned Brooks a 1993 GLAAD Media Award.

Also nltk has problems with initials like in:

- On that list, Wright was listed along with many of the USA's other greatest architects including Eero Saarinen, I.M. Pei, Louis Kahn, Philip Johnson, and Ludwig Mies van der Rohe; he was the only architect who had more than one building on the list.

Spacy has broblems with clauses like in:

## Maxmatch tokenization

Maxmatch tokenization was made by indexed vocaburary in jupyter notebook file. BLEU metric was applyed to tokenized sentences from train and test sets.

How we can see that bleu score of maxmatch algorithm is better on train set than on test test (0.65 vs 0.48).
This can be connected with lack of dictionary in second case.
- I have hardly anything in common with myself and should stand very quietly in a corner, content that I can breathe".
- Discourse 5 of that work, "Knowledge Its Own End", is a recent statement of a Christian educational perennialism.

Both nltk and spacy has problems with ':\n' sequence, but in different sentences.
