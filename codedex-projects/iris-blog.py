import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

client = openai.OpenAI(api_key=api_key)

def generate_blog(paragraph_topic):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Write a paragraph about: {paragraph_topic}"}
            ],
            max_tokens=400,
            temperature=0.3
        )
        retrieve_blog = response.choices[0].message.content.strip()
        return retrieve_blog
    except Exception as e:
        return f"Error generating blog: {str(e)}"

keep_writing = True

while keep_writing:
    answer = input("Write a paragraph? (Y to continue, any other key to quit): ")
    if answer.upper() == "Y":
        paragraph_topic = input("How is life post-grad?")
        print("\n" + generate_blog(paragraph_topic) + "\n")
    else:
        keep_writing = False



