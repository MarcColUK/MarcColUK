import nltk
import random
from nltk.chat.util import Chat, reflections

class ChatbotDialogueManager:
    def __init__(self):
        self.chatbot_pairs = [
            [
                r"my name is (.*)",
                ["Hello %1, How are you today?",]
            ],
            [
                r"hi|hey|hello",
                ["Hello", "Hey there",]
            ],
            [
                r"what is your name ?",
                ["I am a chatbot. You can call me Chatbot.",]
            ],
            [
                r"how are you ?",
                ["I'm doing good. How about you?",]
            ],
            [
                r"sorry (.*)",
                ["It's alright.", "No problem.",]
            ],
            [
                r"I am fine",
                ["Great to hear that! How can I assist you today?",]
            ],
            [
                r"quit",
                ["Bye! Take care.", "Nice talking to you. Bye.",]
            ],
            [
                r"(.*)",
                ["Sorry, I didn't understand. Can you please rephrase?",]
            ]
        ]

        self.chatbot_chat = Chat(self.chatbot_pairs, reflections)

    def chat(self):
        print("Hello! How can I assist you today?")
        while True:
            user_input = input("> ")
            if user_input.lower() == "quit":
                break
            response = self.chatbot_chat.respond(user_input)
            print(response)

# Example usage:
chatbot = ChatbotDialogueManager()
chatbot.chat()
