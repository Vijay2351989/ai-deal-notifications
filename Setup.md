# Local environment setup

## Prerequisites

1. Install python
2. Install pip
3. Install anaconda

## Activate environment
4. Set up anaconda environment using environment.yml file
   conda env create -f environment.yml (This will create a conda env with anme pricer)
5. Activate the environment
   conda activate pricer


## Set up .env file for environment variables

1. For the project to run end to end we will need some api keys to be configured in .env file.
2. Create a .env file in the root directory of the project.

3. [Set up open api key](https://platform.openai.com/api-keys). Add the key to the .env file as         OPENAI_API_KEY=<your-key>

4. [Set up hugging face token](https://huggingface.co/settings/tokens). Add the token to the .env file as HF_TOKEN=<your-token>

5. [Set up pushover account for push notifications](https://pushover.net/)
   a. Once you set up your account you will get a pushover user key. Add it to the .env file as PUSHOVER_KEY=<your-key>
   
   b. You will also need to create an application. Add the application token to the .env file as PUSHOVER_TOKEN=<your-token>

6. For envrionment variable to take effect you will need to reactivate the environment.
   conda activate pricer

## [Set up modal](https://modal.com)

1. Add your card to get a free $30 credit.
2. Create a workspace.

### We need to set your HuggingFace Token as a secret in Modal

1. Go to modal.com, sign in and go to your dashboard
2. Click on Secrets in the nav bar
3. Create new secret, click on Hugging Face, this new secret needs to be called **hf-secret** because that's how we refer to it in the code
4. Fill in your HF_TOKEN where it prompts you

### Setting up modal token

1. Run `modal setup` from terminal. It connects with Modal and installs your tokens.
2. This will create a modal token in your modal dashboard under API Tokens.
3. Also it will create the modal.toml file at the root user directory of your machine.
4. Copy the token and secret from toml file.
5. From an activated environment in the command line run:  
`modal token set --token-id <your_token_id> --token-secret <your_token_secret>` 

# Fine tune LLM deployment in modal
To deploy the fine tuned LLM in modal we need to run below command at the command line in an activated environment
modal deploy -m pricer_service

Once the above command run successfully you will be able to see a deployed service in your modal dashboard under Apps section as a live app. (price-predictor-service)

# Create vector datastore
To create the vector datastore run below command at the command line in an activated environment
python create_vector_store.py

# Create random forest model
To create the random forest model run below command at the command line in an activated environment
python create_random_forest_model.py

# Create ensembel model
To create the ensembel model run below command at the command line in an activated environment
python create_ensemble_model.py

# Start the app
To start the app run below command at the command line in an activated environment
python run app.py


   
