from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import time  # Importing time module for pausing execution

# Initialize the chatbot
chat = ChatOpenAI(temperature=0, model='gpt-3.5-turbo', openai_api_key='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')

# Initialize message list with a system message
messages = [
    SystemMessage(content='You are a helpful assistant'),
]

while True:
    try:
        # Prompt user for input
        user_input = input('You: ')

        # Append user's message to the message list
        messages.append(HumanMessage(content=user_input))

        # Get AI response
        ai_response = chat(messages=messages).content

        # Print AI response
        print('AI:', ai_response)

        # Append AI response to the message list
        messages.append(AIMessage(content=ai_response))

    except Exception as e:
        if 'insufficient_quota' in str(e):
            print('Error: You have exceeded your API quota. Please try again later.')
            # You might want to wait for some time before retrying
            time.sleep(60)  # Wait for 1 minute before retrying
        else:
            print('An error occurred:', e)
