from flask import Flask, render_template, request, jsonify
from pdf_extraction import process_pdf  # Make sure your pdf_extraction.py exists
import os

app = Flask(__name__)

# =================== ROUTES ===================

@app.route('/')
def home():
    return render_template('index.html')

# 1. Chat Route
from serpapi import GoogleSearch

SERPAPI_API_KEY = "367206b60740ae8dc0db8a7760fd4d320477d56ae5af2d8ba484f56c4463b203"  # Paste your key here

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_question = data.get('question', '')

    if not user_question:
        return jsonify({'question': 'No question received!'})

    params = {
        "engine": "google",
        "q": user_question,
        "api_key": SERPAPI_API_KEY,
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Try to get direct answer if available
    if "answer_box" in results:
        response = results["answer_box"].get("answer", "Sorry, I couldn't find a direct answer.")
    else:
        # If no direct answer, fallback to organic results
        organic_results = results.get("organic_results", [])
        if organic_results:
            response = organic_results[0].get("snippet", "Sorry, I couldn't find an answer.")
        else:
            response = "Sorry, I couldn't find an answer."

    return jsonify({'question': response})


# 2. Upload PDF Route
@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded!'})

    file = request.files['file']

    return jsonify({'message': 'PDF uploaded successfully!'})

# 3. Extract Text Route
@app.route('/extract_text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    text = process_pdf(file)
    return jsonify({'text': text})

# 4. Generate Routine
@app.route('/get_routine', methods=['POST'])
def get_routine():
    data = request.get_json()
    days_left = int(data.get('days_left', 0))
    topics = data.get('topics', [])

    routine = [f"Day {i+1}: Study {topic}" for i, topic in enumerate(topics)]
    return jsonify({'routine': routine})

# 5. Summarize Text Route ✅
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'summary': 'No text provided!'}), 400

    sentences = text.split('. ')
    summary = '. '.join(sentences[:5])
    if not summary.endswith('.'):
        summary += '.'

    return jsonify({'summary': summary})

# =================== MAIN ===================
if __name__ == '__main__':
    app.run(debug=True)


#Vidisha Arpita