import openai
from openai import Completion
from config import apikey

def test_openai():
    print("API Key is:", apikey)
# Set API key
openai.api_key = apikey

# Create response from OpenAI
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Write an email to my boss for resignation?",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print only the text
print(response["choices"][0]["text"].strip())
