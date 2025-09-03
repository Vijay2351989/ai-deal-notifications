import joblib
import chromadb
from sklearn.ensemble import RandomForestRegressor
import numpy as np

DB = "products_vectorstore"

client = chromadb.PersistentClient(path=DB)
collection = client.get_or_create_collection('products')

result = collection.get(include=['embeddings', 'documents', 'metadatas'])
vectors = np.array(result['embeddings'])
documents = result['documents']
prices = [metadata['price'] for metadata in result['metadatas']]

rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf_model.fit(vectors, prices)

joblib.dump(rf_model, 'random_forest_model.pkl')