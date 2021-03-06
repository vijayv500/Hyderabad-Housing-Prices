import pandas as pd 
import streamlit as st 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Find Out Builders In Your Locality: Hyderabad')

st.markdown("""
This app displays list of builders in your locality as word cloud.
* Select your locality from the dropdown menu on the left.
* Bigger the font in the word cloud below, more the number of listings of that particular builder on Magicbricks.com.
* Listings correspond to "BUYING" flats, villas, Residential Houses  etc.
""")

st.sidebar.header('Select Your Locality')


df = pd.read_csv('merge_first_second_raw_10907x23.csv')
df = df.dropna(subset=['builder'])
df['locality'] = df['locality'].astype(str)
df['builder'] = df['builder'].astype(str)
loc_list = list(df['locality'].unique())


chosen_loc = st.sidebar.selectbox('Locality',loc_list)

df_chosen_loc = df.loc[(df['locality']==chosen_loc)]
builder_list  = df_chosen_loc['builder'].values.tolist()

count = Counter(builder_list)
wordcloud = WordCloud(width = 1600, height = 800)\
.generate_from_frequencies(count)
plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.axis("off")
plt.show() 



st.header('Builders in '+ chosen_loc + ":")
st.pyplot()
st.markdown('''
* [Github Repo](https://github.com/vijayv500/Hyderabad-Housing-Prices), [Twitter](https://twitter.com/vijayv500), [Medium Blog](https://vijayv500.medium.com).
	''')
builder_list = df['builder'].values.tolist()
count = Counter(builder_list)
wordcloud = WordCloud(width = 1600, height = 800,background_color='white')\
.generate_from_frequencies(count)
plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.axis("off")
plt.show() 

st.header('List of builders in Hyderabad (all localities)')
st.pyplot()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
