from flask import Flask, render_template, request, redirect, url_for
import markdown
from model import ask  # Assuming `ask(question=...)` returns a response string
import json
import datetime

app = Flask(__name__)

responses = []

@app.route('/', methods=["GET", "POST"])
def home():
    
    # If the user sends asks a question
    if request.method == "POST":

        # Get their question
        user_question = request.form.get("user_message", "")

        # Get a response
        gpt_raw = ask(question=user_question)
        gpt_response = markdown.markdown(gpt_raw, extensions=['fenced_code'])
        
        # When response was sent
        date_sent = datetime.datetime.today().date().strftime("%Y-%m-%d")  # For current date
        now = datetime.datetime.now()  # For current date and time
        time_sent = now.strftime("%I:%M:%S %p")  # Format time to hours:minutes:seconds


        # Add response to responses
        responses.append({"question": user_question, "response": gpt_response, "date": date_sent, "time": time_sent})
        
        return redirect(url_for('home'))

    with open("chat.json","w") as f:
        json.dump(responses, f, indent=4)
    
    with open("chat.json", 'r') as f:
        data = json.load(f)

    
    return render_template("index.html", responses=data)

if __name__ == "__main__":
    app.run(debug=True)