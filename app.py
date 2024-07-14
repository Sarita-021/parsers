import os
import dotenv
from flask import Flask, render_template, request, jsonify
from openai import AzureOpenAI

# Load environment variables from a .env file
dotenv.load_dotenv()


# Initialize the Flask application
app = Flask(__name__)


# Set up the Azure OpenAI client with API key, version, and endpoint
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)


# Initial conversation setup with system prompt
conversation = [
    {
        "role": "system",
        "content": "You are an AI assistant specialized in providing information about the latest trends in the fashion industry. Generate the simple text i.e. no bold. Try to generate the answer in points. Also don't give answer in detail. If you receive a question outside this domain, kindly inform the user that you cannot assist with that topic and ask if they need help with anything else related to fashion and don't answer that question."
    }
]


# Route to render the main HTML page
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle chat messages
@app.route('/chat', methods=['POST'])
def chat():
    # Get the user's message from the POST request
    user_input = request.json.get("message")

    # Append the user's message to the conversation
    conversation.append({"role": "user", "content": user_input})

    # Get the assistant's response from the Azure OpenAI service
    response = client.chat.completions.create(
        model="Myntabot",
        messages=conversation
    )

    # Extract the assistant's reply from the response
    reply = response.choices[0].message.content

    # Append the assistant's reply to the conversation
    conversation.append({"role": "assistant", "content": reply})

    # Return the assistant's reply as plain text
    return reply


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
