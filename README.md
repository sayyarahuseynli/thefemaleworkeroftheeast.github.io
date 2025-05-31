# The Female Worker of the East
 
* [Primary source](https://github.com/sayyarahuseynli/workeroftheeast.github.io/tree/main/Primary%20source)
  
* [Technical tools](https://github.com/sayyarahuseynli/workeroftheeast.github.io/tree/main/Technical%20tools)


**About the primary source**

>About the project:

This Digital Humanities Certificate project is called The Female Worker of the East (trans. “Труженица Востока”). The project shares its title with the publication it is based on a short periodical published between 1927 – 1929. Each issue of consists of 30-50 pages, describing the livelihoods of women from thirty ethnic groups living across Soviet geography. The title signals to how Soviet ethnographers, who compiled the publication, conceptualized the idea of the “East”. At first glance, despite the size of the community, all are described in the same manner, namely backwards, especially the women.  Other similarities include the number of chapters, the same narrative structure, which starts with the overview of environment each community inhabits, followed by observations on the roles of women in the communities before and after the revolution. Lastly, all issues have the same circulation of 7000 copies, with prices ranging between 18-22 cents (kopeek). Considering such a limited scope and the language of the publication being Russian, it is reasonable to assume that the primary public for the print media were the educated elite, and institutional settings, such as libraries and universities. 

A closer look reveals new insights into these historical documents. Using spaCy, a natural language processing (NLP) software, I interrogate this publication to shed light on themes that are represented in the brochure but intentionally undermined. I ask the following **questions**: 

- What are the main topics that are shared among brochures?  

- How are the Muslim women, who make up forty five percent of the represented publication were described in comparison to their non-Muslim counterparts?  

- How useful is topic modeling to analyze a small corpus in Russian language? Overall, I argue that The Female Worker of the East, presents a complex perspective on Muslim women which needs a careful and close examination, which may be a difficult task for the NLP to synthesize. 


For the humanist analysis of the brochures I use an article published by Natalya Chernyaeva, who conducted an [analysis](https://www.academia.edu/102573955/Chernyaeva_Imagining_the_Soviet_East_Narratives_of_Popular_Ethnography_in_a_Series_of_Pamphlets_The_Female_Worker_of_the_East_1927_1929) of the textual and visual materials included in the publication. According to the Chernyaeva, the brochure was created "by ethnographers affiliated with the Scientific Association of Oriental Studies, the brochures used the language of description that drew both on Russian academic ethnography of the Imperial period and the Marxist ideological canonfile." Quote from this article. [Read more here](https://cyberleninka.ru/article/n/voobrazhaya-sovetskiy-vostok-narrativy-populyarnoy-etnografii-v-serii-broshyur-truzhenitsa-vostoka-1927-1929/viewer) the static and uncivilized perspective of the "other" within the Soviet Union positioned the reader, the Russian, as a civilized and modern. This approach supported the Soviet civilizing mission as well. However, the author does not criticize the content, which is why the current intervention is important. Using secondary literacy on specific communities, I will provide more accurate information about a particular group.    


![cover picture](cover_photo.jpg)

For the pre-preprocessing of the text, I undertook the below steps: 

- Extract the text from each brochure into a separate Google Docs file which I subsequently saved as a new txt file
- Lemmatize the text, which means to convert each word in the corpus to its infinitive form
- Identify an appropriate stop word list and add to the project folder
- Remove the stop words from the corpus
- Process the texts and review the visualizations
- Record the findings

I documented my process in details in this Google Sheet [file](https://docs.google.com/spreadsheets/d/1WJqD3pefQvqm_7P4_fsjvtYJ_cCSSoVbIeO1uvRs0uo/edit?gid=0#gid=0). 
  

**Method and its limitations**

**Lessons learned and Opportunities**

**Teaching resources**

In English:

[Russian Corpora](https://ruscorpora.ru/en) 

[Topic Modeling Russian History](https://link.springer.com/chapter/10.1007/978-3-030-42855-6_24#Sec9)

[Meet the Method: Computational Text Analysis](https://cssh.northeastern.edu/nulab/meet-the-method-computational-text-analysis/)  

In Russian:

Chernyaeva N. Imagining the Soviet East: Narratives of Popular Ethnography in a Series of Pamphlets, The Female Worker of the East, 1927–1929. Etnografia. 2022. 3 (17): 149–178. (In Russ.). doi 10.31250/2618-8600-2022-3 (17)-149-178 



