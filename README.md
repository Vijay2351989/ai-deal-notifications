# Deal Notifications

A proprietary <span style="color:neongreen">**fine-tuned LLM**</span> deployed on Modal and a **RAG pipeline with a frontier model** collaborate to send push notifications with great online deals.

## Before you begin

### What is this?

This is a completely **autonomous agentic AI** offering to get best deal notifications through push notifications. It is a practice project to implement all the building blocks of an agentic AI product.
Six agents are collaborating here to get the desired output. Each agent has a specific purpose and is responsible for a specific task. All the agents are collaborating with each other using a **planning agent** which also act as an orchestration agent for all the other agents. An **agent framework layer** is build on top of all these agent which maintain the logging, memory and monitoring aspect of the project. In the end we also have frontend using **gradio ui** to see the list of deals the program captures; and to make it autonomous we have a ui schedule which runs the program every scheduled interval. 

## LLM Agents

Below is the brief description of each LLM agent making the complete project work.

### Scanner Agent

This agent is responsible for scraping the deals from the website. It scrapes through 5 feed urls; 
parses the top 10 feed from each url; for each feed scrape through the content of the feed url to get the product details as scraped deals. It then passes the scraped deals as a context to the frontier model to get the best 5 deals from the context which has clear description and price. It also uses prompt with structured output to get the deals in a structured format. At the end scanner agent return with 5 best deals which has most clear price and description.

### Ensemble Agent for optimized price prediction

Ensemble Agent lies at the top of price predictor agent. It used three agents to predict the price of the product based on its description. Three agents predicts the price based on product description and ensemble agent that uses the **linear regression model** trained on a dataset to get the weighted average of the price predicted by the three agents. The three agents are:

#### Specialist Agent

This agent is responsible for predicting the price of the product based on its description. It uses in the background a fine tuned LLM model and the model is deployed on [modal cloud as a live app](https://modal.com/). The fine tuned model is trained on a vast dataset of products. The raw dataset used for training is [pulled from huggingface](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023/tree/main/raw/review_categories). It is curated and used for training the [llama 8B paramdeter model](https://huggingface.co/meta-llama/Llama-3.1-8B) using **QLORA technique** targetting the attention layer of the pretrained model. The fine tuned model is [available as a public model](https://huggingface.co/Jai23051989/pricer-2024-09-13_13.04.39).

#### Frontier Agent

This agent is again predicting the price of a product; but with a different approach. It uses the training dataset mentioned in specialist agent section to. create a **vector store using chroma db**. 

**Vector store uses the open source embedding model :**
[The all-MiniLM is a very useful model from HuggingFace that maps sentences & paragraphs to a 384 dimensional dense vector space and is ideal for tasks like semantic search.](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

 The vector store is then used to set a **RAG pipeline** to retrieve price of product semantically closer to the product description and pass it as an extra context to the frontier model (gpt-4o-mini). This approach gives extra power to the frontier model to predict the price of the product based on the context set in prompt.

#### Random Forest Agent

What better to bring in a **baseline model ramdom forest aggressor from scikit** and fit it to the prices of the trained data in chroma vectorstore mentioned above. This is exactly what this agent uses. It again predict price of product but the model used is a random forest model trained on the product vectorstore created using the chromadb.

## Messaging Agent









