from dotenv import load_dotenv
import os
import openai

# Load .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("API_KEY")

# Create OpenAI client securely
client = openai.OpenAI(api_key=api_key)

def generate_blog(paragraph_topic):
    try:
        print("Sending request to OpenAI...")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Write a paragraph about: {paragraph_topic}"}
            ],
            max_tokens=400,
            temperature=0.3
        )

        print("Response received.")
        retrieve_blog = response.choices[0].message.content.strip()
        return retrieve_blog

    except Exception as e:
        print("Error during API call:", str(e))
        return "Failed to generate blog."

print("Generating blog...")
result = generate_blog("What is life like after undergrad?")
print("Generated text:\n", result)

