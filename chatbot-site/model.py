# Asks the model a question
def ask(question):
    from google import genai
    gemini_api_key = "AIzaSyA9WkZdmSS-PGoq6kdL1UfXVfBj8asFT_c"
    client = genai.Client(api_key=gemini_api_key)
    result = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=question
    )
    return result.text.strip() 
