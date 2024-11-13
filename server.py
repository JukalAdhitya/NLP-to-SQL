from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  


api_key = 'USE_API_KEY'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    
    if prompt:
        response = model.generate_content(prompt)
        return jsonify({'response': response.text})
    else:
        return jsonify({'error': 'No prompt provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
