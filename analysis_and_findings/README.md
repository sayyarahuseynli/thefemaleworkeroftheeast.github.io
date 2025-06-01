# The Female Worker of the East

## Context on the analysis ##

To Frame the analysis and subsequent findings of the current project I relied on the key approaches in the [Topic Modeling Martha Ballard's Diary](https://cblevins.github.io/posts/topic-modeling-martha-ballards-diary/) project by Cameron Blevins, and discussion points from the article "ВООБРАЖАЯ СОВЕТСКИЙ ВОСТОК: НАРРАТИВЫ ПОПУЛЯРНОЙ ЭТНОГРАФИИ В СЕРИИ БРОШЮР «ТРУЖЕНИЦА ВОСТОКА», 1927-1929" [Imagining the Narratives of the Soviet East: Popular Ethnography in the Female Worker of the East brochure series](https://journal.kunstkamera.ru/archive/2024_nomer_2_24/chernyaeva_n_a_povtornoe_ispolzovanie_etnograficheskoj_fotografii_i_rezhimy_vizualizacii_etnichnosti_na_primere_fotografii_iz_ko) by Natalya Anatolyevna Chernyaeva (Наталья Анатольевна Черняева). 

Blevins inspired me to construct the following questions:

- What are the possible advantages of using topic modeling with a small corpus?
- What are the common topics? 
- To what extent did I expect this topic to appear in the model and why?
- What did I expect to see and didn't see? 

My discovery of Chernyaeva's article fulfilled two purposes for me, first it validated my initial assumptions about the publication, and secondly, it showed me an interesting research gap, I could address with the current project. When I first encountered "The Female Worker of The East", I was surprised by how a publication which contained such demeaning and derogatory language about people could be allowed for print. However, as a novice scholar, I doubted by judgment. This feeling disappeared after encountering Chernyaeva's article, who had noted that: 

>"The brochures activated an apparatus of cultural hegemony, contributing to identification of the reader with the civilized and the representatives of other nations backwardness."[^1] 

Natalya Chernyaeva is the author of a 2022 article the focus of which is the present a detailed visual analysis of the brochures. In the article, Chernyaeva skillfully presents the information on the historical background, the authors and motivations behind the publication. The analysis of the visual components, including each unique cover and subsequent internal drawings and photographers, are fascinating to read, so I recommend reading the full article [Read more here](https://cyberleninka.ru/article/n/voobrazhaya-sovetskiy-vostok-narrativy-populyarnoy-etnografii-v-serii-broshyur-truzhenitsa-vostoka-1927-1929/viewer). Please note that the article is in Russian language. 

Secondly, this Chernyaeva's article helped me notice a research gap. I realized that within the analysis of the brochures, the author did not criticize the content, especially when the descriptions associated with the life and traditions of the Muslim women. For this reason, I pose the following questions:

- How are the Muslim women, who represent 13 out of 30 ethnic groups accounted for in the brochures, are described in comparison to their non-Muslim counterparts? How does the topic modeling demonstrate these discrepancies? 
- Are there any discrepancies that came up in the topic modeling outputs?

[^1]: Chernyaeva, N. Imagining the Narratives of the Soviet East: Narratives of Popular Ethnography in a Series of Pamphlets series, The Female Worker of the East, 1927-1929. Etnografia. 2022. 3(17): 149-178: 149-178. 164-165.

## Analysis ##

One of the most important decisions that needs to be made before conducting a topic modeling analysis is to decide an optimal number of topics. Most researchers suggest experimenting with different numbers to evaluate the quality of topic outputs. On one hand, analyzing larger data sets with a low number of topics can result in topics that are too general, missing out on the granularity of the data. On the other hand, using too many topics will generate outputs with topics that are too rare and non-representative. 

For the current analysis, I experimented with 10, 30, 50 and 100 topics. The outputs generated using 10 and 30 topics were more interesting than those of 50 and 100. For this reason, the below analysis will include excerpts from using 10 and 30 topics. 