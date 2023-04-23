# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:26:57 2023

@author: franc
"""

# Importing libraries
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

# Summary of the data
data.describe()

# Summary of the columns
data.info()

# Counting the number of articles per source
data.groupby(['source_id'])['article_id'].count()

# Summing the number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# Dropping a column
data = data.drop('engagement_comment_plugin_count', axis=1)

# Checking for missing values
data.isnull().sum()

# Creating keyword count by using def, for loop, and if statement

keyword = 'crash'
keyword_flag = []
for x in range (0,10):
    heading = data['title'][x]
    if keyword in heading:
       flag = 1
    else:
       flag = 0
    keyword_flag.append(flag) 

# Creating a function
def keywordflag(keyword):
    length = len(data)
    keyword_flag= []
    for x in range( 0, length):
        heading= data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

# Creating a keyword flag
keywordflag = keywordflag('murder')

# Creating a new column in data dataframe
data['keyword_flag'] = pd.Series(keywordflag)   

# SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# Adding a for loop to extract sentiment per title
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(neg)
    title_neu_sentiment.append(neg)
    
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

# Exporting the data
data.to_excel('blog_me_clean.xlsx', sheet_name='blogmedata', index=False)

