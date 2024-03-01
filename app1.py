import streamlit as st
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain_openai import OpenAI
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

# Initialize Session State
if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # Input
if 'past' not in st.session_state:
    st.session_state['past'] = []  # Output
if 'input' not in st.session_state:
    st.session_state['input'] = ''
if 'stored_session' not in st.session_state:
    st.session_state['stored_session'] = []

# Define Function to get user_input
def get_text():
    '''
    Get the user input text.
    Returns:
       (str): The text entered by the user
    '''
    input_text = st.text_input('You:', value=st.session_state['input'],
                               placeholder='Your AI assistant here! Ask me anything .....',
                               key='input',
                               help='Type your message here and press Enter to send.')
    return input_text

def new_chat():
    '''
    Clear Session state and starts a new chat.
    ''' 
    save = []
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        save.append('User: ' + st.session_state['past'][i])
        save.append('Bot: ' + st.session_state['generated'][i])
        
    st.session_state['stored_session'].append(save)
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['input'] = ''
    st.session_state.entity_memory.buffer.clear()

st.title('Memory Bot')

# API
MODEL_OPTIONS = ['gpt-3.5-turbo', 'text-davinci-001', 'text-davinci-002', 'text-davinci-003', 'text-davinci-004', 'text-davinci-005', 'text-davinci-006']
selected_model = st.sidebar.selectbox(label='Model', options=MODEL_OPTIONS)
api = st.sidebar.text_input('API-Key', type='password', help='Enter your OpenAI API key')

try:
    if api:
        # Create OpenAI Instance
        llm = OpenAI(
            temperature=0,
            openai_api_key=api,
            model_name=selected_model
        )

        # Create Conversation Memory
        if 'entity_memory' not in st.session_state:
            st.session_state.entity_memory = ConversationEntityMemory(llm=llm, k=10)

        conversation = ConversationChain(
            llm=llm,
            prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
            memory=st.session_state.entity_memory
        )
    else:
        st.error('API Not Found')
    st.sidebar.button('New Chat', on_click=new_chat, type='secondary')

    # Get the user input
    user_input = get_text()

    # Generate the output using the Conversation object
    if user_input:
        output = conversation.run(input=user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

    with st.expander('Conversation'):
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            st.info(st.session_state['past'][i], icon=':coffee:')
            st.success(st.session_state['generated'][i], icon='🤖')
except Exception as e:
    st.error(f"An error occurred: {e}")
