#Store the FAQs in a structured format, such as a JSON or database:
    
    
{
  "FAQs": [
    {
      "question": "What are your support hours?",
      "answer": "Our support team is available 24/7."
    },
    {
      "question": "How can I reset my password?",
      "answer": "To reset your password, click on 'Forgot Password' on the login page."
    }
  ]
}


#Install the required libraries:

    
pip install nltk spacy flask
python -m spacy download en_core_web_sm



import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np




#Load SpaCy model

nlp = spacy.load("en_core_web_sm")




#FAQ data

FAQS = [
    {"question":"What are your support hours?","answer":"Our support team is available 24/7."},
    {"question":"How can I reset my password?","answer":"To reset your password, click on 'Forgot Password' on the login page."}
]



#Function to find the best matching FAQ

def get_best_match(user_question):
    questions = [faq["question"] for faq in FAQS]
    
    #Vectorize questions
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(questions)
    
    #Vectorize user input
    
    user_vector = vectorizer.transform([user_question])
    
    #Compute cosine similarity
    
    similarity = cosine_similarity(user_vector, tfidf_matrix).flatten()
    best_match_index = np.argmax(similarity)
    
    if similarity[best_match_index] > 0.5:  # Threshold for similarity
        return FAQS[best_match_index]["answer"]
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase your question?"




from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = get_best_match(user_input)
    return jsonify({"response": response})




if __name__ == "__main__":
    app.run(debug=True)



#User Input:

{"message": "How do I reset my password?"}


#Output:

{
  "response": "To reset your password, click on 'Forgot Password' on the login page."
}





