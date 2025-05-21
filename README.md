# NLP-Text-Summarizer
An intuitive web-based text summarizer built with Streamlit and NLTK, enabling users to quickly generate concise summaries from lengthy paragraphs.
# 🧠 NLP Text Summarizer

# Developers
Muhammad Yousif Khan
Umed Ali
Rizwan Ahmed

## 📌 Overview  
**NLP Text Summarizer** is an intuitive web application that summarizes lengthy texts into concise, meaningful summaries using **Natural Language Processing (NLP)** techniques. It's ideal for:
- 📚 Students summarizing lectures or notes  
- 🧪 Researchers condensing long papers  
- 💼 Professionals extracting insights from documents  

By identifying and ranking key sentences, it delivers a clean and accurate summary tailored to your needs.

---

## ✨ Key Features

- **🖥 Interactive Web Interface**  
  Powered by **Streamlit** for a real-time and user-friendly experience.

- **🎛 Customizable Summary Length**  
  Easily set the number of sentences using an interactive slider.

- **🧠 NLP-Driven Summarization**  
  Employs tokenization, word frequency analysis, and stop word filtering.

- **📄 Clean Output**  
  Delivers summaries in a structured, readable format.

- **💾 Export to Text**  
  Save the output summary as a `.txt` file for future reference.

---

## 🚀 How It Works

1. **Text Cleaning**  
   - Removes unnecessary characters, extra spaces, and citations like `[1]`.

2. **Tokenization**  
   - Splits text into individual sentences and then into words.

3. **Stop Word Removal**  
   - Eliminates common words that carry minimal meaning (e.g., *"the"*, *"is"*, *"and"*).

4. **Word Frequency Analysis**  
   - Calculates and normalizes word frequency to identify importance.

5. **Sentence Scoring**  
   - Assigns scores based on word importance, excluding overly long sentences.

6. **Summary Generation**  
   - Selects the top-scoring sentences based on user-defined summary length.

---

## 🛠 Technologies & Libraries Used

### 🐍 Programming Language
- **Python 3.x** – Primary language used for development.

### 🌐 Web Framework
- **Streamlit** – To create the front-end interface and serve the app in a web browser.

### 🧰 NLP Toolkit
- **NLTK (Natural Language Toolkit)**  
  Used for natural language operations:
  - `punkt` – for sentence and word tokenization  
  - `stopwords` – for filtering out common words

### 🧹 Utility Libraries
- `re` – Regular expressions for text preprocessing and cleanup  
- `heapq` – Efficient selection of top N scoring sentences

---

## ⚙️ Setup and Installation

To run the project locally, ensure the following Python libraries are installed:

### ✅ Required Libraries
- `streamlit`
- `nltk`

> It’s recommended to use a **virtual environment** to manage dependencies.

Also, make sure to download the following **NLTK datasets**:
- `punkt`
- `stopwords`

These will usually be downloaded automatically the first time the app runs, but can also be downloaded manually using NLTK’s downloader.

---

## 📖 Usage Instructions

Once the app is running:

1. **Input Your Text**  
   Paste or write your paragraph into the text area.

2. **Choose Summary Length**  
   Use the slider to set how many sentences you want (1 to 7).

3. **Generate Summary**  
   Click the *“✨ Generate Summary”* button.

4. **Review Output**  
   Your summary will appear under *“✅ Generated Summary”*.

5. **Download Option**  
   Click *“💾 Download Summary”* to save your summary as a `.txt` file.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report issues  
- ✨ Suggest features  
- 🔧 Improve performance  
- 🎨 Enhance UI

### Steps to Contribute:
1. Fork the repository  
2. Create a new branch: `feature/YourFeatureName`  
3. Commit your changes  
4. Push to your branch  
5. Open a Pull Request  

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

## 🙌 Acknowledgments

- Inspired by the need to summarize content efficiently for learning and research.
- Built with 💙 using Python and Streamlit.

---
