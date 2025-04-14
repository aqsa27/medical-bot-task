#import libraries
import pandas as pd
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer

#Step 2: Load the FAISS Index and Metadata

# File paths
INDEX_PATH = "embeddings/faiss_index.bin"
META_PATH = "embeddings/qa_metadata.pkl"

# Load the FAISS index
index = faiss.read_index(INDEX_PATH)

# Load the saved metadata (Q+A pairs)
with open(META_PATH, "rb") as f:
    metadata = pickle.load(f)

#Step 3: Load the Sentence Embedding Model
# Load the same sentence transformer model used during indexing
model = SentenceTransformer("all-MiniLM-L6-v2")

#Step 4: Add the Chat Loop
print("\n Medical Assistant Bot — Ask me anything about medical conditions!")
print("Type 'exit' or 'quit' to end the chat.\n")

while True:
    user_input = input("Please enter your question: ")
    if not user_input.strip():
        print("Bot: Please enter a valid medical question.\n")
        continue
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Take care and stay healthy!")
        break
    #turns the input question into a 384-dimensional vector and converts it to float32 format because FAISS only works with that data type
    user_embedding = model.encode([user_input]).astype("float32")
    # Search the FAISS index for the most similar Q+A
    D, I = index.search(user_embedding, k=1)  # Get top 1 match
    top_result_index = I[0][0]
    match = metadata[top_result_index]
    answer = match["answer"]
    print(f"\nBot: {answer}\n")