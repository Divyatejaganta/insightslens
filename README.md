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

insightlens/
├── README.md
├── LICENSE
├── requirements.txt
├── .env.example
├── docker-compose.yml
├── Makefile
├── insightlens/
│   ├── app/
│   │   ├── api.py
│   │   └── core/
│   │       ├── config.py
│   │       ├── embeddings.py
│   │       ├── index.py
│   │       ├── log_parser.py
│   │       ├── anomaly.py
│   │       └── summarizer.py
│   └── ui/
│       ├── Home.py
│       └── pages/
│           ├── 1_🔍_Search_Logs.py
│           ├── 2_🧩_Clusters_&_Anomalies.py
│           └── 3_🗂️_Datasets.py
└── data/
    └── sample_logs/
        ├── app_json.log
        ├── apache_access.log
        └── syslog_sample.log
