from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Missing API key. Set OPENAI_API_KEY in your environment variables.")

client = OpenAI(api_key=api_key)

def promptGPT(prompt, model, system_requirements):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_requirements},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

print("\nStep 1: Starting the Interactive Story")

prompt = "Once upon a time in a small village by the forest, there lived a young girl named Elara who loved exploring the unknown. One day, she discovered a hidden path that no one had ever seen before."

model = "gpt-3.5-turbo"

system_requirements = "You are an advanced AI storyteller. Continue the given story in an engaging, immersive, and creative way while maintaining logical consistency."

initial_story = promptGPT(prompt, model, system_requirements)

print("\nGenerated Story:\n")
print(initial_story)

def split_into_chapters(full_text, chapter_length=1000):
    chapters = []
    words = full_text.split()
    for i in range(0, len(words), chapter_length):
        chapter = " ".join(words[i:i + chapter_length])
        chapters.append(chapter)
    return chapters

