import chromadb
import ollama

# Connect to vector database
client = chromadb.PersistentClient(path="./vector_store/chroma_db")
collection = client.get_collection(name="log_collection")


def analyze_logs(query):

    print("\nRetrieving relevant logs...\n")

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    retrieved_logs = results["documents"][0]
    context = "\n".join(retrieved_logs)

    print("Calling local LLM (Ollama)...\n")

    prompt = f"""
You are an expert log analysis assistant.

Analyze the following logs and provide:

- Root Cause Summary
- Severity Level (LOW, MEDIUM, HIGH)
- Recurring Issues (if any)
- Suggested Actions

Logs:
{context}

User Query:
{query}

Respond clearly in structured format.
"""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        print("\n==============================")
        print("      LLM LOG ANALYSIS REPORT")
        print("==============================\n")
        print(response["message"]["content"])
        print("\n==============================\n")

    except Exception as e:
        print("Error while calling Ollama:")
        print(e)


if __name__ == "__main__":
    user_query = input("Enter your query: ")
    analyze_logs(user_query)