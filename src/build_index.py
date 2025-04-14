import pandas as pd
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from tqdm import tqdm


#Path 

DATA_PATH = "data/mle_screening_dataset.csv"
INDEX_PATH = "embeddings/faiss_index.bin"
META_PATH = "embeddings/qa_metadata.pkl"

#Load data
df = pd.read_csv(DATA_PATH)
#Drop any row that has eiother a missing question or answer, we do not
#have any embeddings or index empty questions or return missing answers
df.dropna(subset=["question", "answer"], inplace=True)
#remove any leading and trailing spaces
df["question"] = df["question"].str.strip()
df["answer"] = df["answer"].str.strip()

#Load pretrained sentence embedding model from the sentence-transformers library.
model = SentenceTransformer('all-MiniLM-L6-v2')

# Combine question and answer for better embedding context
print(" Combining questions and answers for richer embeddings...")
combined_text = df.apply(lambda row: f"Q: {row['question']} A: {row['answer']}", axis=1)

# Generate embeddings
print(" Generating embeddings for Q+A pairs...")
embeddings = model.encode(combined_text.tolist(), show_progress_bar=True)

embeddings = embeddings.astype("float32")

#Build FAISS index
print("creating FAISS index")
#create a new flast FAISS index that uses L2 distance to measure similarity between vectors
#Why L2? It’s a standard way to compare vectors. Lower L2 = more similar.
index = faiss.IndexFlatL2(embeddings.shape[1])  # ✅ correct
#adds all your vector embeddings to the FAISS index
index.add(embeddings)

#save FAISS index to disk
faiss.write_index(index, INDEX_PATH)

metadata = df[["question", "answer"]].to_dict(orient="records")

with open(META_PATH, "wb") as f:
    pickle.dump(metadata, f)

print("FAISS index and metadata saved to /embeddings")