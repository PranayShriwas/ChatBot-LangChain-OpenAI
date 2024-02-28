from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Function to refine the prompt based on user feedback
def refine_prompt(old_prompt, feedback):
    refined_prompt = old_prompt.strip() + "\n\n" + feedback.strip() + "\n\nLet's continue optimizing the conversation!\n"
    return refined_prompt

# Your old prompt
old_prompt = "Refining and improving the prompt based on the testing, optimization."

# User feedback (hypothetical, adjust as per actual feedback)
user_feedback = """
- Users found the chatbot responses informative but occasionally too formal.
- Some users suggested adding more variety in question types to keep the conversation engaging.
- Clarification was needed on how to end or reset the conversation.
- Users also noted a desire for a more friendly and conversational tone.
"""

# Generate refined prompt
refined_prompt = refine_prompt(old_prompt, user_feedback)

# Initialize the chatbot with the refined prompt
chat = ChatOpenAI(prompt=refined_prompt, temperature=0, model='gpt-3.5-turbo', openai_api_key='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')

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
