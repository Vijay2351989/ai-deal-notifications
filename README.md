# Deal Notifications

A proprietary fine-tuned LLM deployed on Modal and a RAG pipeline with a frontier model collaborate to send push notifications with great online deals.

## Before you begin

### What is this?

This is a completely autonomous agentic AI offering to get best deal notifications through push notifications. It is a practice project to implement all the building blocks of an agentic AI product.
Six agents are collaborating here to get the desired output. Each agent has a specific purpose and is responsible for a specific task. All the agents are collaborating with each other using a planning agent which also act as an orchestration agent for all the other agents. An agent framework layes is build on top of all these agent which maintain the logging, memory and monitoring aspect of the project. In the end we also have frontend using gradio ui to see the list of deals the program captures; and to make it autonomous we have a ui schedule which runs the program every scheduled interval. 

## Agents

Below is the brief description of each agent making the complete project work.

### Scanner Agent

This agent is responsible for scraping the deals from the website. It scrapes through 5 feed urls; 
parses the top 10 feed from each url; for each feed scrape through the content of the feed url to get the product details as scraped deals. It then passes the scraped deals as a context to the frontier model to get the best 5 deals from the context which has clear description and price. It also uses prompt with structured output to get the deals in a structured format. At the end scanner agent return with 5 best deals which has most clear price and description.

### Ensemble Agent for optimized price prediction

Ensemble Agent lies at the top of price predictor agent. It used three agents to predict the price of the product based on its description. Three agents predicts the price based on product description and ensemble agent that uses the linear regression model trained on a dataset to get the weighted average of the price predicted by the three agents. The three agents are:

#### Specialist Agent








