from flask import Flask, render_template, request, redirect, url_for
import markdown
from model import ask  # Assuming `ask(question=...)` returns a response string
import datetime
from save import *

app = Flask(__name__)

responses = []

def get_chat_data():
    user_question = request.form.get("user_message", "")

    # Get a response
    gpt_raw = ask(question=user_question)
    gpt_response = markdown.markdown(gpt_raw, extensions=['fenced_code'])
    
    # When response was sent
    date_sent = datetime.datetime.today().date().strftime("%Y-%m-%d")  # For current date
    now = datetime.datetime.now()  # For current date and time
    time_sent = now.strftime("%I:%M:%S %p")  # Format time to hours:minutes:seconds

    return {"question": user_question, "response": gpt_response, "date": date_sent, "time": time_sent}


@app.route('/', methods=["GET", "POST"])
def home():
    
    # If the user sends asks a question
    if request.method == "POST":

        # Get their question
        chat_data = get_chat_data()

        # Add response to responses
        responses.append(chat_data)
        
        return redirect(url_for('home'))

    write_json("chat.json", responses)
    
    return render_template("index.html", responses=responses)

if __name__ == "__main__":
    app.run(debug=True)