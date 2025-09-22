#importing the necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#creating the streamlit app
st.title("COVID-19 Research Papers Explorer")
st.write("This app lets you explore metadata from COVID-19 related publications.")

#importing the data but limiting it to 5000 rows because its large
df = pd.read_csv("metadata.csv", nrows=5000)

#dropping all columns where all 5000 rows have missing values
df_cleaned = df.dropna(axis=1, how="all").copy()

# converting publish_time to datetime format
df_cleaned['publish_time'] = pd.to_datetime(
    df_cleaned['publish_time'], errors='coerce'
)

# getting the year of publish
df_cleaned['pub_year'] = df_cleaned['publish_time'].dt.year

# creating the abstract word count column
df_cleaned['abstract_word_count'] = (
    df_cleaned['abstract']
    .astype(str)          
    .apply(lambda x: len(x.split()))
)

# Sidebar Widgets
st.sidebar.header("Filters")

# Year filter
min_year, max_year = int(df_cleaned['pub_year'].min()), int(df_cleaned['pub_year'].max())
year_range = st.sidebar.slider(
    "Select Publication Year Range",
    min_year, max_year,
    (min_year, max_year)
)

# Apply filter
filtered = df_cleaned[
    (df_cleaned['pub_year'] >= year_range[0]) & 
    (df_cleaned['pub_year'] <= year_range[1])
]

# visualizing publications per year
st.subheader("Publications per Year")
papers_per_year = filtered['pub_year'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8, 4))
papers_per_year.plot(kind='bar', ax=ax, color="skyblue")
ax.set_title("Publications per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# visualizing top journals
st.subheader("Top Journals")
if 'journal' in filtered.columns:
    top_journals = filtered['journal'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    top_journals.plot(kind='bar', ax=ax, color="salmon")
    ax.set_title("Top 10 Journals Publishing COVID-19 Research")
    ax.set_xlabel("Journal")
    ax.set_ylabel("Number of Papers")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)
else:
    st.write("No 'journal' column available in the dataset.")

# creating word cloud of titles
st.subheader("Word Cloud of Paper Titles")
if 'title' in filtered.columns:
    all_titles = " ".join(filtered['title'].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_titles)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.write("No 'title' column available in the dataset.")
