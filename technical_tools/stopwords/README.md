## spaCy
 
>What is spaCy? 

spaCy is an industrial size natural language processing library. spaCy supports over 75 languages and contains trained models 84 trained pipelines for 25 languages. The ability of spaCy to process such a diverse set of languages, is what solidified by decision to use it for pre-precessing my data set. 

spaCy offers three pre-trained pipelines to process datasets in Russian language: [small, medium and large](https://spacy.io/models/ru). The pre-processing that requires these pipelines is lemmatization, which is essential in order to avoid the occurrence of different inflections of the same word. This essential step is crucial for working with highly inflected languages such as the Russian language. After running a few lemmatization tests with the small and medium size pipelines, and not getting sufficient result, I opted to use the large model. Since my corpus contains a significant amount of archaic words which may have been absent from the news articles all three models are trained on, even the large model failed to recognize some terms. Nevertheless, overall the results were satisfactory and discernible. 

Please be aware that I wasn't able to use any of the existing tutorials for processing Russian language with my own list of stopwords. However, these three tutorials were the building blocks which I used to design my own code. 

>Melanie Walsh - [Text Analysis: Russian](https://melaniewalsh.github.io/Intro-Cultural-Analytics/05-Text-Analysis/Multilingual/Russian/00-Russian.html)

>Sherman Centre for Digital Scholarship, [Topic Modeling with Python (Gensim & spaCy)](https://learn.scds.ca/text-analysis-3/lessons/tmpython.html#step4)

>Fares Sayah, [Mastering Text Analysis and Topic Modeling with spaCy and Gensim](https://medium.com/@sayahfares19/text-analysis-topic-modelling-with-spacy-gensim-4cd92ef06e06)

You can read more information about the different stages of the process in this [Google doc](https://docs.google.com/document/d/1U5P1JX93KRGIx_zXjibidHvNtTbw0pd_NUh8-X43qmY/edit?tab=t.0)
