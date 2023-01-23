import openai
import json

# 初始化 API 访问密钥

user_name = input ("What is your name:")
user_token = input ("And please input your api token:")
data = {'username':user_name,'usertoken':user_token}
with open('api_token.json', 'w') as f:
    json.dump(data, f)

openai.api_key = user_token

# 初始化会话状态
conversation_history = []

while True:
    user_input = input("You: ")
    conversation_history.append(user_input)

    # 使用 API 生成回复
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"{' '.join(conversation_history)}"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 输出 API 生成的回复
    print("ChatGPT: ", response["choices"][0]["text"])
    conversation_history.append(response["choices"][0]["text"])
