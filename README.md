# GenAI-Powered Natural Language to DSL Query Generator with Advanced RAG Pipeline

**Observability and data access with a production-grade pipeline that translates natural language into precise PromQL queries using cutting-edge Retrieval-Augmented Generation (RAG)**

## 🧠 Technical Highlights

- **Hybrid Dense & Sparse Retrieval:** Seamlessly fuses FAISS (dense vector search) and BM25 (sparse retrieval) for context retrieval, maximizing both recall and precision. Supports plug-and-play backends: Milvus, Elasticsearch, and OpenSearch.
- **Agentic RAG Architecture:** Implements agent-based reasoning for iterative query refinement, error correction, and self-improvement—enabling robust, explainable query generation.
- **Domain-Specific Language (DSL) Synthesis:** Converts ambiguous, open-ended user questions into syntactically and semantically correct PromQL queries, leveraging prompt engineering and context-aware LLMs.
- **Scalable, Modular Design:** Built for extensibility—swap out retrieval engines, LLMs, or DSL targets with minimal code changes. Ready for enterprise-scale deployments.
- **Comprehensive Evaluation Suite:** Includes automated benchmarking, real-world test cases, and performance metrics to ensure reliability and continuous improvement.



- **End-to-End RAG Pipeline:** Integrates document chunking, embedding, hybrid retrieval, and LLM-based synthesis in a single, reproducible workflow.
- **Observability-First:** Tailored for Prometheus and PromQL, but easily adaptable to other DSLs and monitoring platforms.
- **Research-Backed, Production-Ready:** Combines the latest advances in IR, NLP, and agentic AI with robust engineering practices—bridging the gap between academic innovation and real-world utility.
- **Explainability & Transparency:** Agentic reasoning and context tracing provide clear, auditable query generation steps—critical for enterprise adoption.
## 🚀 Deployment & Testing Workflow
This project documents the process of setting up a distributed system environment using a Kind (Kubernetes-in-Docker) cluster, integrating Prometheus for monitoring and the OpenTelemetry Demo for telemetry data, and developing a Python script (test_promql.py) to evaluate PromQL queries against the setup. The journey includes initial setup, troubleshooting, testing modifications, and a complete uninstallation to ensure a clean system state.
## 📂 Project Structure

- `rag/` – Core RAG pipelines, agentic workflows, and LLM orchestration
- `evaluation/` – Automated evaluation scripts, metrics, and test datasets
- `dataset/` – Real-world queries, metrics, and documentation for training and benchmarking

## 💻 Tech Stack

- **Python, Jupyter, PyTorch/TensorFlow**
- **FAISS, BM25, Milvus, Elasticsearch, OpenSearch**
- **State-of-the-art LLMs (Mistral, Gemini, etc.)**
- **Prometheus, PromQL, KIND, KUBERNETES**


