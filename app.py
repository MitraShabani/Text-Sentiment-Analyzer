import streamlit as st
from transformers import pipeline
# import matplotlib.pyplot as plt


#
# single-sentence/paragraph-sentiment-analyzer
#

# Load model
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis")

sentiment_analyzer = load_sentiment_model()


# Title & Layout
st.title("Sentiment Analysis App")
st.write("Enter your sentences below to analyze their sentiment:")
userInput = st.text_area(
                "",
                height=150,
                placeholder="Enter one sentence per line "
)


if st.button("Analyze Sentiment"):
    lines = [ln.strip() for ln in userInput.split("\n") if ln.strip()]

    # Ensure not empty
    if lines:
         with st.spinner("Analyzing…"):
            results = sentiment_analyzer(lines, truncation=True)

         for userInput, result in zip(lines,results):
            st.write(f"  {userInput}  ->  \n{result['label']} ({result['score']:.2f})")

    else:
        st.warning("Please enter at least one non-empty line.")