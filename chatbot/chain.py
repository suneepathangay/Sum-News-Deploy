


from langchain.llms import openai
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv())


llm=openai.OpenAI(model_name="gpt-3.5-turbo-instruct")

res=llm("explain large language models in one sentence")

print(res)

# pinecone_key='da54c716-4fe0-4222-b321-67148fd0361d'

# open_ai='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'

