#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code for sentiment analysis app for UIS PMO


# In[12]:


get_ipython().system('pip install streamlit')


# In[2]:


get_ipython().system('pip install textblob -i https://pypi.org/simple')


# In[3]:


get_ipython().system('pip show textblob')


# In[1]:


# Writing the Streamlit app code to a file
app_code = """
import streamlit as st
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit UI
st.title("Sentiment Analysis App for UIS PMO")
st.subheader("Analyze the sentiment of your text or dataset")

# Input options
option = st.radio("Choose input type:", ("Manual Text", "Upload CSV File"))

if option == "Manual Text":
    user_input = st.text_area("Enter text to analyze:")
    if user_input:
        blob = TextBlob(user_input)
        polarity, subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
        st.write(f"Polarity: {polarity}")
        st.write(f"Subjectivity: {subjectivity}")

elif option == "Upload CSV File":
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
        if 'text' in df.columns:
            df['Polarity'], df['Subjectivity'] = zip(*df['text'].apply(lambda x: TextBlob(x).sentiment))
            st.dataframe(df)
            st.write("Sentiment Analysis Completed!")
            # Plot polarity distribution
            plt.figure(figsize=(10, 5))
            plt.hist(df['Polarity'], bins=20, edgecolor='black')
            plt.title('Polarity Distribution')
            plt.xlabel('Polarity')
            plt.ylabel('Frequency')
            st.pyplot(plt)
        else:
            st.error("The file must contain a 'text' column.")
"""

# Save the code to a file
with open("sentiment_app.py", "w") as f:
    f.write(app_code)

print("Streamlit app code saved as 'sentiment_app.py'")


# In[ ]:


get_ipython().system('streamlit run sentiment_app.py')


# In[11]:


get_ipython().system('pip show streamlit')

