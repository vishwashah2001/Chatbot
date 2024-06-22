Interactive Chat with Local LLMs
Table of Contents
•	Overview
•	Installation
•	Setup Llama3
•	Setup Gemma:2b
•	Running the Streamlit Application
•	Testing the API
•	Submission Requirements
Overview
This repository contains the setup and usage instructions for interacting with two local language models, Llama3 and Gemma:2b, using a Streamlit application. The models are served via Flask APIs.
Installation
Prerequisites
- Python 3.7+
- `pip` (Python package installer)
- `virtualenv` (recommended)
Create a Virtual Environment
1. Create a virtual environment:
```sh
python -m venv venv
```
2. Activate the virtual environment:
- On Windows:
```sh
venv\Scripts\activate
```
- On macOS/Linux:
```sh
source venv/bin/activate
```
Setup Llama3
1. Clone the Llama3 repository:
```sh
git clone https://github.com/Ollama/llama3.git
cd llama3
```
2. Install dependencies:
```sh
pip install -r requirements.txt
```
3. Run the Llama3 model server:
```sh
python app.py
```
The server should be running at `http://localhost:11434/api/chat`.
Setup Gemma:2b
1. Clone the Gemma:2b repository:
```sh
git clone https://github.com/yourusername/gemma2b.git
cd gemma2b
```
2. Install dependencies:
```sh
pip install -r requirements.txt
```
3. Create a Flask server to host Gemma:2b. Save the following script as `app.py`:
```python
from flask import Flask, request, jsonify
import gemma2b  # Replace with the actual import statement for Gemma:2b

app = Flask(__name__)

# Load your Gemma:2b model here
model = gemma2b.load_model('path_to_model')  # Replace with the actual function to load the model

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    model_name = data.get('model')
    messages = data.get('messages')
    
    # Assuming your model takes a list of messages and returns a response
    response = model.generate_response(messages)  # Replace with the actual function call
    
    return jsonify({"message": {"content": response}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)
```
4. Run the Gemma:2b model server:
```sh
python app.py
```
The server should be running at `http://localhost:12345/api/chat`.
Testing the API
For Llama3
```sh
curl -X POST "http://localhost:11434/api/chat" -H "Content-Type: application/json" -d '{"model": "llama3", "messages": [{"role": "user", "content": "Hello, Llama3!"}]}'
```
For Gemma:2b
```sh
curl -X POST "http://localhost:12345/api/chat" -H "Content-Type: application/json" -d '{"model": "gemma:2b", "messages": [{"role": "user", "content": "Hello, Gemma:2b!"}]}'
```


After extensive testing and usage of both models, we observed the following:

	•	Gemma:2b:
	•	Speed: Gemma:2b exhibited faster response times during interactions, making it more efficient for real-time applications.
	•	Accuracy: The model provided more accurate and contextually relevant responses in most scenarios.
	•	Llama3:
	•	Speed: Llama3 had slower response times compared to Gemma:2b.
	•	Accuracy: While accurate, the responses were not as consistently relevant as those from Gemma:2b.

Based on these observations, Gemma:2b is recommended for applications where speed and accuracy are critical.
Youtube link: https://youtu.be/at9vMPPfFHI

