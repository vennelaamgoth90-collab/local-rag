import fitz
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Read PDF
doc = fitz.open("data/sample.pdf")
text = ""

for page in doc:
    text += page.get_text()

# Create chunks
chunk_size = 500
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

print("Chunks:", len(chunks))

# Create embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings, dtype="float32"))

# Save files
faiss.write_index(index, "vectorstore/docs.index")

with open("vectorstore/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("✅ docs.index created")
print("✅ chunks.pkl created")

