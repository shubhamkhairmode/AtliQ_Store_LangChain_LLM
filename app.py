from flask import Flask, render_template, request, send_from_directory, jsonify
from langchain_helper import get_few_shot_db_chain

app = Flask(__name__)

# Set Streamlit title and developer details
page_title = "AtliQ Brand Store: Database Q&A 👕"
developer_info = "Developed by Shubham Khairmode\nContact: shubhambkhairmode@gmail.com"

@app.route('/')
def index():
    return render_template('index.html', page_title=page_title, developer_info=developer_info)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    if question:
        chain = get_few_shot_db_chain()
        response = chain.run(question)
        return response
    return "Please ask a question."

# Serve static files
@app.route('/static/css/<path:filename>')
def css(filename):
    return send_from_directory('static/css', filename)

@app.route('/static/data/<path:filename>')
def data(filename):
    return send_from_directory('Data', filename)

if __name__ == '__main__':
    app.run(debug=True)
