from flask import request, jsonify
from app import app
from app.model import generate_text

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    generated_text = generate_text(prompt)
    return jsonify({'generated_text': generated_text})
