import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="./pdf_db"
)

collection = client.get_or_create_collection(
    name="pdf_collection"
)


def create_chunks(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunks.append(
            text[i:i + chunk_size]
        )

    return chunks


def store_pdf(text):

    chunks = create_chunks(text)

    for idx, chunk in enumerate(chunks):

        embedding = model.encode(chunk)

        collection.add(
            ids=[str(idx)],
            documents=[chunk],
            embeddings=[
                embedding.tolist()
            ]
        )


def retrieve_chunks(query):

    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=3
    )

    return results["documents"][0]