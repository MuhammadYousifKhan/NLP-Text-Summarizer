import nltk
import re
import heapq
import streamlit as st

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Summarization logic
def summarize(text, max_sentences=3):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\[[0-9]*\]', ' ', text)

    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    word_frequencies = {}
    words = word_tokenize(text.lower())

    for word in words:
        if word.isalnum() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    if not word_frequencies:
        return "No meaningful words to summarize."

    max_freq = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] /= max_freq

    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                if len(sent.split(' ')) < 30:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

    summary_sentences = heapq.nlargest(max_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary

# Streamlit App UI
def main():
    st.set_page_config(page_title="🧠 NLP Text Summarizer", layout="wide")

    st.markdown("""
        <style>
        .main {
            background-color: #f8f9fa;
        }
        .title {
            font-size:40px !important;
            font-weight: bold;
            color: #2c3e50;
        }
        .summary-box {
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 10px;
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>📝 NLP Text Summarizer</div>", unsafe_allow_html=True)
    st.markdown("Enter a paragraph below and get a concise summary powered by Natural Language Processing.")

    col1, col2 = st.columns([2, 1])

    with col1:
        input_text = st.text_area("Enter your paragraph here:", height=300)

    with col2:
        max_sentences = st.slider("Number of sentences in summary:", min_value=1, max_value=7, value=3)
        generate = st.button("✨ Generate Summary")

    if generate:
        if not input_text.strip():
            st.warning("Please enter some text to summarize.")
        else:
            summary = summarize(input_text, max_sentences)
            st.markdown("### ✅ Generated Summary:")
            st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)

            # Optional: Download button
            st.download_button("💾 Download Summary", summary, file_name="summary.txt")

if __name__ == "__main__":
    main()
    #streamlit run text_summarizer_gui.py
