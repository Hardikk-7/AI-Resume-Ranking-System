import streamlit as st
import pandas as pd
import plotly.express as px

from parser import *
from skills import extract_skills
from ranking import *
from utils import highlight_matched_skills

st.set_page_config(page_title="AI Resume Ranker", layout="wide")

# ---------- PREMIUM CSS ----------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: #e2e8f0;
}

/* Hero Section */
.hero {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    padding: 30px;
    border-radius: 18px;
    margin-bottom: 25px;
    color: white;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 16px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    transition: 0.3s;
}
.card:hover {
    transform: scale(1.02);
}

/* KPI */
.kpi {
    text-align: center;
    padding: 20px;
    border-radius: 14px;
    background: linear-gradient(135deg, #1e293b, #020617);
}

/* Buttons */
.stButton button, .stDownloadButton button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 10px;
    border: none;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #020617;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <h1>🚀 AI Resume Ranking System</h1>
    <p>Analyze, Rank & Visualize Candidates Like a Pro</p>
</div>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("⚙️ Controls")
sort_option = st.sidebar.selectbox("Sort By", ["Score", "Experience"])
show_details = st.sidebar.toggle("Show Insights", True)

# ---------- INPUT ----------
col1, col2 = st.columns([2,1])

with col1:
    jd = st.text_area("📄 Job Description", height=180)

with col2:
    uploaded_files = st.file_uploader(
        "📂 Upload Resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

# ---------- PROCESS ----------
if uploaded_files and jd:

    results = []
    progress = st.progress(0)

    for i, file in enumerate(uploaded_files):
        progress.progress((i + 1) / len(uploaded_files))

        text = extract_text_from_pdf(file) if file.name.endswith(".pdf") else extract_text_from_docx(file)

        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        experience = extract_experience(text)
        education = extract_education(text)
        location = extract_location(text)
        skills = extract_skills(text)

        skill_score = calculate_skill_match(skills, jd)
        similarity = calculate_similarity(text, jd)
        final_score = calculate_final_score(skill_score, similarity, experience)

        results.append({
            "Name": name,
            "Skills": ", ".join(skills),
            "Experience": experience,
            "Score": round(final_score, 2),
            "Email": email,
            "Phone": phone,
            "Education": education,
            "Location": location
        })

    df = pd.DataFrame(results)

    if sort_option == "Score":
        df = df.sort_values(by="Score", ascending=False)
    else:
        df = df.sort_values(by="Experience", ascending=False)

    df.reset_index(drop=True, inplace=True)
    df.index += 1

    # ---------- KPI ----------
    st.markdown("## 📊 Overview")

    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div class='kpi'><h2>{len(df)}</h2><p>Resumes</p></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='kpi'><h2>{df['Score'].max()}</h2><p>Top Score</p></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='kpi'><h2>{round(df['Score'].mean(),2)}</h2><p>Average</p></div>", unsafe_allow_html=True)

    st.markdown("---")

    # ---------- TOP 3 ----------
    st.markdown("## 🥇 Top Candidates")

    top3 = df.head(3)

    cols = st.columns(3)
    for i, (_, row) in enumerate(top3.iterrows()):
        cols[i].markdown(f"""
        <div class="card">
            <h3>{row['Name']}</h3>
            <p>Score: {row['Score']}</p>
            <p>{row['Skills']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------- CHARTS ----------
    st.markdown("## 📈 Analytics")

    col1, col2 = st.columns(2)

    # Score chart
    fig1 = px.bar(df, x=df.index, y="Score", title="Score Distribution")
    col1.plotly_chart(fig1, use_container_width=True)

    # Experience chart
    fig2 = px.scatter(df, x="Experience", y="Score", title="Experience vs Score")
    col2.plotly_chart(fig2, use_container_width=True)

    # ---------- SKILLS CHART ----------
    all_skills = []
    for s in df["Skills"]:
        all_skills.extend(s.split(", "))

    skill_df = pd.Series(all_skills).value_counts().reset_index()
    skill_df.columns = ["Skill", "Count"]

    fig3 = px.bar(skill_df, x="Skill", y="Count", title="Skill Frequency")
    st.plotly_chart(fig3, use_container_width=True)

    # ---------- TABLE ----------
    st.markdown("## 🏆 Leaderboard")
    st.dataframe(df, use_container_width=True)

    # ---------- DETAILS ----------
    if show_details:
        st.markdown("## 📌 Candidate Insights")

        for i, row in df.iterrows():
            with st.expander(f"{row['Name']} (Score: {row['Score']})"):

                st.write(f"📧 {row['Email']}")
                st.write(f"📞 {row['Phone']}")
                st.write(f"🎓 {row['Education']}")
                st.write(f"📍 {row['Location']}")

                st.progress(min(row["Score"]/100,1))

                matched = highlight_matched_skills(
                    row["Skills"].split(", "), jd
                )

                st.success(f"Matched Skills: {', '.join(matched)}")

    st.success("✅ AI Analysis Complete!")