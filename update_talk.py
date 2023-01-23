import openai
import json
import sys
import time

user_name = input ("What is your name:")
user_token = input ("And please input your api token:")
data = {'username':user_name,'usertoken':user_token}
with open('api_token.json', 'w') as f:
    json.dump(data, f)

# Set the API key
openai.api_key = user_token

# Define the model 
model_engine = "text-davinci-002"

active = True
while active:
    # Input user question
    ask = input("Please input your question here:")

    # Make the API request
    response = openai.Completion.create(
        engine=model_engine,
        prompt=ask,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the response
    print(response["choices"][0]["text"])
    print('\n')

    question = input("Do you want to ask another quesion?(Y/n)")
    if question == 'Y' or question == 'y':
        active = active
    elif question == 'N' or question == 'n':
        active = False
        print("This program will exit in 3 seconds leter!")
        time.sleep(3)
        del openai.api_key
        sys.exit()
