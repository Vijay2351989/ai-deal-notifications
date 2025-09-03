import os
import chromadb
from datasets import load_dataset
from dotenv import load_dotenv
from items import Item
from huggingface_hub import login
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# environment

load_dotenv(override=True)
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')
os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN', 'your-key-if-not-using-env')
DB = "products_vectorstore"

# Log in to HuggingFace

hf_token = os.environ['HF_TOKEN']
login(hf_token, add_to_git_credential=True)

# Create vector datastore
ds = load_dataset("Jai23051989/pricer-data")
train = ds['train']
test = ds['test']

DB = "products_vectorstore"

client = chromadb.PersistentClient(path=DB)
collection = client.get_or_create_collection('products')

from agents.specialist_agent import SpecialistAgent
from agents.frontier_agent import FrontierAgent
from agents.random_forest_agent import RandomForestAgent

specialist = SpecialistAgent()
frontier = FrontierAgent(collection)
random_forest = RandomForestAgent()

def description(item):
    return item['text'].prompt.split("to the nearest dollar?\n\n")[1].split("\n\nPrice is $")[0]

specialists = []
frontiers = []
random_forests = []
prices = []
for item in tqdm(test.select(range(1000, 1250))):
    text = description(item)
    specialists.append(specialist.price(text))
    frontiers.append(frontier.price(text))
    random_forests.append(random_forest.price(text))
    prices.append(item.price)

mins = [min(s,f,r) for s,f,r in zip(specialists, frontiers, random_forests)]
maxes = [max(s,f,r) for s,f,r in zip(specialists, frontiers, random_forests)]

X = pd.DataFrame({
    'Specialist': specialists,
    'Frontier': frontiers,
    'RandomForest': random_forests,
    'Min': mins,
    'Max': maxes,
})

# Convert y to a Series
y = pd.Series(prices)

# Train a Linear Regression
np.random.seed(42)

lr = LinearRegression()
lr.fit(X, y)

joblib.dump(lr, 'ensemble_model.pkl')