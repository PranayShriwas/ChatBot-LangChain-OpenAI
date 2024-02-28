
# ChatBot Using LangChain and OpenAI

This script demonstrates how to build a chatbot using LangChain and OpenAI's GPT-3 model. The chatbot refines and improves its prompt based on user feedback, providing a more engaging and user-friendly conversation experience.

# Usage

1. Installation
   Make sure you have LangChain and OpenAI's Python library installed. You can install them using pip:
   pip install langchain_openai

2. Configuration
   - Replace `'your_api_key'` with your actual OpenAI API key.
   - Adjust the initial prompt, user feedback, and other parameters as needed.
     
3. Execution
   Run the script using Python:
   python main.py

4. Interaction
   - The chatbot starts with a system message welcoming the user to the chat.
   - Enter your message when prompted with "You: ".
   - The chatbot will respond based on the input using the refined prompt.
   - The conversation continues until interrupted or an error occurs.

# Script Overview

1. Refining the Prompt
   - The script defines a function `refine_prompt` to refine the prompt based on user feedback.
   - Initial prompt and user feedback are provided as examples.

2. Initialization
   - The initial prompt is refined based on user feedback.
   - The chatbot is initialized with the refined prompt, using the LangChain `ChatOpenAI` class.

3. Conversation Loop
   - The script enters a loop to facilitate the conversation.
   - User input is captured and appended to the message list as a human message.
   - The chatbot processes the messages and generates a response.
   - The response is printed and appended to the message list as an AI message.
   - Errors, such as API quota exceeded, are handled gracefully.

# Code
# Import required libraries
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import time

# Function to refine the prompt based on user feedback
def refine_prompt(old_prompt, feedback):
    refined_prompt = old_prompt.strip() + "\n\n" + feedback.strip() + "\n\nLet's continue optimizing the conversation!\n"
    return refined_prompt

# Define initial prompt and user feedback
old_prompt = "Refining and improving the prompt based on the testing, optimization."
user_feedback = """
- Users found the chatbot responses informative but occasionally too formal.
- Some users suggested adding more variety in question types to keep the conversation engaging.
- Clarification was needed on how to end or reset the conversation.
- Users also noted a desire for a more friendly and conversational tone.
"""

# Generate refined prompt
refined_prompt = refine_prompt(old_prompt, user_feedback)

# Initialize the chatbot with the refined prompt
chat = ChatOpenAI(temperature=0, model='gpt-3.5-turbo', openai_api_key='your_api_key', model_kwargs={'prompt': refined_prompt})

# Initialize message list with a system message
messages = [
    SystemMessage(content="Welcome to the chat!"),
]

# Conversation loop
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
```

### Additional Instructions

- Make sure to adjust the initial prompt and user feedback based on the specific requirements and feedback received.
- Follow proper error handling practices to gracefully handle exceptions and errors that may occur during execution.
