# Deal Notifications

A proprietary fine-tuned LLM deployed on Modal and a RAG pipeline with a frontier model collaborate to send push notifications with great online deals.

## Before you begin

### What is this?

This is a completely autonomous agentic AI offering to get best deal notifications through push notifications. It is a practice project to implement all the building blocks of an agentic AI product.
Six agents are collaborating here to get the desired output. Each agent has a specific purpose and is responsible for a specific task. All the agents are collaborating with each other using a planning agent which also act as an orchestration agent for all the other agents. An agent framework layes is build on top of all these agent which maintain the logging, memory and monitoring aspect of the project. In the end we also have frontend using gradio ui to see the list of deals the program captures; and to make it autonomous we have a ui schedule which runs the program every scheduled interval. The program when started will : 

1. Run at a configured scheduled interval (Every 1 min) ->
2. 





