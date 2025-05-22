import json


# Asks the model a question
def ask(question):
    with open("chat.json", 'r') as f:
        chat_history = json.load(f)

    from google import genai
    gemini_api_key = "AIzaSyA9WkZdmSS-PGoq6kdL1UfXVfBj8asFT_c"
    client = genai.Client(api_key=gemini_api_key)
    result = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Here is our chat history: {chat_history} (don't mention it tho its just a log of data) Using this answer the question: {question}"
    )
    return result.text.strip() 

# 