print()
print("Welcome to Virtual Bot")
print()
# printing out a description of the Chat Bot for the users.
print("This is a friendly Virtual Chat Bot designed to interact with the user who wants to spend their time chatting. You can start to chat by typing in your name, and whenever you feel like you want to stop the chat you can type in done.")
print()

# Starting the chat by asking users name.
username = input("What is your name? ")
print()
print("Hello "+username+",")
print()
# saying hello to the user and start greeting.

import random

# using 'get_bot_response' function to print a random response to the user from the responses listed.
# creating lists of possible inputs(responses) that the user may type in.
# creating lists of messages that we want to print in response to users inputs.
def get_bot_response(user_response):

    bot_input_1 = ["great", "Great", "good", "Good", "I am feeling good", "I'm feeling good", "I am feeling great", "I'm feeling great"]
    bot_input_2 = ["Ok", "ok", "fine", "Fine", "I am fine", "I'm fine", "I am ok", "I'm ok"]
    bot_input_3 = ["Happy", "happy", "Awesome", "awesome", "feeling happy", "feeling awesome"]
    
    bot_response_1 = ["Glad to hear that!", "Perfect!", "I'm happy to hear that!"]
    bot_response_2 = ["I'm here for you", "I understand"]
    bot_response_3 = ["Great?", "Sending good vibes", "Very good!","Wonderful"]

# using 'if conditionals' to be able to have variety of responses for the user inputs.
    if user_response in bot_input_1:
        return random.choice(bot_response_1)
    elif user_response in bot_input_2:
        return random.choice(bot_response_2)
    elif user_response in bot_input_3:
        return random.choice(bot_response_3)
    else:
        return "All right"

# creating a 'while loop' so that our function continuously runs the code, untill we recieve the respond "done" from the user.
user_response = ""
while user_response != "done":
    user_response = input("How are you feeling? ")
    bot_response = get_bot_response(user_response)
    print(bot_response)

# When recieved the respond "done" the chat is over.