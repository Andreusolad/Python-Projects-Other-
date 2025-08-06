import streamlit as st
import pandas

st.set_page_config(layout="wide")


st.title("The Best Company")
st.text("This is the official page of the best company in the world, "
        "The Best Company")

st.header("Our Team")

col1, ec1, col2, ec2, col3 = st.columns([4, 0.1, 4, 0.1, 4])

df = pandas.read_csv("Student Projects/SP Day 22/data.csv", sep=",")


with col1:
    for index, row in df[0:4].iterrows():
        st.header(row["first name"].capitalize() + "   " + row["last name"].capitalize())
        st.text(row["role"].capitalize())
        st.image(f"Student Projects/SP Day 22/images/{row['image']}")


with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"].capitalize() + "   " + row["last name"].capitalize())
        st.text(row["role"].capitalize())
        st.image(f"Student Projects/SP Day 22/images/{row['image']}")


with col3:
    for index, row in df[8:12].iterrows():
        st.header(row["first name"].capitalize() + "   " + row["last name"].capitalize())
        st.text(row["role"].capitalize())
        st.image(f"Student Projects/SP Day 22/images/{row['image']}")



