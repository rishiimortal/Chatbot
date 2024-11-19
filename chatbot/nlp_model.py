# chatbot/nlp_model.py

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter

class NLPModel:
    def __init__(self):
        # Load the English NLP model from spaCy
        self.nlp = spacy.load("en_core_web_sm")

    def preprocess_text(self, text):
        """Preprocess the input text: tokenize, lemmatize, and remove stop words."""
        doc = self.nlp(text)
        tokens = [token.lemma_.lower() for token in doc if token.text not in STOP_WORDS and token.is_alpha]
        return tokens

    def extract_entities(self, text):
        """Extract named entities from the input text."""
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def analyze_sentiment(self, text):
        """Analyze the sentiment of the input text."""
        doc = self.nlp(text)
        sentiment_score = doc._.polarity  # Assuming you have a sentiment analysis extension
        return sentiment_score

    def get_most_common_tokens(self, text, n=5):
        """Get the most common tokens from the input text."""
        tokens = self.preprocess_text(text)
        token_counts = Counter(tokens)
        return token_counts.most_common(n)

# Example usage
if __name__ == "__main__":
    nlp_model = NLPModel()
    
    user_input = input("Enter a sentence for NLP processing: ")
    
    # Preprocess the text
    tokens = nlp_model.preprocess_text(user_input)
    print("Preprocessed Tokens:", tokens)
    
    # Extract named entities
    entities = nlp_model.extract_entities(user_input)
    print("Named Entities:", entities)
    
    # Analyze sentiment
    sentiment_score = nlp_model.analyze_sentiment(user_input)
    print("Sentiment Score:", sentiment_score)
    
    # Get most common tokens
    common_tokens = nlp_model.get_most_common_tokens(user_input)
    print("Most Common Tokens:", common_tokens)