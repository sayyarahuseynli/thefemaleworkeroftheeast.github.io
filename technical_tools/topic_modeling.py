#import libraries 
import spacy
from spacy import displacy

# Import external libraries: gensim to create models and do some additional preprocessing
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# Import external libraries: pyLDA for vis
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis

import os

#set up filepaths, source files
import ru_core_news_lg
nlp = ru_core_news_lg.load()

stopwordsfile = 'ru.txt'
outname = 'topicmodel.csv'

# Open and read text my list of stopwords
stopwords = open(stopwordsfile, encoding='utf-8').read()
stopwords_list = stopwords.splitlines()

#add the my stopwords to spaCy's list

for stopword in stopwords_list:

    word = nlp.vocab[stopword]

    word.is_stop = True

# Define a function to remove stop words from a sentence 
def remove_stop_words(sentence): 
  # Parse the sentence using spaCy 
  doc = nlp(sentence) 
  
  # Use a list comprehension to remove stop words 
  filtered_tokens = [token for token in doc if not token.is_stop] 
  
  # Join the filtered tokens back into a sentence 
  return ' '.join([token.text for token in filtered_tokens])

# Preprocess texts for gensim
def gen_words(texts): # create a function called gen_words that runs on a list

    final = [] # Create an empty list to hold tokens
    for text in texts:
        new = gensim.utils.simple_preprocess(text, deacc = False) 
        # If working with languages that employ accents, you can set deacc to False
        final.append(new)
    return (final)

# Load all texts to a list
# Use OS to get a list of every file in the folder

folder_path = "lemmatized_files"
# Make an empty list for the corpus
lemmatized_texts = []

for filename in os.listdir(folder_path): # For every file in the specified folder
    file_path = os.path.join(folder_path, filename) 
    if os.path.isfile(file_path): # Check if it's a file
        # Print file name for debugging (display)
        print(f"Processing file: {filename}")
        
        # Open and read the file into a variable text
        text = open(file_path, encoding='utf-8').read()
        filtered_text = remove_stop_words(text)
        # Append that text varible to corpus emply list
        lemmatized_texts.append(filtered_text)

data_words = gen_words(lemmatized_texts) # Pass lemmatized_texts from previous step through the gen_words function

# Combine bigrams and trigrams
bigram_phrases = gensim.models.Phrases(data_words, min_count=3, threshold=50)
trigram_phrases = gensim.models.Phrases(bigram_phrases[data_words], threshold=50)

bigram = gensim.models.phrases.Phraser(bigram_phrases)
trigram = gensim.models.phrases.Phraser(trigram_phrases)

def make_bigrams(texts):
    return [bigram[doc] for doc in texts]

def make_trigrams(texts):
    return [trigram[bigram[doc]] for doc in texts]

data_bigrams = make_bigrams(data_words)
data_bigrams_trigrams = make_trigrams(data_bigrams)

# --Uncomment to print list of words showing bigrams and trigrams
# print (data_bigrams_trigrams[0])

# Create dictionary of all words in texts
id2word = corpora.Dictionary(data_bigrams_trigrams)

# Represent dictionary words as tuples (index, frequency)
corpus = []
for text in data_bigrams_trigrams:
    new = id2word.doc2bow(text)
    corpus.append(new)

# Specify number of topics (clusters of words)

num_topics = 100   # Experiment with more and fewer numbers of topics, comparing results

# Create LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                            id2word=id2word,
                                            num_topics=num_topics,
                                            random_state=100,
                                            update_every=1,
                                            chunksize=100,     
                                            # Change chunksize to increase or decrease the length of segments
                                            passes=50,         
                                            # Can do more passes but will increase the time it takes the block to run
                                            alpha="auto")

# Print topics
print(lda_model.show_topics())

# Output visualization
vis_data = gensimvis.prepare(lda_model, corpus, id2word, R=15, mds='mmds')
vis_data
pyLDAvis.display(vis_data)
pyLDAvis.save_html(vis_data, './topicVis' + str(num_topics) + '.html')





