# Career Intelligence System

A data-driven career intelligence system that analyzes resume evidence against a target career and provides career readiness insights, skill gaps, learning priorities, and a personalized learning roadmap.

## 🚀 Live Demo

[Open the Live Demo](https://coolkarni-career-intelligence-system.streamlit.app/)

## 🎯 Problem

A resume can show what a candidate has done, but it does not always answer important career questions:

- How ready am I for a specific career?
- Which required skills do I already have?
- Which skills am I missing?
- Which gaps should I prioritize?
- What should I learn next?

## 💡 Solution

Career Intelligence System takes a resume and a target career and transforms them into a structured career analysis.

The system evaluates:

- Technical skill readiness
- Core skill evidence
- Knowledge coverage
- Market relevance
- Matched and missing skills
- Learning priorities
- Learning recommendations
- Career learning roadmap

## ✨ Features

### 📄 Resume Analysis

Upload a PDF resume and extract its textual content for analysis.

### 🧠 Technical Skill Detection

Detect technical skills from the resume using a curated skill vocabulary.

### ✅ Human Skill Validation

Review detected skills before they are used for technical career analysis.

### 🔎 Career Search

Search for careers using career names, aliases, skills, or technologies and select from relevant career suggestions.

### 📊 Career Readiness Analysis

Calculate an overall career readiness score using multiple analysis dimensions:

- Technical Skills
- Core Skills
- Knowledge
- Market Relevance

### 🎯 Skill Gap Analysis

Compare confirmed resume skills with the technical requirements of the selected career to identify:

- Matched skills
- Missing skills

### 📈 Market Relevance

Analyze relevant O*NET technology signals using career-specific market mappings.

### 📚 Learning Priorities

Identify and prioritize skill gaps that are relevant to the selected career.

### 💡 Learning Recommendations

Generate learning recommendations and project ideas for identified skill gaps.

### 🗺️ Career Learning Roadmap

Organize recommended learning into progressive foundation, intermediate, and advanced stages.

## 🔍 How It Works

```text
Resume PDF
    ↓
Text Extraction
    ↓
Text Cleaning
    ↓
Technical Skill Extraction
    ↓
Human Skill Validation
    ↓
Career Selection / Search
    ↓
Career Requirements + O*NET Data
    ↓
Career Intelligence Analysis
    ↓
┌──────────────────────────────┐
│ Technical Skill Analysis     │
│ Core Skill Evidence          │
│ Knowledge Coverage           │
│ Market Relevance             │
└──────────────┬───────────────┘
               ↓
      Career Readiness Score
               ↓
      Skill Gap Analysis
               ↓
       Learning Priorities
               ↓
   Learning Recommendations
               ↓
      Career Learning Roadmap
```

## 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │   Resume PDF    │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Resume Pipeline │
                    │                 │
                    │ Text Extraction │
                    │ Text Cleaning   │
                    │ Skill Detection │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Career Selection│
                    │   / Search      │
                    └────────┬────────┘
                             ↓
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
       Technical Data   O*NET Data    Career Mapping
              │              │              │
              └──────────────┼──────────────┘
                             ↓
                 ┌─────────────────────┐
                 │ Intelligence Engine │
                 ├─────────────────────┤
                 │ Technical Score     │
                 │ Core Skill Score    │
                 │ Knowledge Score     │
                 │ Market Relevance    │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Career Readiness    │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Skill Gaps          │
                 │ Priorities          │
                 │ Recommendations     │
                 │ Roadmap             │
                 └─────────────────────┘
```

## 🧮 Career Readiness Model

The overall readiness score combines four dimensions:

```text
Technical Skills       → 40%
Core Skills            → 20%
Knowledge              → 25%
Market Relevance       → 15%
```

The resulting score is an analytical indicator of how closely the available resume evidence matches the selected career profile.

It should not be interpreted as a hiring probability or guarantee of employment.

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- PyMuPDF
- Plotly
- spaCy
- NLTK
- O*NET data

## 📁 Project Structure

```text
CareerIntelligence/
│
├── app/
│   ├── streamlit_app.py
│   └── utils/
│       ├── pdf_reader.py
│       ├── text_cleaner.py
│       ├── skill_extractor.py
│       ├── skill_gap.py
│       ├── job_matcher.py
│       ├── readiness_score.py
│       ├── skill_normalizer.py
│       ├── onet_loader.py
│       ├── career_scores.py
│       ├── skill_priority.py
│       ├── learning_recommender.py
│       ├── roadmap_builder.py
│       ├── career_requirements.py
│       ├── technical_requirements.py
│       ├── career_profile.py
│       ├── career_search.py
│       ├── career_catalog.py
│       └── ...
│
├── data/
│   ├── skills.csv
│   ├── job_requirements.csv
│   ├── learning_resources.csv
│   └── onet/
│
├── models/
├── scripts/
├── tests/
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/DhruvCoolkarni/career-intelligence-system.git
cd career-intelligence-system
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\activate
```

Install the project dependencies:

```powershell
pip install -r requirements.txt
```

## ▶️ Run Locally

Start the Streamlit application:

```powershell
streamlit run app/streamlit_app.py
```

The application will then be available through the local Streamlit address shown in the terminal.

## 🧪 Testing

The project includes automated tests covering:

- Core functionality
- Career scoring
- Skill extraction
- Skill normalization
- Career search
- Intelligence pipeline
- Career-specific market relevance

Current test result:

```text
21 passed
```

Run the complete test suite with:

```powershell
pytest -q
```

## 📊 Example Analysis

The system produces a multi-dimensional career analysis containing:

```text
Technical Skill Readiness
Core Skill Evidence
Knowledge Coverage
Market Relevance
Overall Career Readiness
Matched Skills
Missing Skills
Learning Priorities
Learning Recommendations
Career Roadmap
```

Users can also review detected resume skills before those skills are used for technical career analysis.

## ⚠️ Limitations

- Resume skill detection depends on the current curated skill vocabulary.
- Career technical requirements are based on project-curated requirements.
- O*NET data provides occupational and technology signals but does not represent every employer's exact hiring requirements.
- Market relevance mappings are project-defined interpretations of relevant O*NET technology signals.
- Resume evidence does not guarantee actual proficiency.
- The readiness score is an analytical indicator and not a hiring probability.
- The system does not replace professional career counseling or employer-specific evaluation.
- Learning recommendations depend on the resources currently available in the project dataset.

## 🔮 Future Improvements

- Expand the skill ontology
- Improve semantic skill matching
- Improve resume evidence extraction
- Add more career profiles
- Integrate real-time labor-market data
- Improve learning-resource recommendations
- Add stronger NLP-based resume understanding
- Add job-description analysis
- Continuously update market-skill signals
- Develop more advanced career recommendation models

## 📄 License

This project is licensed under the MIT License.

Copyright © 2026 Dhruv Kulkarni.

See the `LICENSE` file for the complete license text.

## 👨‍💻 Author

**Dhruv Kulkarni**

B.Tech AI & Data Science

Career Intelligence System — 2026