import streamlit as st
from transformers import pipeline

#
# single-sentence/paragraph-sentiment-analyzer
#

# Load model
sentiment_analyzer = pipeline("sentiment-analysis")


# Title & Layout
st.title("Sentiment Analysis App")
st.write("Enter text below to analyze its sentiment:")
userInput = st.text_area("Your test: ")

if st.button("Analyze Sentiment"):
    # Ensure not empty
    if userInput.strip():
        result = sentiment_analyzer(userInput)[0]
        label = result['label']
        score = round(result['score'], 3)

        st.write(f"Sentiment :  {label}")
        st.write(f"Confidence :  {score}")
    else:
        st.warning("Your text area is empty.")