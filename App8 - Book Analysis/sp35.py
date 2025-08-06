import streamlit as st
import plotly.express as px
import glob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


# Get the data of the diary.
filepaths = glob.glob("diary/*.txt")
dates = [name.strip(".txt").strip("diary/") for name in filepaths]

diary_days = []
for filepath in filepaths:
    with open(filepath, 'r') as file:
        diary = file.read()
    diary_days.append(diary)


# Get the sentiment for each day
global_score = []
positive = []
negative = []
for day in diary_days:
    score = analyzer.polarity_scores(day)
    positive.append(score['pos'])
    negative.append(score['neg'])
    global_score.append(score)
print(global_score)
print('positive', positive)
print('negative', negative)


# The title of the webpage
st.title("Diary Tone")

st.subheader("Positivity")
figure = px.line(x=dates, y=positive, labels={'x': "Date", 'y': "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure = px.line(x=dates, y=negative, labels={'x': "Date", 'y': "Positivity"})
st.plotly_chart(figure)

# WE COULD DO IT WITH ONLY 2 FOR LOOPS IN THE WAY I HAVE DONE IT.
#HOWEVER, A CLEAN CODE IS NOT MY PRIORITY NOW.