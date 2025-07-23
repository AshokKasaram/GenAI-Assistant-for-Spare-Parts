# GenAI Assistant for Spare Parts

A lightweight **GenAI chatbot** built using **Retrieval-Augmented Generation (RAG)** and open-source **LLM (Flan-T5)** to answer domain-specific questions from internal SOP documents. Designed for full offline use — no paid APIs or cloud needed.

![LangChain](https://img.shields.io/badge/Built%20With-LangChain-blue)
![FAISS](https://img.shields.io/badge/Vector%20DB-FAISS-green)
![LLM](https://img.shields.io/badge/LLM-Flan--T5-red)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Use Case

This assistant helps internal support teams quickly find SOP-related answers — such as part delivery timelines, escalation paths, and required documents — from a private knowledge base.

---

## Features

- Ask natural language questions about spare parts SOPs  
- Combines **vector search + LLM** (RAG pipeline)  
- Powered by open-source models, runs fully **offline**
- Interactive chat interface via **Streamlit**
- **No API keys or cloud services** needed  
- Modular code — easy to adapt to any domain (HR, IT, Legal, etc.)

---

## 🛠 Tech Stack

| Component             | Tool/Library                |
|-----------------------|-----------------------------|
| RAG Orchestration     | LangChain                   |
| Vector Indexing       | FAISS                       |
| Embedding Model       | Sentence Transformers (`all-MiniLM-L6-v2`) |
| LLM                   | Flan-T5 (`google/flan-t5-small`) |
| UI                    | Streamlit                   |
| Model Backend         | PyTorch                     |
| Dev/Preprocessing     | Jupyter Notebook            |

---

## Folder Structure


