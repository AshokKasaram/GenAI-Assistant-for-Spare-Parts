import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration

# --- Load FAISS index ---
index_path = "index"
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)

# --- Load Flan-T5 Small for CPU ---
model_name = "google/flan-t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
llm = HuggingFacePipeline(pipeline=pipe)

# --- Setup Retrieval Q&A chain ---
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# --- Streamlit UI ---
st.set_page_config(page_title="Support Copilot", page_icon="🧠")
st.title("🧠 GenAI Support Assistant for Spare Parts")
st.markdown("Ask any support-related question based on your internal SOPs or policies.")

# Sample suggested questions
sample_questions = [
    "What is the standard delivery time for North America?",
    "How should I escalate if a spare part is delayed?",
    "What documents are needed to handle customs issues?",
    "What is the process to request spare parts for Tier-2 datacenters?"
]

# Dropdown for sample questions
st.markdown("### 💡 Suggested Questions")
selected_question = st.selectbox("Pick a question:", [""] + sample_questions)

# Manual input field
user_query = st.text_input("💬 Or enter your own question:")

# Final query: prioritize user input, fallback to dropdown
final_query = user_query or selected_question

# Answer logic
if final_query:
    with st.spinner("🤖 Thinking..."):
        response = qa_chain.run(final_query)
    st.success("✅ Answer:")
    st.write(response)

st.markdown("---")
st.caption("Built with LangChain, FAISS, Sentence Transformers, and Flan-T5")
