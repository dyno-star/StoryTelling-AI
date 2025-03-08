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

initial_chapters = split_into_chapters(initial_story)

print(f'Chapter 1: {initial_chapters[0]}')
print(f'Beginning of the Story:\n{initial_story}\n')

print(f'Step 2: Making the story interactive')
user_choice= input("Elara reaches a fork in the path. Should she go either left towards the dark cave, right towards the sparkling stream, or climb the mysterious tree? (Enter 'left', 'right' or 'climb'):)") 
if user_choice.lower()== 'left':
    prompt = 'Elara took a deep breath and chose the left path, heading towards the dark cave. As she approached, she heard strange whispers echoing from the inside...'

elif user_choice.lower() == 'right':
    prompt = 'Elara chose to follow the right path, towards the sparkling stream, the air became fresher, and she noticed something shimmering beneath the water...'

elif user_choice.lower() == 'climb':
    prompt = 'Elara to climb the mysterious tree, as she ascended she noticed an old wooden box hidden in the branches, covered in strange carvings...'

else:
     prompt = 'Elara hesistated, unsure of which path to take so decided to sit and think for a moment'


next_part = promptGPT(prompt, model, system_requirements)

print(f'Next Part of the Story:\n{next_part}\n')
