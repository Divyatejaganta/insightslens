# InsightsLens

**Convert chaos into clarity:** Ingest logs, detect anomalies, cluster incidents, and get LLM-powered summaries.

---

## Tagline

*Convert chaos into clarity — one log file at a time.*

---

## Technology Stack

- **Python**
- **OpenAI API**
- **LangChain**
- **FastAPI**
- **Streamlit**

---

## Concept

InsightsLens is an LLM-driven observability tool that ingests application or server logs, clusters incidents, and generates intelligent summaries, anomaly trends, and root-cause hypotheses leveraging embeddings and GPT refinement.

---

## Why InsightsLens?

- Real-world DevOps & Support use case — highly relevant for employers.
- Integrates NLP and anomaly detection for smarter incident management.
- Easily deployable locally with Streamlit and Qdrant/OpenSearch.

---

## Getting Started

### Quick Local Setup

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional)** Copy environment file and set `OPENAI_API_KEY` for best results:
   ```bash
   cp .env.example .env
   # Edit .env to add your OpenAI API key
   ```

4. **Start the FastAPI backend:**
   ```bash
   uvicorn insightlens.app.api:app --reload
   ```

5. **Start the Streamlit UI:**
   ```bash
   streamlit run insightlens/ui/Home.py
   ```

6. **Ingest sample logs:**
   ```bash
   make ingest
   ```

### Run with Docker

```bash
docker compose up
```

---

## Features

- **FastAPI backend:** `/ingest`, `/search`, `/summarize`
- **Streamlit UI:** Home, Search, Clusters/Anomalies, Datasets
- **FAISS vector store** with metadata stored as Parquet files
- **OpenAI-powered embeddings and summaries** (offline fallback available if no API key is provided)
- **Sample logs:** Includes JSON app logs, Apache access logs, and Syslog

---
