import re
import nltk

from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words=set(stopwords.words('english'))

def clean_text(text):
    # lowercase
    text = text.lower()
    
    # remove numbers
    text = re.sub(r'\d+', '', text)
    
    # remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    return " ".join(words)