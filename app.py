from langchain_openai import ChatOpenAI 
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Initialize the chatbot
chat = ChatOpenAI(temperature=0, model='gpt-3.5-turbo', openai_api_key='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')

# Initialize message list with a system message
messages = [
    SystemMessage(content='You are a helpful assistant'),
]

# Define test scenarios
test_scenarios = [
    "What is your name?",
    "Can you help me with programming?",
    "Tell me a joke.",
    "What is the capital of France?",
    "How do I bake a cake?",
    "What is the weather like today?",
    "Can you recommend a good book?",
    "How can I improve my productivity?",
    "What is the average airspeed velocity of an unladen swallow?",
    "How do I fix a leaking faucet?",
    "Tell me about the history of ancient Egypt.",
    "What are some healthy breakfast ideas?",
    "Can you explain the theory of relativity?",
    "What's the best way to prepare for a job interview?",
    "Tell me about the benefits of meditation.",
    "How do I start a small business?",
    "What is the Pythagorean theorem?",
    "How do I troubleshoot a computer that won't turn on?",
    "Can you recommend a good movie to watch?",
]

# Execute test cases
for test_scenario in test_scenarios:
    try:
        # Prompt user for input
        user_input = test_scenario

        # Append user's message to the message list
        messages.append(HumanMessage(content=user_input))

        # Get AI response
        ai_response = chat(messages=messages).content  # Updated parameter name

        # Print AI response
        print('User:', user_input)
        print('AI:', ai_response)
        print('---')

        # Append AI response to the message list
        messages.append(AIMessage(content=ai_response))

    except Exception as e:
        print('An error occurred:', e)
