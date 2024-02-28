from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import time

# Function to refine the prompt based on user feedback
def refine_prompt(old_prompt, feedback):
    refined_prompt = old_prompt.strip() + "\n\n" + feedback.strip() + "\n\nLet's continue optimizing the conversation!\n"
    return refined_prompt

# Function to continuously refine the prompt based on user feedback
def continuously_refine_prompt(old_prompt):
    while True:
        try:
            # Gather feedback (hypothetical, adjust as per actual feedback collection mechanism)
            user_feedback = input("Please provide feedback on the chat experience: ")

            # Refine prompt based on user feedback
            old_prompt = refine_prompt(old_prompt, user_feedback)

            # Update chat initialization with the refined prompt
            chat = ChatOpenAI(temperature=0, model='gpt-3.5-turbo', openai_api_key='your_api_key', model_kwargs={'prompt': old_prompt})

            # Initialize message list with a system message
            messages = [
                SystemMessagePromptTemplate(content="Welcome to the chat!").to_message(),
            ]

            # Start the conversation loop
            while True:
                # Prompt user for input
                user_input = input('You: ')

                # Append user's message to the message list
                messages.append(HumanMessagePromptTemplate(content=user_input).to_message())

                # Get AI response
                ai_response = chat(messages=messages).content

                # Print AI response
                print('AI:', ai_response)

                # Append AI response to the message list
                messages.append(AIMessagePromptTemplate(content=ai_response).to_message())

        except Exception as e:
            if 'insufficient_quota' in str(e):
                print('Error: You have exceeded your API quota. Please try again later.')
                # You might want to wait for some time before retrying
                time.sleep(60)  # Wait for 1 minute before retrying
            else:
                print('An error occurred:', e)

# Your old prompt
old_prompt = "Refining and improving the prompt based on the testing, optimization."

# Start the continuous refinement of prompt based on user feedback
continuously_refine_prompt(old_prompt)
