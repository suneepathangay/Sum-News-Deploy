Sum News

Sum News was project developed by me for summarizing news articles. The basic synposis of the project is that a user would either put in a lengthy article of their choice and they would recieve a short summary.

Tech Stack- Flask, Langchain, Pinecone, Huggingface

The entire application is centered around a Flask server which handles backend functionality alogn with serving web pages. 

Algorithm- For this project, I developed an approach to summarizing articles using vecotr embeddings. I tokenized the text into sentences. I then embedded those sentences into vectors using a pretrained Sentence transformers model. The next step was to build a similiartiy matrix for each sentence. Using the notion that sentences that 
have the highest similarity scores are the most important I was able to determine the most important vectors using the cosine similiartiy algorithm. From there I was able to decode the top 3 or 4 most important sentences.

Chatbot- The chatbot is a new feature that I am currently developing. The main synopsis of it is the user feeds text to the chatbot and the user is able to ask questions about the text. Currently, I am buidling the chatbot through a combination of Langchain, Pinecone, and OpenAI API.



