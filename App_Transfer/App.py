from flask import Flask, render_template,request
from pickle import load
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/Analyze', methods = ['get','post'])
def Analysis():
    Data = request.form.get("Sentiment Analysis OF Badminton")

    def preprocess(raw_text):
        letters_only = re.sub("[^a-zA-Z]", " ",raw_text)

        letters_only = letters_only.lower()

        words = letters_only.split()
        
        words = [w for w in words if not w in stopwords.words("english")]
        
        stemmer = PorterStemmer()
        
        words = [stemmer.stem(word) for word in words]
        
        clean_sent = " ".join(words)
        
        return clean_sent
    

    def predict(text):
        vectorizer = load(open('Model_1/countvectorizer.pkl', 'rb'))
        
        classifier = load(open('Model_1/logit_model.pkl', 'rb'))
        
        clean_text = preprocess(text)
        
        clean_text_encoded = vectorizer.transform([clean_text])
        
        prediction = classifier.predict(clean_text_encoded)
        
        return prediction
    
    prediction = predict(Data)
    
    return render_template("home.html",prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
