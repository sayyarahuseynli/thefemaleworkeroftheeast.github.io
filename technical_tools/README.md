## spaCy
 
>What is spaCy? 

spaCy is an industrial size natural language processing library. spaCy supports over 75 languages and contains trained models 84 trained pipelines for 25 languages. The ability of spaCy to process such a diverse set of languages, is what solidified by decision to use it for pre-precessing my data set. 

spaCy offers three pre-trained libraries to process documents in Russian language: [small, medium and large](https://spacy.io/models/ru). After running a few tests with the small and medium size models, and not getting good topics, I opted to use the large model. Since my corpus contains a significant amount of archaic words which may have been absent from the news articles all three models are trained on, even the large model failed to recognize some terms. Nevertheless, overall the results were satisfactory and discernible. 

Please be aware that I wasn't able to use any of the existing tutorials for processing Russian language with my own list of stopwords. However, these three tutorials were the building blocks which I used to design my own code. 

>Melanie Walsh - [Text Analysis: Russian](https://melaniewalsh.github.io/Intro-Cultural-Analytics/05-Text-Analysis/Multilingual/Russian/00-Russian.html)

>Sherman Centre for Digital Scholarship, [Topic Modeling with Python (Gensim & spaCy)](https://learn.scds.ca/text-analysis-3/lessons/tmpython.html#step4)

>Fares Sayah, [Mastering Text Analysis and Topic Modeling with spaCy and Gensim](https://medium.com/@sayahfares19/text-analysis-topic-modelling-with-spacy-gensim-4cd92ef06e06)
