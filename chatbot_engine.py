# chatbot_engine.py

import pyttsx3
from datetime import datetime
import random

# === 1. Speak Function === #
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# === 2. Load Routine === #
def load_routine(day_num):
    try:
        with open(f'routine_day{day_num}.txt', 'r') as file:
            topics = file.readlines()
        return [topic.strip() for topic in topics]
    except Exception:
        return []

# === 3. Load Important Topics === #
def load_important_topics():
    try:
        with open('important_topics.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception:
        return []

# === 4. Generate a Response === #
def chatbot_response():
    today = datetime.now().day
    routine = load_routine(today % 4 + 1)  # Loop between day 1-4
    important_topics = load_important_topics()

    response = "Hey! I'm your StudyMate AI 👩‍💻.\n"
    if routine:
        response += f"Today you should focus on: {', '.join(routine)}.\n"
    else:
        response += "No specific routine found for today.\n"

    if important_topics:
        response += f"Important topics from previous years: {', '.join(important_topics[:5])}.\n"
    else:
        response += "No important topics found.\n"

    response += "Stay focused and avoid distractions. Remember, you are capable of achieving your target!"
    return response

# === 5. Get Chatbot Reply === #
def get_chatbot_reply(message):
    message = message.lower()
    if "motivate" in message:
        return "Keep going! Every step you take gets you closer to your dreams! 💪"
    elif "topic" in message:
        return "Let's plan your topics wisely. Stay consistent!"
    else:
        return "I'm always here to support you. Let's achieve greatness together!"

# === 6. Quiz System === #
def get_quiz_question():
    quiz = [
        {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "answer": "O(log n)"},
        {"question": "Which keyword is used to define a function in Python?", "options": ["func", "define", "def", "function"], "answer": "def"},
        {"question": "What does HTML stand for?", "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyper Text Marketing Language", "None"], "answer": "Hyper Text Markup Language"},
    ]
    return random.choice(quiz)

# === 7. Test Running === #
if __name__ == "__main__":
    bot_text = chatbot_response()
    print(bot_text)
    speak(bot_text)
