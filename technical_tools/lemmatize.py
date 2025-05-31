#import libraries 
import spacy

#set up filepaths, source files
import ru_core_news_lg
nlp = ru_core_news_lg.load()

filepath = 'text_files/cherkeshenka_simpletext.txt'

outname = filepath.replace('.txt', '-lemmatized.txt')

# Open and read text
text = open(filepath, encoding='utf-8').read()

# Process text with spaCy
document = nlp(text)

# Create a lemmatized version of the original text file
with open(outname, 'w', encoding='utf8') as out:
    for token in document:

        # Get the lemma for each token
        out.write(token.lemma_.lower())

        # Insert white space between each token
        out.write(' ')

