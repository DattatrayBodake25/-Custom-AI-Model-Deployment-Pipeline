from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from flask_cors import CORS
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from urllib.parse import quote

model2 = Flask(__name__)
CORS(model2)  # Enable CORS for all routes

# MySQL Database Configuration
username = 'root'
password = 'Datta@2505'
host = 'localhost'
port = '3306'
database = 'modeldatabase'

# Encode the password
encoded_password = quote(password)

# Construct the MySQL connection string
model2.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{encoded_password}@{host}:{port}/{database}'
model2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a database connection
db = SQLAlchemy(model2)

# Define a model for logging requests and results
class PredictionLog(db.Model):
    id = Column(Integer, primary_key=True)
    question1 = Column(String(255))
    question2 = Column(String(255))
    prediction = Column(Float)

# Load the tokenizer and model
tokenizer = Tokenizer()
tokenizer.fit_on_texts([""])  # Empty fit to avoid errors
loaded_model = tf.keras.models.load_model('quora_question_similarity_model.h5')

# Set the maximum sequence length
max_length = 100

# Define the preprocessing function
def preprocess_text(text):
    # Remove punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenize the words
    words = text.split()

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Remove short words (length less than 3)
    words = [word for word in words if len(word) > 2]

    # Join the processed words back into a single string
    processed_text = ' '.join(words)

    # Return the preprocessed text
    return processed_text

# API endpoint for data submission and prediction
@model2.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.get_json()
    question1 = data['question1']
    question2 = data['question2']

    # Make prediction using the loaded model
    input_data = tokenizer.texts_to_sequences([preprocess_text(question1), preprocess_text(question2)])
    input_data = pad_sequences(input_data, maxlen=max_length)
    prediction = loaded_model.predict([input_data[0:1], input_data[1:]])

    # Log the request and result in the MySQL database
    rounded_prediction = round(float(prediction))
    log_entry = PredictionLog(question1=question1, question2=question2, prediction=rounded_prediction)
    db.session.add(log_entry)
    db.session.commit()

    # Return the rounded prediction as JSON response
    return jsonify({'prediction': rounded_prediction})


# Render the HTML page
@model2.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Load the tokenizer and model
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([""])  # Empty fit to avoid errors
    loaded_model = tf.keras.models.load_model('quora_question_similarity_model.h5')

    # Set the maximum sequence length
    max_length = 100
    # Run the Flask web service
    model2.run(host='0.0.0.0', port=5000, debug=True)