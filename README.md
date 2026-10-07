<<<<<<< HEAD
# 🚀 Career Copilot AI

An intelligent, production-ready AI career assistant built with **Python, Streamlit, and the Groq API**.

---

## ✨ Features

| Module | Description |
|---|---|
| 📄 Resume Analyzer | Upload PDF/DOCX, extract skills, ATS score, strengths & suggestions |
| 🎯 Job Matcher | Match resume to target roles, salary ranges, missing skills |
| 🧠 Skill Gap Analysis | Visual gap chart, priority learning order |
| 📚 Learning Roadmap | 30/90/180-day personalized roadmaps with resources |
| 🎤 Interview Coach | Question bank + live mock interview with scoring |
| ✉️ Cover Letter | AI-generated, ATS-friendly, PDF export |
| 📊 ATS Score | Deep ATS compatibility scan with quick fixes |
| 🏠 Dashboard | Radar chart, gauges, performance trends |
| ⚙️ Settings | API key, model selection, session management |

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit + Custom CSS (Glassmorphism dark theme)
- **AI:** Groq API — LLaMA 3.3 70B Versatile
- **Database:** SQLite (auth, sessions, interview logs)
- **PDF:** pdfplumber (read) + ReportLab (write)
- **Charts:** Plotly (radar, gauge, bar, pie, line)
- **Auth:** bcrypt password hashing

---

## ⚡ Quick Start

### 1. Clone & install

```bash
git clone <your-repo>
cd career_copilot_ai
pip install -r requirements.txt
```

### 2. Get your Groq API key

Visit [console.groq.com](https://console.groq.com) and create a free API key.

### 3. Run the app

```bash
streamlit run app.py
```

### 4. Login

- Create an account via the Sign Up tab
- Enter your Groq API key on the login screen
- Start analyzing!
=======
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,18&height=180&section=header&text=Career%20Copilot%20AI&fontSize=52&fontColor=ffffff&fontAlignY=38&animation=fadeIn" width="100%" alt="Career Copilot AI header"/>

<a href="https://github.com/your-username/career-copilot-ai">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=900&color=6366F1&center=true&vCenter=true&width=860&height=60&lines=Your+AI-Powered+Career+Mentor;Smart+Resume+Coach+%26+ATS+Analyzer;Interview+%26+Placement+Preparation+Assistant;Built+with+Python+%F0%9F%90%8D+and+AI+%F0%9F%9A%80" alt="Typing animation"/>
</a>

<br/><br/>

**Your AI-Powered Career Mentor, Resume Coach, and Placement Preparation Assistant.**

Build ATS-friendly resumes, master interviews, close skill gaps, and land your dream role, all in one intelligent Python-powered platform.

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-6366F1?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Version](https://img.shields.io/badge/Version-1.0.0-7C3AED?style=for-the-badge)](https://github.com/your-username/career-copilot-ai/releases)
[![Build](https://img.shields.io/github/actions/workflow/status/your-username/career-copilot-ai/ci.yml?style=for-the-badge&logo=githubactions&logoColor=white&color=3B82F6)](https://github.com/your-username/career-copilot-ai/actions)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-3B82F6?style=for-the-badge)](CONTRIBUTING.md)

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)](https://scikit-learn.org)
[![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=flat-square&logo=spacy&logoColor=white)](https://spacy.io)

<br/>

[🚀 **Live Demo**](https://careercopilot.ai) &nbsp;·&nbsp; [📖 **Docs**](https://docs.careercopilot.ai) &nbsp;·&nbsp; [🐛 **Report Bug**](https://github.com/your-username/career-copilot-ai/issues/new?labels=bug) &nbsp;·&nbsp; [💡 **Request Feature**](https://github.com/your-username/career-copilot-ai/issues/new?labels=enhancement)

</div>

---

## 📑 Table of Contents

- [🌟 Overview](#-overview)
- [🎯 Who It's For](#-whos-it-for)
- [✨ Core Features](#-core-features)
- [🏗️ Architecture](#️-architecture)
- [🧰 Tech Stack](#-tech-stack)
- [📸 Screenshots](#-screenshots)
- [📁 Project Structure](#-project-structure)
- [⚡ Installation Guide](#-installation-guide)
- [🔐 Environment Variables](#-environment-variables)
- [🗺️ Roadmap](#️-roadmap)
- [📈 GitHub Statistics](#-github-statistics)
- [🤝 Contributing](#-contributing)
- [❓ FAQ](#-faq)
- [📜 License](#-license)

---

## 🌟 Overview

**Career Copilot AI** is an intelligent career guidance platform for **students, job seekers, and professionals**. Built end-to-end in **Python**, it combines large language models, NLP, and machine learning to deliver personalized, actionable career support, from your first resume to your next promotion.

<div align="center">

| 📄 **Smarter Resumes** | 🧭 **Clear Roadmaps** | 🎤 **Interview Ready** | 📊 **Measurable Progress** |
|:---:|:---:|:---:|:---:|
| ATS scoring & AI rewrites | Personalized step-by-step paths | Mock interviews with feedback | Dashboards that track growth |

</div>

> 💡 *Career Copilot AI turns the overwhelming job-search process into a guided, data-driven journey.*

---

## 🎯 Who It's For

| Audience | What You Get |
|:---|:---|
| 🎓 **Students** | Early career direction, skill roadmaps, and internship discovery |
| 🌱 **Freshers** | ATS-ready resumes, interview practice, and job recommendations |
| 🏫 **Campus Placement Candidates** | DSA tracking, aptitude prep, and placement dashboards |
| 🔎 **Job Seekers** | Resume optimization, skill gap analysis, and tailored job matches |
| 💼 **Working Professionals** | Growth roadmaps, upskilling plans, and career pivots |

---

## ✨ Core Features

### 📄 Resume Intelligence

| Feature | Description |
|:---|:---|
| 🧠 **AI Resume Analyzer** | Deep analysis of structure, content quality, keywords, and impact |
| 🎯 **ATS Score Checker** | Instant ATS compatibility score against a target job description |
| ✍️ **Resume Improvement Suggestions** | Line-by-line AI rewrites with stronger action verbs and metrics |
| 🔍 **Skill Gap Analysis** | Compare your profile against role requirements and spot what's missing |

### 🧭 Career Guidance

| Feature | Description |
|:---|:---|
| 🗺️ **AI Career Roadmap Generator** | Personalized roadmaps based on goals, skills, and timeline |
| 📚 **Personalized Learning Plans** | Weekly study plans with curated resources and milestones |
| 💬 **Career Chatbot Assistant** | 24/7 AI mentor for career questions, advice, and planning |
| 💼 **Internship & Job Recommendations** | Smart matching engine based on skills, interests, and goals |

### 🎓 Placement Preparation

| Feature | Description |
|:---|:---|
| 🏆 **Placement Preparation Dashboard** | One command center for all placement activities |
| 👨‍💻 **DSA Learning Tracker** | Topic-wise progress, difficulty breakdown, and revision reminders |
| 🧮 **Aptitude Preparation Assistant** | Quant, logical, and verbal practice with adaptive difficulty |
| ❓ **Interview Question Generator** | Role-specific technical and HR questions on demand |
| 🎤 **Mock Interview System** | Simulated interviews with AI scoring and detailed feedback |

### 📊 Analytics

| Feature | Description |
|:---|:---|
| 📈 **Progress Analytics Dashboard** | Visualize streaks, scores, skill growth, and readiness over time |

<details>
<summary><b>🔬 See how the AI engine works</b></summary>
<br/>

- **LLM layer (OpenAI API):** Generates roadmaps, rewrites, interview questions, and chatbot responses.
- **NLP layer (spaCy):** Extracts skills, entities, and keywords from resumes and job descriptions.
- **ML layer (scikit-learn):** Powers ATS scoring (TF-IDF + cosine similarity), skill-gap matching, and job/internship ranking.
- **Personalization:** User history, goals, and performance continuously refine recommendations.

</details>

---

## 🏗️ Architecture

### 🔷 System Architecture

```mermaid
flowchart TB
    U(["👤 User"]) --> FE

    subgraph FE["🖥️ Frontend  ·  Streamlit"]
        UI["Dashboard & UI"]
        RB["Resume Tools"]
        MI["Mock Interview"]
        CH["Career Chatbot"]
    end

    FE -->|"HTTP / REST"| API

    subgraph BE["⚙️ Backend  ·  FastAPI (Python)"]
        API["API Gateway"]
        AUTH["Auth & Sessions"]
        RES["Resume Service"]
        CAR["Roadmap Service"]
        PRE["Placement Service"]
        REC["Recommendation Engine"]
    end

    subgraph AI["🤖 AI Layer"]
        LLM["OpenAI API"]
        NLP["spaCy NLP Pipeline"]
        ML["scikit-learn Models"]
    end

    DB[("🗄️ PostgreSQL")]

    API --> AUTH
    API --> RES
    API --> CAR
    API --> PRE
    API --> REC
    RES --> NLP
    RES --> LLM
    CAR --> LLM
    PRE --> LLM
    REC --> ML
    AUTH --> DB
    RES --> DB
    CAR --> DB
    PRE --> DB
    REC --> DB
```

### 🔶 Resume Analysis Flow

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant UI as Streamlit UI
    participant API as FastAPI
    participant NLP as spaCy Pipeline
    participant ML as ML Scoring
    participant LLM as OpenAI API
    participant DB as PostgreSQL

    User->>UI: Upload resume + target job
    UI->>API: POST /api/resumes/analyze
    API->>NLP: Parse text, skills, keywords
    NLP-->>API: Structured resume data
    API->>ML: Compute ATS score & skill gaps
    ML-->>API: Score + gap report
    API->>LLM: Generate improvement suggestions
    LLM-->>API: Personalized feedback
    API->>DB: Save analysis report
    API-->>UI: Score, gaps & suggestions
    UI-->>User: Interactive report
```

### 🔸 Data Model

```mermaid
erDiagram
    USERS ||--o{ RESUMES : uploads
    USERS ||--o{ ROADMAPS : follows
    USERS ||--o{ MOCK_INTERVIEWS : takes
    USERS ||--o{ DSA_PROGRESS : tracks
    USERS ||--o{ APPLICATIONS : submits
    RESUMES ||--o{ ANALYSES : generates
    JOBS ||--o{ APPLICATIONS : receives

    USERS {
        uuid id PK
        string name
        string email
        string target_role
    }
    RESUMES {
        uuid id PK
        uuid user_id FK
        text content
    }
    ANALYSES {
        uuid id PK
        int ats_score
        json skill_gaps
    }
    ROADMAPS {
        uuid id PK
        string goal
        json milestones
    }
```

---

## 🧰 Tech Stack

<div align="center">

| Layer | Technologies |
|:---:|:---|
| 🎨 **Frontend** | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?logo=plotly&logoColor=white) |
| ⚙️ **Backend** | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?logo=fastapi&logoColor=white) ![Pydantic](https://img.shields.io/badge/-Pydantic-E92063?logo=pydantic&logoColor=white) |
| 🗄️ **Database** | ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?logo=postgresql&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white) ![Alembic](https://img.shields.io/badge/-Alembic-6BA81E) |
| 🤖 **AI / ML** | ![OpenAI](https://img.shields.io/badge/-OpenAI_API-412991?logo=openai&logoColor=white) ![spaCy](https://img.shields.io/badge/-spaCy-09A3D5?logo=spacy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikitlearn&logoColor=white) ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white) |

</div>

---

## 📸 Screenshots

<div align="center">

| 🏠 Dashboard | 📄 Resume Analyzer |
|:---:|:---:|
| ![Dashboard](docs/screenshots/dashboard.png) | ![Resume Analyzer](docs/screenshots/resume-analyzer.png) |

| 🎯 ATS Score Report | 🗺️ Career Roadmap |
|:---:|:---:|
| ![ATS Score](docs/screenshots/ats-score.png) | ![Roadmap](docs/screenshots/roadmap.png) |

| 🎤 Mock Interview | 👨‍💻 DSA Tracker |
|:---:|:---:|
| ![Mock Interview](docs/screenshots/mock-interview.png) | ![DSA Tracker](docs/screenshots/dsa-tracker.png) |

| 💼 Job Recommendations | 📊 Analytics |
|:---:|:---:|
| ![Jobs](docs/screenshots/jobs.png) | ![Analytics](docs/screenshots/analytics.png) |

> 🖼️ *Replace the placeholder paths with your real screenshots in `docs/screenshots/`.*

</div>
>>>>>>> 4965c1566827cf22c44328ee0114cb3a7932c150

---

## 📁 Project Structure

<<<<<<< HEAD
```
career_copilot_ai/
├── app.py                    # Entry point, auth, routing
├── pages/
│   ├── dashboard.py          # Overview charts and metrics
│   ├── resume_analyzer.py    # PDF upload + AI analysis
│   ├── job_matcher.py        # Role compatibility scoring
│   ├── skill_gap.py          # Gap analysis with bar charts
│   ├── learning_roadmap.py   # AI roadmap generator (streaming)
│   ├── interview_coach.py    # Question bank + mock interview
│   ├── cover_letter.py       # Cover letter + PDF export
│   ├── ats_score.py          # ATS deep scan
│   └── settings.py           # API key, profile, data
├── utils/
│   ├── groq_client.py        # Groq API wrapper (stream + sync)
│   ├── pdf_parser.py         # PDF/DOCX text extraction
│   ├── resume_parser.py      # Structured resume extraction
│   ├── prompts.py            # All LLM prompt templates
│   ├── database.py           # SQLite models and queries
│   └── helpers.py            # CSS, UI components
├── database/                 # SQLite DB (auto-created)
├── reports/                  # Generated PDFs
└── requirements.txt
```

---

## 🔧 Configuration

Set these environment variables (optional — key can also be entered at login):

```bash
export GROQ_API_KEY="gsk_your_key_here"
```

Or create a `.env` file:
```
GROQ_API_KEY=gsk_your_key_here
```

---

## 📦 Dependencies

```
streamlit>=1.32.0
groq>=0.5.0
langchain>=0.1.0
pandas>=2.0.0
plotly>=5.18.0
pdfplumber>=0.10.0
python-docx>=1.1.0
reportlab>=4.1.0
SQLAlchemy>=2.0.0
bcrypt>=4.1.0
python-dotenv>=1.0.0
```

---

## 🎨 UI Design

- **Dark Glassmorphism** theme with purple/blue gradient
- Responsive sidebar navigation
- Animated progress bars and hover effects
- Plotly interactive charts (radar, gauge, bar, pie, line)
- Streaming AI responses for roadmap generation
=======
<details>
<summary><b>📂 Click to expand the project tree</b></summary>

```text
career-copilot-ai/
├── 📁 app/                            # FastAPI backend
│   ├── 📄 main.py                     # Application entry point
│   ├── 📁 api/
│   │   ├── 📄 deps.py                 # Shared dependencies (auth, db session)
│   │   └── 📁 routes/
│   │       ├── 📄 auth.py
│   │       ├── 📄 resume.py           # Analyzer, ATS checker, suggestions
│   │       ├── 📄 roadmap.py          # Career roadmap generator
│   │       ├── 📄 placement.py        # Dashboard, DSA, aptitude
│   │       ├── 📄 interview.py        # Question generator, mock interviews
│   │       ├── 📄 jobs.py             # Internship & job recommendations
│   │       └── 📄 chatbot.py          # Career assistant
│   ├── 📁 core/
│   │   ├── 📄 config.py               # Settings (pydantic-settings)
│   │   └── 📄 security.py             # JWT & password hashing
│   ├── 📁 db/
│   │   ├── 📄 base.py
│   │   ├── 📄 session.py
│   │   └── 📁 migrations/             # Alembic migrations
│   ├── 📁 models/                     # SQLAlchemy models
│   ├── 📁 schemas/                    # Pydantic schemas
│   ├── 📁 services/
│   │   ├── 📄 openai_service.py       # LLM integration
│   │   ├── 📄 resume_service.py
│   │   ├── 📄 roadmap_service.py
│   │   ├── 📄 interview_service.py
│   │   └── 📄 recommendation_service.py
│   └── 📁 ml/
│       ├── 📄 nlp_pipeline.py         # spaCy skill & keyword extraction
│       ├── 📄 ats_scorer.py           # TF-IDF + similarity scoring
│       └── 📄 skill_gap.py
│
├── 📁 frontend/                       # Streamlit UI
│   ├── 📄 Home.py
│   ├── 📁 pages/
│   │   ├── 📄 1_Resume_Analyzer.py
│   │   ├── 📄 2_Career_Roadmap.py
│   │   ├── 📄 3_Placement_Dashboard.py
│   │   ├── 📄 4_Mock_Interview.py
│   │   ├── 📄 5_Job_Recommendations.py
│   │   ├── 📄 6_Career_Chatbot.py
│   │   └── 📄 7_Analytics.py
│   ├── 📁 components/
│   └── 📄 api_client.py
│
├── 📁 tests/
├── 📁 docs/
│   └── 📁 screenshots/
├── 📄 .env.example
├── 📄 requirements.txt
├── 📄 alembic.ini
├── 📄 CONTRIBUTING.md
├── 📄 LICENSE
└── 📄 README.md
```

</details>

---

## ⚡ Installation Guide

### ✅ Prerequisites

| Requirement | Version |
|:---|:---|
| 🐍 Python | `3.10+` |
| 📦 pip | Latest |
| 🐘 PostgreSQL | `v14+` |
| 🔑 OpenAI API Key | [Get one here](https://platform.openai.com/api-keys) |

### 🚀 Quick Start

<details open>
<summary><b>1️⃣ Clone the repository</b></summary>

```bash
git clone https://github.com/your-username/career-copilot-ai.git
cd career-copilot-ai
```

</details>

<details open>
<summary><b>2️⃣ Create & activate a virtual environment</b></summary>

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

</details>

<details open>
<summary><b>3️⃣ Install dependencies</b></summary>

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

</details>

<details open>
<summary><b>4️⃣ Create the database</b></summary>

```bash
psql -U postgres -c "CREATE DATABASE career_copilot;"
```

</details>

<details open>
<summary><b>5️⃣ Configure environment variables</b></summary>

```bash
cp .env.example .env      # Windows: copy .env.example .env
```

Then edit `.env` with your values (see [Environment Variables](#-environment-variables)).

</details>

<details open>
<summary><b>6️⃣ Run database migrations</b></summary>

```bash
alembic upgrade head
```

</details>

<details open>
<summary><b>7️⃣ Start the backend (FastAPI)</b></summary>

```bash
uvicorn app.main:app --reload --port 8000
```

API docs available at **http://localhost:8000/docs** 📘

</details>

<details open>
<summary><b>8️⃣ Start the frontend (Streamlit)</b></summary>

Open a new terminal (with the virtual environment activated):

```bash
streamlit run frontend/Home.py
```

🎉 Open **http://localhost:8501** and start building your career!

</details>

<details>
<summary><b>🐳 Run with Docker (optional)</b></summary>

```bash
docker compose up --build
```

</details>

<details>
<summary><b>🧪 Useful commands</b></summary>

| Command | Description |
|:---|:---|
| `uvicorn app.main:app --reload` | Run the API in development mode |
| `streamlit run frontend/Home.py` | Run the Streamlit UI |
| `alembic revision --autogenerate -m "msg"` | Create a new migration |
| `alembic upgrade head` | Apply migrations |
| `pytest` | Run the test suite |
| `ruff check .` | Lint the codebase |
| `black .` | Format the codebase |

</details>

---

## 🔐 Environment Variables

<details open>
<summary><b>⚙️ <code>.env</code></b></summary>
<br/>

```env
# ── App ────────────────────────────────
APP_ENV=development
API_HOST=0.0.0.0
API_PORT=8000
API_URL=http://localhost:8000
FRONTEND_URL=http://localhost:8501

# ── Database ───────────────────────────
DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/career_copilot

# ── Authentication ─────────────────────
SECRET_KEY=your_super_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# ── AI ─────────────────────────────────
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini

# ── File Uploads ───────────────────────
MAX_FILE_SIZE_MB=5
```

</details>

| Variable | Required | Description |
|:---|:---:|:---|
| `DATABASE_URL` | ✅ | PostgreSQL connection string (SQLAlchemy format) |
| `SECRET_KEY` | ✅ | Secret used to sign JWT tokens |
| `OPENAI_API_KEY` | ✅ | OpenAI API key for AI features |
| `OPENAI_MODEL` | ➖ | Model used for generation |
| `API_URL` | ✅ | Backend URL used by the Streamlit client |
| `FRONTEND_URL` | ✅ | Allowed frontend origin (CORS) |
| `MAX_FILE_SIZE_MB` | ➖ | Maximum resume upload size |

> ⚠️ **Never commit your `.env` file.** Keep API keys and secrets private.

---

## 🗺️ Roadmap

<details open>
<summary><b>📍 Development Progress</b></summary>
<br/>

| Phase | Milestone | Progress | Status |
|:---:|:---|:---|:---:|
| **1** | 🔐 Authentication & User Profiles | `██████████` 100% | ✅ Done |
| **2** | 📄 AI Resume Analyzer & ATS Checker | `████████░░` 80% | 🚧 In Progress |
| **3** | 🗺️ Career Roadmap Generator | `███████░░░` 70% | 🚧 In Progress |
| **4** | 🏆 Placement Dashboard, DSA & Aptitude | `█████░░░░░` 50% | 🚧 In Progress |
| **5** | 🎤 Interview Generator & Mock Interviews | `████░░░░░░` 40% | 🚧 In Progress |
| **6** | 💼 Job & Internship Recommendations | `███░░░░░░░` 30% | 🛠️ Building |
| **7** | 📊 Advanced Analytics & Chatbot | `██░░░░░░░░` 20% | 🛠️ Building |
| **8** | 🌐 Production Web Frontend | `░░░░░░░░░░` 0% | 📅 Planned |
| **9** | 🏫 College & Recruiter Portals | `░░░░░░░░░░` 0% | 📅 Planned |

</details>

<details>
<summary><b>✅ Detailed checklist</b></summary>
<br/>

- [x] User authentication & profiles
- [x] Resume upload & parsing
- [ ] ATS score checker
- [ ] AI resume improvement suggestions
- [ ] Career roadmap generator
- [ ] DSA tracker & aptitude assistant
- [ ] Mock interview system with AI feedback
- [ ] Internship & job recommendation engine
- [ ] Voice-based mock interviews
- [ ] LinkedIn profile optimizer
- [ ] Multi-language support
- [ ] Docker & CI/CD pipeline

</details>

---

## 📈 GitHub Statistics

<div align="center">

<img src="https://img.shields.io/github/stars/your-username/career-copilot-ai?style=for-the-badge&logo=github&color=6366F1" alt="Stars"/>
<img src="https://img.shields.io/github/forks/your-username/career-copilot-ai?style=for-the-badge&logo=github&color=7C3AED" alt="Forks"/>
<img src="https://img.shields.io/github/issues/your-username/career-copilot-ai?style=for-the-badge&color=3B82F6" alt="Issues"/>
<img src="https://img.shields.io/github/issues-pr/your-username/career-copilot-ai?style=for-the-badge&color=8B5CF6" alt="PRs"/>
<img src="https://img.shields.io/github/last-commit/your-username/career-copilot-ai?style=for-the-badge&color=60A5FA" alt="Last commit"/>
<img src="https://img.shields.io/github/contributors/your-username/career-copilot-ai?style=for-the-badge&color=A78BFA" alt="Contributors"/>

<br/><br/>

<img height="170" src="https://github-readme-stats.vercel.app/api?username=your-username&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117" alt="GitHub stats"/>
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=your-username&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117" alt="Top languages"/>

<br/>

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/career-copilot-ai&type=Date)](https://star-history.com/#your-username/career-copilot-ai&Date)

</div>
>>>>>>> 4965c1566827cf22c44328ee0114cb3a7932c150

---

## 🤝 Contributing

<<<<<<< HEAD
PRs welcome! Add new pages under `pages/` and prompts under `utils/prompts.py`.

---

**Made with ❤️ using Groq's ultra-fast LLaMA 3.3 70B**
=======
Contributions are what make the open-source community thrive. Any contribution you make is **greatly appreciated**! 💜

<details open>
<summary><b>📋 Contribution workflow</b></summary>
<br/>

1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. 💻 **Make your changes** and add tests where applicable
4. 🧹 **Format & lint** your code
   ```bash
   black . && ruff check .
   ```
5. ✅ **Run tests**
   ```bash
   pytest
   ```
6. 📝 **Commit** using [Conventional Commits](https://www.conventionalcommits.org/)
   ```bash
   git commit -m "feat: add amazing feature"
   ```
7. 📤 **Push** and open a **Pull Request** describing your changes

</details>

<details>
<summary><b>📐 Guidelines</b></summary>
<br/>

- ✔️ Follow [PEP 8](https://peps.python.org/pep-0008/) and use type hints where possible
- ✔️ Format with `black` and lint with `ruff` before committing
- ✔️ Write clear commit messages and PR descriptions
- ✔️ Add or update tests for new functionality
- ✔️ Update documentation when behavior changes
- ✔️ Keep pull requests small and focused
- ✔️ Be respectful and inclusive in all discussions

</details>

<details>
<summary><b>🌱 Good first issues</b></summary>
<br/>

New here? Look for issues labeled [`good first issue`](https://github.com/your-username/career-copilot-ai/labels/good%20first%20issue) or [`help wanted`](https://github.com/your-username/career-copilot-ai/labels/help%20wanted).

</details>

<div align="center">

### 💖 Thanks to all contributors

<a href="https://github.com/your-username/career-copilot-ai/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=your-username/career-copilot-ai" alt="Contributors"/>
</a>

</div>

---

## ❓ FAQ

<details>
<summary><b>💰 Is Career Copilot AI free to use?</b></summary>
<br/>

The open-source code is free under the MIT license. If you self-host, you'll only pay for your own infrastructure and OpenAI API usage.

</details>

<details>
<summary><b>🎯 How is the ATS score calculated?</b></summary>
<br/>

The spaCy NLP pipeline extracts skills, keywords, and structure from your resume. scikit-learn then compares them against the target job description using TF-IDF and cosine similarity, combined with checks for formatting, section completeness, and impact language.

</details>

<details>
<summary><b>🔒 Is my resume data private?</b></summary>
<br/>

When self-hosting, your data is stored in your own PostgreSQL database and is only used to provide platform features. Review the OpenAI API data usage policy for details on AI processing.

</details>

<details>
<summary><b>🤖 Which AI models does it use?</b></summary>
<br/>

It uses the OpenAI API for generation (configurable via `OPENAI_MODEL`), combined with custom spaCy and scikit-learn components for parsing, scoring, and recommendations.

</details>

<details>
<summary><b>🐍 Which Python version is required?</b></summary>
<br/>

Python **3.10 or higher** is recommended.

</details>

<details>
<summary><b>🛠️ Can I use a different AI provider?</b></summary>
<br/>

Yes. The AI logic lives in `app/services/openai_service.py`, so you can swap in another provider by implementing the same interface.

</details>

<details>
<summary><b>🐞 How do I report a bug or request a feature?</b></summary>
<br/>

Open an [issue](https://github.com/your-username/career-copilot-ai/issues) with clear steps to reproduce (for bugs) or a description of the problem you want solved (for features).

</details>

---

## 📜 License

<details open>
<summary><b>MIT License</b></summary>
<br/>

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

```text
MIT License

Copyright (c) 2025 Career Copilot AI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

</details>

---

<div align="center">

### 🚀 **Your career journey starts here. Let Career Copilot AI be your co-pilot.**

⭐ **If this project helps you, please give it a star!** ⭐

<br/>

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-6366F1?style=for-the-badge)](https://github.com/your-username/career-copilot-ai)
[![Powered by OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,18&height=120&section=footer" width="100%" alt="footer"/>

</div>
>>>>>>> 4965c1566827cf22c44328ee0114cb3a7932c150
