# GenAI Support Assistant for Spare Parts

A lightweight **GenAI chatbot** using **RAG (Retrieval-Augmented Generation)** and an open-source **LLM (Flan-T5)** to answer internal SOP questions. Fully offline and built using free, open-source components — no API keys or cloud needed.

![LangChain](https://img.shields.io/badge/Built%20With-LangChain-blue)
![FAISS](https://img.shields.io/badge/Vector%20DB-FAISS-green)
![LLM](https://img.shields.io/badge/LLM-Flan--T5-red)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Use Case

Designed to help internal support teams quickly retrieve policy or SOP-related answers about spare parts logistics and processes using natural language.

---

## Features

- Natural language Q&A over your own documents
- Offline chatbot with **RAG** pipeline (FAISS + LLM)
- Uses open-source **Sentence Transformers + Flan-T5**
- Interactive UI built with **Streamlit**
- No paid APIs or cloud required

---

## Tech Stack

| Component             | Tool/Library                                      |
|-----------------------|---------------------------------------------------|
| RAG Pipeline          | LangChain                                         |
| Vector Indexing       | FAISS                                             |
| Embedding Model       | SentenceTransformers (`all-MiniLM-L6-v2`)        |
| LLM                   | Flan-T5 (`google/flan-t5-small`)                  |
| Interface             | Streamlit                                         |
| Dev Tools             | Python, Jupyter Notebook                          |

---

## Project Structure

```
genai-support-chatbot/
│
├── app.py                  # Streamlit chatbot UI
├── build_index.ipynb       # Jupyter notebook to build FAISS index
├── Data/                   # Internal SOP text files
├── index/                  # Saved FAISS vector store
└── README.md               # Project documentation
```

---

## Concepts Used

- Retrieval-Augmented Generation (RAG)
- Sentence Embeddings
- Semantic Search using FAISS
- Prompting + Text2Text Inference using Flan-T5
- Local deployment with Streamlit

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/genai-support-chatbot.git
cd genai-support-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:

```bash
pip install langchain streamlit faiss-cpu sentence-transformers transformers torch
```

### 3. Add your SOP documents

Place your `.txt` files inside the `Data/` folder.

### 4. Build the FAISS index

Run the notebook or script to embed your docs:

```bash
# Jupyter Notebook
build_index.ipynb

# Or script (if created)
python build_index.py
```

### 5. Launch the chatbot

```bash
streamlit run app.py
```

---

## Example Questions

- What is the standard delivery time for North America?
- How should I escalate a delayed spare part?
- What documents are needed for customs issues?
- How to request spare parts for Tier-2 datacenters?

---

## Why This Project?

This project showcases how to use **GenAI** and **RAG** for real business problems — by combining document search with an open-source LLM to answer user questions without paid APIs.

Perfect for:

- Internal Copilots for Support / HR / IT
- Knowledge Assistants for internal SOPs / FAQs
- Offline GenAI Prototypes for Enterprise

---

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [HuggingFace Transformers](https://huggingface.co)
- [Sentence-Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io)

---

_✨ Built with LangChain, FAISS, HuggingFace, and Streamlit ✨_
