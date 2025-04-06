# 🎵 Song Recommendation System Based on Mood

A powerful AI-driven system that recommends songs based on user mood. Built using:

- 🧠 Gemini API (LLM)
- 📊 Traditional ML fallback (TF-IDF + Cosine Similarity + Logistic Regression)
- 🎙️ Voice input (Speech Recognition)
- 💻 Streamlit frontend with chatbot-style UI + song thumbnails
- ☁️ Deployed via Render/Streamlit Cloud

---

## 📌 Features

- Detect mood from user's natural language input or voice
- Recommend songs based on mood
- Gemini API (LLM) for mood understanding and fallback ML if API fails
- Clean and modern chatbot-style Streamlit frontend
- Shows song thumbnails using image URLs
- Train ML model on Google Colab, use in VS Code locally

---

## 🧠 Tech Stack

| Layer        | Tech                                       |
|--------------|--------------------------------------------|
| Frontend     | Streamlit, HTML/CSS, Chatbot UI, Thumbnails |
| Backend      | Flask (or FastAPI), Python                  |
| ML Model     | TF-IDF, Cosine Similarity, Logistic Regression |
| LLM API      | Gemini Pro API (via Google Generative AI)  |
| Voice Input  | SpeechRecognition, PyAudio, pyaudio-wheel  |
| Deployment   | Render / Streamlit Cloud                    |

---

## 🗂️ Folder Structure

```bash
song_recommendation_system/
├── venv/                        # Python Virtual Environment
├── backend/
│   ├── app.py                   # Flask/FastAPI backend
│   ├── model/
│   │   ├── mood_classifier.pkl
│   │   ├── tfidf_vectorizer.pkl
│   │   └── song_data.csv
│   ├── utils/
│   │   └── fallback.py
│   └── gemini/
│       └── gemini_api.py
├── frontend/
│   ├── streamlit_app.py         # Chatbot frontend
│   ├── style.css
│   └── assets/
│       └── thumbnails/          # Song/Book images
├── colab_training/
│   ├── mood_classifier_training.ipynb
│   └── cleaned_dataset.csv
├── requirements.txt
└── README.md
