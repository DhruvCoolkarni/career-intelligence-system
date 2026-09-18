# Career Intelligence System

A data-driven career intelligence system that analyzes resume evidence against a target career and provides career readiness insights, skill gaps, learning priorities, and a personalized learning roadmap.

## 🚀 Live Demo

https://coolkarni-career-intelligence-system.streamlit.app/

## 🎯 Problem

A resume can show what a candidate has done, but it does not always answer important career questions:

- How ready am I for a specific career?
- Which required skills do I already have?
- What skills am I missing?
- Which gaps should I prioritize?
- What should I learn next?

## 💡 Solution

Career Intelligence System takes a resume and a target career and transforms them into a structured career analysis.

The system evaluates:

- Technical skill readiness
- Core skill evidence
- Knowledge coverage
- Market relevance
- Missing skills
- Learning priorities
- Learning recommendations
- Career learning roadmap

## ✨ Features

### Resume Analysis
Upload a PDF resume and extract its textual content.

### Technical Skill Detection
Detect technical skills from the resume using a curated skill dataset.

### Human Skill Validation
Review detected skills before they are used for technical scoring.

### Career Readiness Analysis
Calculate an overall readiness score using multiple analysis dimensions.

### Skill Gap Analysis
Identify matched and missing skills for the selected career.

### Market Relevance
Analyze selected skills against relevant O*NET technology signals.

### Learning Priorities
Prioritize missing skills using career requirements and available O*NET signals.

### Personalized Learning Recommendations
Generate learning paths and project ideas for identified gaps.

### Career Learning Roadmap
Organize recommended learning into foundation, intermediate, and advanced phases.

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
Career Requirements
    ↓
Career Intelligence Analysis
    ↓
Skill Gap & Priorities
    ↓
Learning Recommendations
    ↓
Career Learning Roadmap