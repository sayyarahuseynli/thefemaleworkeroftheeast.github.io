## About the visuals ##

The visuals included in the current folder contain the outputs of Topic Modeling with Python using spaCy and Gensim. The visualization aspect was possible with the help of pyLDAvis, which is the last action performed in the topic modeling code.

The first number present in the file name represents the number of topics portrayed in that visual. The reason for having two repeating numbers in the title, is to preserve the file in case if I ran the topic modeling with the same number of topic but switched other variables, such as the number of columns appearing on the right side of the visual. 

# Topic modeling analysis #

One of the most important decisions that needs to be made before conducting a topic modeling analysis is to decide an optimal number of topics. Most researchers suggest experimenting with different numbers to evaluate the quality of topic outputs. On one hand, analyzing larger data sets with a low number of topics can result it topics that are too general, missing out on the granularity of the data. On the other hand, using too many topics will generate outputs with topics too rare and non-representative. 

For the current analysis, I experimented with 10, 30, 50 and 100 topics. The outputs generated using 10 and 30 topics were more interesting than those of 50 and 100. For this reason, the below analysis, will include excerpts from using 10 and 30 topics. 

## How to interact with the visuals? ## 
All visuals included in the current folder are interactive. However, due to technical difficulty of embedding these visuals directly on GitHub, I opted to include static screen shots followed by URLs. By clicking the URLs, the user of the project can engage with the visual directly. 

### Actions for interactivity: ###

- Use “Slide to adjust relevance metric:” 1.0 is the most relevant words in each topic, 0.0 is least relevant, terms that may have appeared only in one or two documents
- Use the top left “Selected Topic” box to view topics clustered together. 
  * For example, in the 10-topic visual only 6 topics are visible on the left chart, 7-10 are clustered together under the number 10, formatted in bold. To view topic 8, type that number in the “Selected Topic” box, which makes the terms of that topic appear on the right side of the screen. 
- The circles represent topics while the sizes correlate with their commonality 
- The space between the circles show the similarity of topics



![10topic](10topicscreenshot)

