
# AutogenXT 🔍💼

AutogenXT is an intelligent resume, cover letter, and interview preparation tool powered by **Hugging Face Transformers**. It helps users rewrite their resumes, generate personalized cover letters, and practice interview Q&A — all via a simple API and Streamlit frontend.

---

## 🚀 Features

- ✅ **Resume Enhancer** – Improve your resume for a specific job.
- ✅ **Cover Letter Generator** – Get a personalized cover letter.
- ✅ **Interview Simulator** – Ask any question, get a smart reply.
- ✅ **Streamlit Frontend** – Easy interface for users to interact.

---

## 🗂️ Project Structure

```

AutogenXT/
│
├── app.py                   # FastAPI backend
├── frontend\_app.py          # Streamlit frontend
├── requirements.txt         # Required packages
├── .env                     # Environment variables
│
├── chains/
│   ├── resume\_chain.py      # Resume logic
│   ├── coverletter\_chain.py # Cover letter logic
│   └── interview\_chain.py   # Interview Q\&A logic

````

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/kuldeeppatel202/AutogenXT.git
cd AutogenXT
````

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a file named `.env` in the project root and add:

```
HF_HOME=~/.cache/huggingface
```

---

## ▶️ Run the Project

### Start FastAPI Backend

```bash
uvicorn app:app --reload
```

### Start Streamlit Frontend

In another terminal:

```bash
streamlit run frontend_app.py
```

---

## 📥 API Endpoints

| Method | Endpoint       | Description              |
| ------ | -------------- | ------------------------ |
| POST   | `/resume`      | Improves resume          |
| POST   | `/coverletter` | Generates cover letter   |
| POST   | `/interview`   | Simulates interview Q\&A |

---

## 🤖 Models Used

* [`distilgpt2`](https://huggingface.co/distilgpt2) – Text generation via Hugging Face

---


---

## 📄 License

MIT License © 2025 [Kuldeep Patel](https://github.com/kuldeeppatel202)

---
