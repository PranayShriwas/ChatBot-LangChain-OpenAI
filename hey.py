# from langchain.prompts import PromptTemplate

# prompt_template=PromptTemplate.from_template(
#     'Tell me a {adjective} joke about {content}.'
# )
# prompt=prompt_template.format(adjective="funny", content="chickens")
# print(prompt)

# from langchain.prompts import PromptTemplate
# prompt_template=PromptTemplate.from_template('Tell A Joke')
# p=prompt_template.format()
# print(p)

# from langchain_core.prompts import ChatPromptTemplate

# chat_template = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful AI bot. Your name is {name}."),
#         ("human", "Hello, how are you doing?"),
#         ("ai", "I'm doing well, thanks!"),
#         ("human", "{user_input}"),
#     ]
# )

# messages = chat_template.format_messages(name="Bob", user_input="What is your name?")
# print(messages)

# from langchain.prompts import HumanMessagePromptTemplate
# from langchain_core.messages import SystemMessage
# from langchain_openai import ChatOpenAI

# chat_template = ChatPromptTemplate.from_messages(
#     [
#         SystemMessage(
#             content=(
#                 "You are a helpful assistant that re-writes the user's text to "
#                 "sound more upbeat."
#             )
#         ),
#         HumanMessagePromptTemplate.from_template("{text}"),
#     ]
# )
# messages = chat_template.format_messages(text="I don't like eating tasty things")
# print(messages)

# from langchain.prompts import PromptTemplate
# from langchain_openai import OpenAI
# from langchain.chains import LLMChain
# import time
# import openai

# openai_api_key = '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'

# demo_template = '''
# I want you to act as acting financial advisor for people
# in an easy way, explain the basics of {financial_concept}
# '''

# prompt = PromptTemplate(
#     input_variables=['financial_concept'],
#     template=demo_template
# )

# print(prompt.format(financial_concept='Income Tax'))

# llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
# chain1 = LLMChain(llm=llm, prompt=prompt)

# user_input = "Can you explain the concept of Income Tax?"

# # Retry logic
# retry_count = 0
# max_retries = 3
# retry_delay = 5  # seconds

# while retry_count < max_retries:
#     try:
#         result = chain1.invoke(input=user_input, financial_concept='Income Tax')
#         print(result)
#         break  # Exit loop if successful
#     except openai.RateLimitError as e:
#         print(f"Rate limit exceeded. Waiting {retry_delay} seconds before retrying...")
#         time.sleep(retry_delay)
#         retry_count += 1
# else:
#     print("Max retries reached. Unable to process request.")


#Language Translation

# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain_openai import OpenAI

# openai_api_key = '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'
# llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# template='''
# In an easy way, translate the following sentence '{sentence}' into {target_language}
# '''
# language_prompt = PromptTemplate(
#     input_variables=['sentence', 'target_language'],
#     template=template
# )
# language_prompt.format(sentence='How are You', target_language='hindi')

# chain2 = LLMChain(llm=llm, prompt=language_prompt)

# # Corrected the input key to 'target_language'
# chain2({'sentence': "Hello How Are You?", 'target_language': 'hindi'})

# from langchain.prompts import PromptTemplate
# prompt = (
#     PromptTemplate.from_template("Tell me a joke about {topic}")
#     + ", make it funny"
#     + "\n\nand in {language}"
# )
# print(prompt)
# PromptTemplate(input_variables=['language', 'topic'], output_parser=None, partial_variables={}, template='Tell me a joke about {topic}, make it funny\n\nand in {language}', template_format='f-string', validate_template=True)
# print(prompt.format(topic="sports", language="spanish"))

# from langchain.chains import LLMChain
# from langchain_openai import ChatOpenAI
# from langchain.prompts import PromptTemplate

# openai_api_key = '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'
# model = ChatOpenAI(openai_api_key=openai_api_key)

# prompt = (
#     PromptTemplate.from_template("Tell me a joke about {topic}")
#     + ", make it funny"
#     + "\n\nand in {language}"
# )
# chain = LLMChain(llm=model, prompt=prompt)
# chain.run(topic="sports", language="spanish")

# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
# prompt = SystemMessage(content="You are a nice pirate")
# print(prompt)
# new_prompt = (
#     prompt + HumanMessage(content="hi") + AIMessage(content="what?") + "{input}"
# )
# new_prompt.format_messages(input="i said hi")
# print([SystemMessage(content='You are a nice pirate', additional_kwargs={}),
#  HumanMessage(content='hi', additional_kwargs={}, example=False),
#  AIMessage(content='what?', additional_kwargs={}, example=False),
#  HumanMessage(content='i said hi', additional_kwargs={}, example=False)])

# from langchain.chains import LLMChain
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
# openai_api_key = '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'
# model = ChatOpenAI(openai_api_key=openai_api_key)
# prompt = SystemMessage(content="You are a nice pirate")
# new_prompt = (
#     prompt + HumanMessage(content="hi") + AIMessage(content="what?") + "{input}"
# )
# chain = LLMChain(llm=model, prompt=new_prompt)
# chain.run("i said hi")

# from langchain.prompts import FewShotPromptTemplate, PromptTemplate
# from langchain.prompts.example_selector import LengthBasedExampleSelector

# # Examples of a pretend task of creating antonyms.
# examples = [
#     {"input": "happy", "output": "sad"},
#     {"input": "tall", "output": "short"},
#     {"input": "energetic", "output": "lethargic"},
#     {"input": "sunny", "output": "gloomy"},
#     {"input": "windy", "output": "calm"},
# ]

# example_prompt = PromptTemplate(
#     input_variables=["input", "output"],
#     template="Input: {input}\nOutput: {output}",
# )
# example_selector = LengthBasedExampleSelector(
#     # The examples it has available to choose from.
#     examples=examples,
#     # The PromptTemplate being used to format the examples.
#     example_prompt=example_prompt,
#     # The maximum length that the formatted examples should be.
#     # Length is measured by the get_text_length function below.
#     max_length=25,
#     # The function used to get the length of a string, which is used
#     # to determine which examples to include. It is commented out because
#     # it is provided as a default value if none is specified.
#     # get_text_length: Callable[[str], int] = lambda x: len(re.split("\n| ", x))
# )
# dynamic_prompt = FewShotPromptTemplate(
#     # We provide an ExampleSelector instead of examples.
#     example_selector=example_selector,
#     example_prompt=example_prompt,
#     prefix="Give the antonym of every input",
#     suffix="Input: {adjective}\nOutput:",
#     input_variables=["adjective"],
# )

# print(dynamic_prompt.format(adjective="big"))
# long_string = "big and huge and massive and large and gigantic and tall and much much much much much bigger than everything else"
# print(dynamic_prompt.format(adjective=long_string))

# # You can add an example to an example selector as well.
# new_example = {"input": "big", "output": "small"}
# dynamic_prompt.example_selector.add_example(new_example)
# print(dynamic_prompt.format(adjective="enthusiastic"))

from langchain_openai import OpenAI

openai_api_key = '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'
llm = OpenAI(temperature=0.6, openai_api_key=openai_api_key)

name = llm('I want to open a restaurant for Indian food. Suggest me a fancy name for this.')
print(name)
