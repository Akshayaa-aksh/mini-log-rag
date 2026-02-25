# Mini Log Intelligence System (RAG-Based Log Analysis)

## 📌 Project Overview

This project implements a minimal but functional Retrieval-Augmented Generation (RAG)-based log analysis system.

The system processes application log files, converts them into embeddings, stores them in a vector database, and performs intelligent retrieval and structured analysis based on user queries.

The goal of this project is to simulate a simplified version of modern AI-powered log intelligence architectures used in production systems.

---

## 🎯 Objective

Build a CLI-based log analysis pipeline with the following flow:

Log File → Vector Embeddings → Vector Database → Retrieval → Agent Reasoning → Structured Output

No UI is implemented. All outputs are displayed in the terminal.

---

## 🏗️ Architecture

The system follows this architecture:

1. Log Ingestion  
   Sample logs are stored in `data/sample_logs.txt`.

2. Vector Indexing  
   - Logs are stored in ChromaDB (persistent vector database).
   - Each log entry is indexed as a vector representation.
   - Database is stored locally in `chroma_db/`.

3. Semantic Retrieval  
   - User query is embedded automatically by Chroma.
   - Top-K relevant logs are retrieved based on similarity search.

4. Agent-Based Analysis  
   A reasoning layer applies:
   - Error classification
   - Severity detection
   - Recurring issue detection
   - Root cause identification
   - Recommended action generation

5. Structured Report Output  
   Results are displayed in a formatted log analysis report.

---


## ⚙️ How to Run

### Step 1 — Install dependencies

### Step 2 — Index logs

This creates and stores vector embeddings in the local Chroma database.

### Step 3 — Run analyzer


Enter a query such as:

- Why is the system failing?
- Find recurring authentication issues
- Are there performance problems?

The system will generate a structured log analysis report.

---

## 🧠 Reasoning Logic

The agent layer applies rule-based reasoning:

- If error count > 3 → HIGH severity
- If error count > 1 → MEDIUM severity
- Detects recurring patterns:
  - Database timeout
  - Authentication failure
  - API rate limit issues
- Suggests targeted corrective actions

This simulates an intelligent log diagnostics engine.

---

## 📊 Example Output

The system produces a structured report including:

- Retrieved logs
- Root cause summary
- Severity level
- Recurring issue detection
- Recommended actions

---

## ⚠️ Limitations

This is a minimal implementation and has several limitations:

- No real-time streaming log ingestion
- No distributed scaling
- Basic rule-based reasoning (not LLM-powered summarization)
- Limited dataset size
- No alerting or monitoring integration
- No REST API or UI layer

---

## 🚀 Future Improvements

This project can be extended with:

- Real-time log ingestion (stream processing)
- REST API integration
- Alerting system for high-severity issues
- Dashboard visualization
- Docker containerization
- Production-grade monitoring

---

## 🧩 Key Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Vector similarity search
- Persistent vector database usage
- Rule-based agent reasoning
- Severity classification logic
- Structured system diagnostics

---

## 📌 Conclusion

This project demonstrates a foundational AI-powered log analysis system using semantic retrieval and rule-based reasoning. It provides a scalable base architecture that can be expanded into a full production-grade log intelligence platform.