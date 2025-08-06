import streamlit as st
import pandas

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=700)

with col2:
    st.title("Andreu Solà")
    content = """ I’m a Physics Engineering student at UPC 
    with a strong interest in artificial intelligence, data analysis, and finance. I have 
    experience in research projects using Python and Matlab, 
    including the classification of astronomical objects with 
    machine learning techniques. I enjoy continuous learning, 
    tackling new challenges, and applying analytical thinking 
    to solve real-world problems. """
    st.info(content)

content2="""Below you can find some of the apps I have built 
in Python. Feel free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[0::2].iterrows():
        st.header(row["title"])
        st.text(row["description"])
        st.image("images/" + row["image"]) #per obtenir el relative path.
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[1::2].iterrows():
        st.header(row["title"])
        st.text(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

