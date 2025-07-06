import openai
import os
from dotenv import load_dotenv

# Load API Key dari file .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
print("DEBUG API KEY:", os.getenv("OPENAI_API_KEY"))
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Fungsi ngobrol ke AI
def chat_with_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Kamu adalah waifu yang manis dan suka ngobrol santai."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Loop interaktif
print("👧 AI Waifu Chatbot Siap! (Ketik 'exit' buat keluar)")
while True:
    user_input = input("Lo: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Bye bye bre~ 😘")
        break
    try:
        reply = chat_with_ai(user_input)
        print("Bot:", reply)
    except Exception as e:
        print("⚠️ Error:", e)
