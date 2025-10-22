# insightslens

**Convert chaos into clarity:** Ingest logs, detect anomalies, cluster incidents, and get LLM summaries.

**Tagline:**  
*Convert chaos into clarity — one log file at a time.*

---

**Stack:**  
- Python  
- OpenAI API  
- LangChain  
- FastAPI  
- Streamlit

---

## Concept

An LLM-driven observability tool that ingests application or server logs, clusters incidents, and generates intelligent summaries, anomaly trends, and root-cause hypotheses using embeddings and GPT reasoning.

---

## Why it’s awesome

- Real-world DevOps/Support use case (high employer relevance).
- Integrates NLP + anomaly detection.
- Deployable locally with Streamlit and Qdrant/OpenSearch.


##How to Run it
How to run locally (quick)
	1.	python3 -m venv .venv && source .venv/bin/activate
	2.	pip install -r requirements.txt
	3.	(Optional) cp .env.example .env and set OPENAI_API_KEY for best results.
	4.	Start API: uvicorn insightlens.app.api:app --reload
	5.	Start UI: streamlit run insightlens/ui/Home.py
	6.	Ingest samples: make ingest

Or with Docker:
docker compose up


What you get
	•	FastAPI backend: /ingest, /search, /summarize
	•	Streamlit UI (Home + Search + Clusters/Anomalies + Datasets)
	•	FAISS vector store with metadata parquet
	•	OpenAI-powered embeddings & summaries (with an offline fallback so it still works without a key)
	•	Sample logs (JSON app, Apache access, Syslog)
