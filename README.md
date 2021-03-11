# Mad-Green
### Your CBD Advisor in Madrid
Ironhack final project
![](images/diapo_primera.jpg)

### Introduction:
The CBD market in Spain has come a long way until it has been finally legalised. As non toxic or addictive weed, it has a lot of benefits for both: medical and recreationnal reasons. The CBD market is currently growing at incredibly high levels. Yet, as CBD has had a lot of stigmatizations in the past, the demand is little to nothing informed about the potential, kinds and usages of CBD. 
As it has behavioral effects on the consumer, I felt the need to break this social fear/ignorance. Informing about the different effects different kinds of CBD have so as to give the freedom for users to explore the CBD world specific to their individual tastes/aims.  


### Goals:
For this reason, my aim in this project is to:

-recommend the user all the different kinds of CBD in function of the effect he/she wants to feel. 

-given this set of CBD buds, allow the user to compare and choose the most optimum kind of CBD in terms of price and CBD percentage containing in the product. Once chosen, return the user the shop-website

-create a community of CBD lovers in which they all share their reviews of a given CBD bud from a given shop recommended.

### Work done:
#### -Created a MongoDB with 4 collections: 

   -One containing CBD strains, effects and flavors. Which is a [Kaggle Dataset]("https://www.kaggle.com/kingburrito666/cannabis-strains")
    
   -Second one with the ratings of the CBD strains from that Kaggle Dataset as well.
    
   -Third collection was created by web-scrapping 2 spanish CBD online shops using **Selenium.**
   
   -Fourth collection was implement for the user to write reviews about the products recommended

#### Streamlit:
Rather than creating an API I wanted my data to be more visual

#### Deployed on Heroku:
Although the website has already been created, data is not showing as there are some problems which will get shortly fixed.

### Libraries Used:
[Pandas]("https://pandas.pydata.org/")
[Selenium]("https://selenium-python.readthedocs.io/")
[Streamlit]("https://streamlit.io/")
[Matplotlib]("https://matplotlib.org/stable/contents.html")
[os]("https://docs.python.org/3/library/os.html")
[Seaborn]("https://seaborn.pydata.org/")



### Future work:

-Fix deploying the app

-Do more web-scrapping

-Expand the CBD products selection (only buds at the moment)

-Create model to predict what CBD strain is the consumer more probably like given its past CBD choices

-Increment the community side of the platform



