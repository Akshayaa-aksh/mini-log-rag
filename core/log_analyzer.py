import chromadb
from collections import Counter

# Connect to persistent database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(name="log_collection")


def analyze_logs(query):

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    retrieved_logs = results["documents"][0]

    error_logs = [log for log in retrieved_logs if "ERROR" in log]
    warning_logs = [log for log in retrieved_logs if "WARNING" in log]

    error_count = len(error_logs)

    # -------------------------------
    # Agent Reasoning Logic
    # -------------------------------

    # Severity Classification
    if error_count > 3:
        severity = "HIGH"
    elif error_count > 1:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    # Root Cause Detection
    root_causes = []

    if any("Database timeout" in log for log in error_logs):
        root_causes.append("Repeated database timeout failures detected.")

    if any("Authentication failure" in log for log in error_logs):
        root_causes.append("Multiple authentication failures observed.")

    if any("Memory usage spike" in log for log in error_logs):
        root_causes.append("Critical memory usage spike detected.")

    if any("API rate limit" in log for log in error_logs):
        root_causes.append("API rate limiting issues detected.")

    if not root_causes:
        root_causes.append("No critical root cause identified in top retrieved logs.")

    # Recurring Pattern Detection
    recurring_patterns = []

    if sum("Database timeout" in log for log in error_logs) > 1:
        recurring_patterns.append("Database timeout errors are recurring.")

    if sum("Authentication failure" in log for log in error_logs) > 1:
        recurring_patterns.append("Authentication failures are recurring.")

    if sum("API rate limit" in log for log in error_logs) > 1:
        recurring_patterns.append("API rate limit issues are recurring.")

    # Suggested Actions
    suggested_actions = []

    if "Database timeout" in " ".join(error_logs):
        suggested_actions.append("Check database connectivity and query optimization.")

    if "Authentication failure" in " ".join(error_logs):
        suggested_actions.append("Verify authentication service and user credential validation.")

    if "Memory usage spike" in " ".join(error_logs):
        suggested_actions.append("Monitor system memory and optimize resource allocation.")

    if "API rate limit" in " ".join(error_logs):
        suggested_actions.append("Review API rate limits and implement backoff strategy.")

    if not suggested_actions:
        suggested_actions.append("Perform general system diagnostics and log monitoring.")

    # -------------------------------
    # Structured Output
    # -------------------------------

    print("\n==============================")
    print("      LOG ANALYSIS REPORT")
    print("==============================\n")

    print("User Query:")
    print(f"{query}\n")

    print("Retrieved Logs:")
    for log in retrieved_logs:
        print(f"- {log}")
    print()

    print("Root Cause Summary:")
    for cause in root_causes:
        print(f"- {cause}")
    print()

    print(f"Severity Level: {severity}\n")

    if recurring_patterns:
        print("Recurring Issues:")
        for issue in recurring_patterns:
            print(f"- {issue}")
        print()

    print("Recommended Actions:")
    for action in suggested_actions:
        print(f"- {action}")

    print("\n==============================\n")


if __name__ == "__main__":
    user_query = input("Enter your query: ")
    analyze_logs(user_query)