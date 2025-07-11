# RAG Versions for NL to PromQL Conversion

 This directory contains different versions of the RAG-based application for natural language to PromQL conversion. Each version explores a specific combination of components such as LLMs, embedding models, databases, retrievers, and prompts.

## Table of Versions (RAG)

| **Version** | **LLM**                  | **Database**                   | **Embedding Model** | **Retriever**                      | **Prompt Type**  | **Syntax Accuracy (%)** |
| ----------- | ------------------------ | ------------------------------ | ------------------- | ---------------------------------- | ---------------- | ----------------------- |
| `rag_v1`    | llama-3.1-8b-instant     | Chroma                         | all-MiniLM-L6-v2    | Similarity                         | -                | 79.57%                  |
| `rag_v2`    | llama-3.1-8b-instant     | Milvus Lite                    | BAAI/bge-m3         | Dense Retriever (Similarity-based) | Chain-of-Thought | 63.98%                  |
| `rag_v3`    | Mistral-7B-Instruct-v0.3 | Chroma                         | all-MiniLM-L6-v2    | Similarity                         | -                | 62.90%                  |
| `rag_v4`    | Mistral-7B-Instruct-v0.3 | Milvus Lite                    | BAAI/bge-m3         | Hybrid Retriever (Dense + Sparse)  | -                | 83.33%                  |
| `rag_v5`    | llama-3.1-8b-instant     | Milvus Lite                    | BAAI/bge-m3         | Hybrid Retriever (Dense + Sparse)  | Chain-of-Thought | 81.72%                  |
| `rag_v6`    | llama-3.1-8b-instant     | Milvus Lite (multi-collection) | BAAI/bge-m3         | Dense Retriever (Similarity-based) | Chain-of-Thought | 51.61%                  |
| `rag_v7`    | llama-3.1-8b-instant     | Milvus Lite (multi-collection) | BAAI/bge-m3         | Dense Retriever (Similarity-based) | -                | 58.60%, \*60.75%        |
| `rag_v8`    | llama-3.3-70b-versatile  | Milvus Lite (multi-collection) | BAAI/bge-m3         | Dense Retriever (Similarity-based) | -                | 73.12%, \*77.96%        |

_Note:_ The values marked with an asterisk (*60.75% and *77.96%) are the results after passing the query through the PromQL syntax correction chain.

---

## Table of Versions (Agentic RAG)

| **Version**      | **LLM**                 | **Database**                   | **Embedding Model** | **Retriever**    | **Tools Used**                                                                        |
| ---------------- | ----------------------- | ------------------------------ | ------------------- | ---------------- | ------------------------------------------------------------------------------------- |
| `agentic_rag`    | llama-3.1-8b-instant    | Chroma                         | all-MiniLM-L6-v2    | Hybrid Retriever | `csv_tool`, `docs_tool`, `metrics_tool`, `query_generation_tool`                      |
| `agentic_rag_v2` | llama-3.3-70b-versatile | Milvus Lite (multi-collection) | BAAI/bge-m3         | Hybrid Retriever | `docs_tool`, `metrics_tool`, `query_generation_tool`, `promql_syntax_correction_tool` |
