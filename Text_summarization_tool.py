# Text Summarization Tool using NLP  
from sumy.parsers.plaintext import PlaintextParser  
from sumy.nlp.tokenizers import Tokenizer  
from sumy.summarizers.lsa import LsaSummarizer  # You can use other summarizers as well  
import nltk  

# Download necessary NLTK data  
nltk.download("punkt")  


def summarize_text(text, num_sentences=3):  
    """  
    Summarizes the input text into the desired number of sentences.  
    Args:  
        text (str): The lengthy article or text to summarize.  
        num_sentences (int): Number of summary sentences desired.  
    Returns:  
        str: Concise summary of the text.  
    """  
    parser = PlaintextParser.from_string(text, Tokenizer("english"))  
    summarizer = LsaSummarizer()  # Latent Semantic Analysis based summarizer  

    summary_sentences = summarizer(parser.document, num_sentences)  
    summary = " ".join(str(sentence) for sentence in summary_sentences)  

    return summary  


# Example Usage  
if __name__ == "__main__":  
    article = """  
    Natural Language Processing (NLP) is a subfield of artificial intelligence (AI) concerned with the interactions between computers and human language.  
    It involves applying algorithms to identify and extract the natural language rules such that the unstructured language data is converted into a form  
    that computers can understand. NLP is at the core of many applications such as language translation, sentiment analysis, chatbots, and text summarization.  
    Text summarization automatically condenses large text documents into shorter versions, preserving essential information. This helps users process information  
    faster, improving productivity and accessibility in various domains, including education, business, and healthcare.  
    """  

    print("Original Text:\n")  
    print(article)  

    print("\nSummarized Text:\n")  
    print(summarize_text(article, num_sentences=2))  
