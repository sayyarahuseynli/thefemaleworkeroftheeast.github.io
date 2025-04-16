# The Female Worker of the East

* [Stopwords](https://github.com/sayyarahuseynli/workeroftheeast.github.io/tree/main/Stopwords)
 
* [Primary source](https://github.com/sayyarahuseynli/workeroftheeast.github.io/tree/main/Primary%20source)
  
* [Technical tools](https://github.com/sayyarahuseynli/workeroftheeast.github.io/tree/main/Technical%20tools)

About the project
“Ethnic Women in Soviet Space” is a project based on a publication showcasing women from thirty ethnic groups across Soviet Union. The information about these women was published in “Труженица Востока” ("Truzhenit︠s︡a Vostoka") brochure published between 1928-1920. Frustrated by one universal representation of all women as backwards, I embarked on this project to push back against this narrative. My special interest lies in investingating how Muslim women, who make up 50% of the communities covered in the publication, had much more social significance and agency than what is described in the source. I consider cultural production dominated by women, such as making textiles, household items and carpets, as evidence of social participation and personal agency.  

For the humanist analysis of the brochures I use an article published by Natalya Chernyaeva, who conducted an [analysis](https://www.academia.edu/102573955/Chernyaeva_Imagining_the_Soviet_East_Narratives_of_Popular_Ethnography_in_a_Series_of_Pamphlets_The_Female_Worker_of_the_East_1927_1929) of the textual and visual materials included in the publication. According to the Chernyaeva, the static and uncivilized perspective of the "other" within the Soviet Union positioned the reader, the Russian, as a civilized and modern. This approach supported the Soviet civilizing mission as well. However, the author does not criticize the content, which is why the current intervetion is important. Using secondary literaty on specific communities, I will provide more accurate information about a particular group.    


The digital humanities component of the project, which is the main focus, uses a [topic modeling](https://programminghistorian.org/en/lessons/topic-modeling-and-mallet#what-is-topic-modeling-and-for-whom-is-this-useful) to indentify cultural contributions of women to their respective societies, the information that is given litte attention and analysis in the brochure. The state support for the universal eradication of illeteracy, participation in the political and social lives amongst women is undeniable. However, it is also cricual to remember that the system's goal of emancipation, was directed at ensuring that women would contribute to the rapid industrilization process and propel the economic progress.     

![cover picture](Azerbaijani.jpg)

**Research questions**

- Diversify our understanding of Muslim women’s occupations in late Imperial Russian and early Soviet History by using topic modeling tool, Mallet
  
- Pose critical research questions based on the results generated through topic modeling
  
- Document the implementation process of working with Russian language in a topic modeling Mallet, especially the stopwords

**About the primary source**

>The Female Worker of the East,published in the USSR from 1927 to 1929, as an example of popular ethnography from this period, i.e., ethnographic knowledge communicated via non-specialized texts for a broad audience. Created by ethnographers affiliated with the Scientific Association of Oriental Studies, the pamphlets used the language of description that drew both on Russian academic ethnography of the Imperial period and the Marxist ideological canonfile. Quote from this article. [Read more here](https://cyberleninka.ru/article/n/voobrazhaya-sovetskiy-vostok-narrativy-populyarnoy-etnografii-v-serii-broshyur-truzhenitsa-vostoka-1927-1929/viewer) 

For the pre-preprocessing of the corpora, I extracted the text from each brochure into a seperate Google Docs file which I subsequently saved in txt format. I tracked this process in a Google Sheet [file](https://docs.google.com/spreadsheets/d/1WJqD3pefQvqm_7P4_fsjvtYJ_cCSSoVbIeO1uvRs0uo/edit?gid=0#gid=0). Another preparatory step was to split each file of the previously created files into sections of less than 1000 words, based on the context. This means that no sentences were split or deconstructed during the splitting process. You can see the splitting in this sample [file](https://docs.google.com/document/d/1tThhBmCiCsHAyF5pnhE9Sv-0Tci44ADkB0q_09MA4lQ/edit?tab=t.0) where the highlighted areas demonstrate where and at what word count I cut the text. The number next to parentheses corresponds with the numerically named subsection. Once the splitting was done, I saved each of the [sections](https://drive.google.com/drive/folders/1Hp3Uakgziklr1MQMSR1iq4sIr2kJy80s?usp=drive_link), originally Google Docs, as txt files. 

One contextual category embedded in the tracking file above is the religious diversity represented in the brochures. Over 50% of ethnic groups are Muslim, however, Christian, Shamanism, Confucianism, Paganism, and Laism are also made visible. As the brochures were constructed by ethnographers and anroropologists, the text also provide interesting desriptions of local traditions and beliefs.    

**Method and its limitations**

**Lessons learned and Opportunities**

**Teaching resources**

In Enligsh:

[Russian Corpora](https://ruscorpora.ru/en) 

[Topic Modeling Russian History](https://link.springer.com/chapter/10.1007/978-3-030-42855-6_24#Sec9)

[Meet the Method: Computational Text Analysis](https://cssh.northeastern.edu/nulab/meet-the-method-computational-text-analysis/)  

In Russian:


