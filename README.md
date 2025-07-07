
# 📝 Text Summarization Tool

A simple Python-based Text Summarization Tool that condenses lengthy articles or documents into concise summaries using Natural Language Processing (NLP) techniques.

---

## 🚀 Features

✅ Extractive text summarization using `sumy`  
✅ Adjustable number of summary sentences  
✅ Easy to use and modify  
✅ Ideal for summarizing articles, reports, or large text documents  

---

## 🛠️ Requirements

Make sure you have Python installed. Then, install the required libraries:

```bash
pip install nltk sumy
```

---

## 📂 Usage

1. Clone or download this repository.
2. Run the Python script:

```bash
python text_summarizer.py
```

3. Example inside the script:

```python
article = """
Natural Language Processing (NLP) is a subfield of artificial intelligence (AI) concerned with the interactions between computers and human language.
It involves applying algorithms to identify and extract the natural language rules such that the unstructured language data is converted into a form that computers can understand.
NLP is at the core of many applications such as language translation, sentiment analysis, chatbots, and text summarization.
Text summarization automatically condenses large text documents into shorter versions, preserving essential information.
This helps users process information faster, improving productivity and accessibility in various domains, including education, business, and healthcare.
"""

summary = summarize_text(article, num_sentences=2)
print(summary)
```

---

## 🔧 How It Works

- The tool uses the `sumy` library's **Latent Semantic Analysis (LSA)** summarizer.  
- It extracts the most relevant sentences from the text to create a concise summary.  
- You can control the length of the summary by adjusting the `num_sentences` parameter.  

---

## 📦 Example Output

**Original Text:**  
*A long article or document...*  

**Summarized Text:**  
*The most important 2-3 sentences extracted from the article...*

---

## 💡 Future Improvements

- Support for different summarization algorithms (LexRank, TextRank)  
- Abstractive summarization using deep learning models (e.g., Hugging Face Transformers)  
- GUI or web-based interface for easier interaction  
- Summarization from text files or URLs  

---

## 📄 License

This project is for educational purposes. Feel free to modify and enhance as needed.
