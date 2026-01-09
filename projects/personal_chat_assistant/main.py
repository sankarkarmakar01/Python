# Rule Based AI Python ChatBot

import datetime

name = input("Hello, what is your name?")
present_hour = datetime.datetime.now().hour

if 5 <= present_hour <= 11:
    print("Good Morning,", name)
elif 11 <= present_hour <= 17:
    print("Good Afternoon,", name)
elif 17 <= present_hour <= 20:
    print("Good Evening,", name)
else:
    print("Good Night,", name)

print("Hello, Welcome to Your Buddy ChatBot")
print("You can ask me basic questions, Type 'bye' to exit from the bot")

# Chatbot Memory Creation [ dictionary of response ]
response = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you?": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great to hear that"
}

# Method/Function to get response of ChatBot
def get_response_of_bot(user_question):
    user_question = user_question.lower()
    for eachKey in response:
        if eachKey in user_question:
            return response[eachKey]
    return "I am not able to tell that yet, I am in learning mode."

# Take user input
while True:
    user_input = input("Please ask your question: ")

    if "bye" in user_input.lower():
        break

    replay = get_response_of_bot(user_input)
    print("Bot Response: ", replay)
