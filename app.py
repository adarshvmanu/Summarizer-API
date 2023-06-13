from flask import Flask, request, jsonify
from transformers import pipeline
import re

app = Flask(__name__)

summarizer = pipeline('summarization', model='t5-small')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    text = data['text']
    summary_size = data['summary_size']  
    result = summarizer(text, max_length=summary_size, min_length=summary_size // 2, do_sample=False)  # Use the summary size for max_length and min_length
    summary = result[0]['summary_text']
 
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', summary)
    # Generate bulleted points with capitalized first letters
    summary = '\n'.join(['• ' + sentence.capitalize() for sentence in sentences])
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
