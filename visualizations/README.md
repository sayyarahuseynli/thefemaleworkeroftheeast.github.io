## About the visuals ##

The visuals included in the current folder contain the outputs of Topic Modeling generated using Python together with spaCy. The specific tool that made the visuals possible was [pyLDAvis](https://pypi.org/project/pyLDAvis/), the tool of Python library designed to create interactive visualizations.

## File naming convention ##

The generated file names follow the naming convention: topicVis + the number of topics portrayed in that visual + .html. If I changed any variables, such as the number of columns, and ran the topic model code without changing the file name, the file that was generated first would be overwritten. To preserve the results of my numerous experiments, I made sure to change the file name every time. I added an underscore (_) and the identified the number of topics applicable for that run, which is reflected at the end of the file name.

## How to view with the visuals? ## 
To view the file, navigate to the file in the Visualizations folder, select one of the HTML files, and click on it. You will see the raw file on your page, that's all right. Bring your cursor to the third button at the top right side of the page, which will be Download raw file. Having downloaded it on your device, open the file using your favorite browser and explore. See the image below: 


![downloadrawfile](downloadrawfile.jpg)

### Suggested interactions: ###

Please note: The circles represent topics while the sizes correlate with their commonality. The space between the circles shows the similarity of topics.

- Use the top left “Selected Topic” box to view topics clustered together. 
  * For example, in the 10-topic visual, only 6 topics are visible on the left chart, whereas topics 7-10 are clustered together under the number 10, formatted in bold. To view topic 8, type that number in the “Selected Topic” box, which makes the terms of that topic appear on the right side of the screen. 
- Use “Slide to adjust relevance metric:” to view terms within that topic from most common to least common.
  * 1.0 represents the most relevant terms in that topic
  * 0.0 represents the least relevant terms in that topic, ie. terms that may have appeared only in one or two documents
  * Within the least common topics less than 1 may not provide a result.
  
### If this is your first time engaging with this kind of visual, you might be interested in this section prior to using the interactive visual.
 	- While there is a legend on the bottom right of the visuals, some people may find it slightly confusing. Please note that the Red bar indicates the Estimated term frequency within the selected topic. Simply put, these terms are the most common within the topic of your choice. 
 	While the light blue bar, stands for the Overall term frequency, which means that those terms are common accross all topics in the corpus. 

* Disclaimer 2: I haven't found a way to embed the HTML files into GitHub. This is the reason I guide my readers to download the files on their computers to view them. Hopefully, this is a temporary solution. In the meantime, I appreciate your patience, my dear reader.

