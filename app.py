from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

summarizer = pipeline('summarization')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    text = data['text']
    result = summarizer(text, max_length=100, min_length=30, do_sample=False)
    summary = result[0]['summary_text']
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)