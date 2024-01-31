from flask import Flask, render_template, request, jsonify
from chat import chatbot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat1.html')

@app.route("/ask", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        message = str(request.form['messageText'])
        return get_chat_response(message)

def get_chat_response(text):
    bot_response = chatbot(text)
    return jsonify({'status': 'OK', 'answer': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
