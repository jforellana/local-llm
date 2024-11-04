from openai import OpenAI

client = OpenAI(
    api_key='bogus',
    base_url='http://localhost:8080/v1'
)

user_message = input("This is the beginning of your chat with AI. [To exit, send \"STOP\".] \n\nYou: ")
message = {"role":"user", "content": user_message}

conversation = [
    {"role": "system", "content": "you are a down-to-earth and very insightful conversationalist"},
    {"role": "user", "content": ""}
    ]

while(user_message!="STOP"):
    conversation[1]['content'] += f"User: {user_message} "
    completions = client.chat.completions.create(model='bogus', messages=conversation, stream=True)
    print("Assistant: ")
    conversation[1]['content'] += "Assistant: "
    for chunk in completions:
        print(chunk.choices[0].delta.content or "", end="")
        conversation[1]['content'] += chunk.choices[0].delta.content or ""
    user_message = input(f"\nYou: ")