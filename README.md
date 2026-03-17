# 🚀 AI Resume Ranking & Parsing System

## 📌 Overview

This project is an AI-powered Resume Ranking System designed to automate candidate screening based on a given Job Description (JD).

It simulates a real-world recruitment workflow where multiple resumes are analyzed, parsed, and ranked intelligently using NLP and scoring algorithms.

---

## 🎯 Key Features

✅ Upload multiple resumes (PDF/DOCX)
✅ Extract candidate details (Name, Email, Skills, Experience, etc.)
✅ Identify technical skills using keyword-based NLP
✅ Compare resumes with Job Description
✅ Rank candidates using a weighted scoring system
✅ Interactive dashboard with visual analytics
✅ Download ranked results as CSV

---

## 🧠 AI & System Design Explanation

### 🔍 Resume Parsing

Resumes are processed using:

* `pdfplumber` → for PDF extraction
* `python-docx` → for DOCX files
* Regex → for extracting structured data (email, phone, experience)

---

### 🧩 Skill Extraction

A predefined technical skill database is used:

* Python, Java, SQL, Machine Learning, React, AWS, etc.

The system scans resume text and matches keywords to identify skills.

---

### 📊 Job Description Matching

Two techniques are used:

1. **Keyword Matching**

   * Matches resume skills with JD requirements

2. **Cosine Similarity**

   * Uses `CountVectorizer` to compare resume text with JD
   * Measures semantic similarity

---

### 🏆 Ranking Algorithm

Each candidate is scored based on:

| Factor        | Weight |
| ------------- | ------ |
| Skills Match  | 50%    |
| JD Similarity | 20%    |
| Experience    | 20%    |
| Education     | 5%     |
| Location      | 5%     |

Final Score Formula:

```
Score = (Skill Match × 50) + (Similarity × 20) + (Experience × 20) + (Education × 5) + (Location × 5)
```

---

### 📈 Dashboard & Visualization

The system provides:

* KPI Metrics (Total resumes, Top score, Avg score)
* Candidate leaderboard
* Top 3 candidates highlight
* Score distribution chart
* Experience vs Score analysis
* Skill frequency visualization

---

## 🛠️ Tech Stack

| Category         | Tools                   |
| ---------------- | ----------------------- |
| Frontend         | Streamlit               |
| NLP & Processing | spaCy, Regex            |
| File Parsing     | pdfplumber, python-docx |
| Data Handling    | Pandas                  |
| Similarity       | Scikit-learn            |
| Visualization    | Plotly                  |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone <your-repo-link>
cd AI-Resume-Ranking-System
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Install NLP Model

```
python -m spacy download en_core_web_sm
```

---

### 5️⃣ Run the Application

```
streamlit run app.py
```

---

### 6️⃣ Open in Browser

```
http://localhost:8501
```

---

## 📂 Project Structure

```
AI-Resume-Ranking-System/
│
├── app.py              # Main Streamlit dashboard
├── parser.py           # Resume parsing logic
├── skills.py           # Skill extraction
├── ranking.py          # Scoring & ranking algorithm
├── utils.py            # Helper functions
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

## 🧪 How to Use

1. Enter a Job Description
2. Upload multiple resumes (PDF/DOCX)
3. System processes resumes
4. View ranked candidates
5. Analyze insights using dashboard
6. Download results

---

## 📸 Demo

<img width="1919" height="993" alt="image" src="https://github.com/user-attachments/assets/9bb88482-26c4-4ecf-848c-ad9294568ee3" />
<img width="1919" height="1000" alt="image" src="https://github.com/user-attachments/assets/606f35d2-4e6e-4125-983f-88beabaeb3bb" />
<img width="1918" height="992" alt="image" src="https://github.com/user-attachments/assets/f9710eec-6354-4a35-a104-748a5e35e00a" />
<img width="1916" height="992" alt="image" src="https://github.com/user-attachments/assets/12eabb9b-cae5-468c-b0bb-b6186431a9a1" />


Example:

* Upload resumes
* Dashboard view
* Ranking results

---

## 💡 Key Highlights

✔ Clean and modern UI (SaaS-style dashboard)
✔ Scalable for multiple resumes (50–100)
✔ Real-world recruitment simulation
✔ Efficient and interpretable ranking logic
✔ No external APIs used (as per requirements)

---

## 🚀 Future Improvements

* Advanced NLP using Named Entity Recognition (NER)
* Semantic skill matching using embeddings
* Resume classification (role-based filtering)
* Integration with real ATS systems
* User authentication & multi-user support

---

## 👨‍💻 Author

**Hardik Sharma**
B.Tech IT | Data Analytics & AI Enthusiast

---

## 📌 Conclusion

This project demonstrates how AI and NLP can significantly improve recruitment efficiency by automating resume screening and ranking.

It reflects strong skills in:

* Problem solving
* System design
* Data processing
* UI/UX development

---

