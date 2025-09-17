import argparse
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader

# init chroma
chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./chroma_store"))
collection = chroma_client.get_or_create_collection("docs")

# embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def index_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    chunks = [text[i:i+500] for i in range(0, len(text), 450)]
    embeddings = model.encode(chunks).tolist()
    collection.add(documents=chunks, embeddings=embeddings, ids=[f"chunk_{i}" for i in range(len(chunks))])
    chroma_client.persist()
    print(f"Indexed {len(chunks)} chunks from {path}")

def query(q):
    q_emb = model.encode([q]).tolist()
    results = collection.query(query_embeddings=q_emb, n_results=3)
    for doc in results["documents"][0]:
        print("-", doc)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["index", "query"])
    parser.add_argument("--file", help="Path to PDF")
    parser.add_argument("--q", help="Query text")
    args = parser.parse_args()

    if args.mode == "index" and args.file:
        index_pdf(args.file)
    elif args.mode == "query" and args.q:
        query(args.q)
