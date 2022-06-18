import re
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer



nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('omw-1.4')

def prepare_text(text, bigram=False):
    text = re.sub('[^A-Za-z ]+', ' ', text.lower()) # lower
    text = word_tokenize(text) # tokenization
    stop = stopwords.words('english')
    text = [word for word in text if (word not in stop)] # stopwords
    text = [WordNetLemmatizer().lemmatize(word) for word in text]
    if bigram:
        text = [word1 + " " + word2 for word1, word2 in zip(text, text[1:])]

    new_list = []
    new_list.append(text)
    new_list
    vectorizer = pickle.load(open("ml_models/uni_vectorizer.sav", "rb"))
    new_text = vectorizer.transform(new_list).toarray()

    return new_text