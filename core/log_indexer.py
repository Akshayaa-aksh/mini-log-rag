import chromadb

# Persistent client (new correct way)
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="log_collection"
)

# Read logs
with open("sample_logs.txt", "r") as file:
    logs = file.readlines()

logs = [log.strip() for log in logs if log.strip()]

# Add logs
for i, log in enumerate(logs):
    collection.add(
        documents=[log],
        ids=[f"log_{i}"]
    )

print("Logs successfully indexed into vector database.")