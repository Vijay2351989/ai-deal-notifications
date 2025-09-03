import os
import chromadb
from datasets import load_dataset
from dotenv import load_dotenv
from items import Item
from huggingface_hub import login
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import json

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

client = chromadb.PersistentClient(path=DB)

# Check if the collection exists and delete it if it does
collection_name = "products"

# For old versions of Chroma, use this line instead of the subsequent one
existing_collection_names = [collection.name for collection in client.list_collections()]
# existing_collection_names = client.list_collections()

if collection_name in existing_collection_names:
    client.delete_collection(collection_name)
    print(f"Deleted existing collection: {collection_name}")

collection = client.create_collection(collection_name)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def description(item):
    text = item['text'].replace("How much does this cost to the nearest dollar?\n\n", "")
    return text.split("\n\nPrice is $")[0]


NUMBER_OF_DOCUMENTS = len(train)

# Uncomment if you'd rather not wait for the full 400,000
# NUMBER_OF_DOCUMENTS = 20000

for i in tqdm(range(0, NUMBER_OF_DOCUMENTS, 1000)):
    documents = [description(item) for item in train.select(range(i, i+1000))]
    vectors = model.encode(documents).astype(float).tolist()
    metadatas = [{"price": item['price']} for item in train.select(range(i, i+1000))]
    ids = [f"doc_{j}" for j in range(i, i+len(documents))]
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=vectors,
        metadatas=metadatas
    )