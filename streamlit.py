import pandas as pd 
import streamlit as st 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Builders In Your Locality: Hyderabad')

st.markdown("""
This app displays list of builders in your locality as word cloud.
* **Data source:** Magicbricks
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



st.header('Display Companies in Selected locality')
st.pyplot()