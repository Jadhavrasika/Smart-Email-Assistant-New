📬 Smart Email Assistant using ML, GenAI, and Agents
An end-to-end AI-powered assistant that classifies incoming emails, generates automatic responses using an open-source LLM, and escalates low-confidence queries for human review. Built using Python, Streamlit, Ollama (LLM), and Docker.

### STEPS:
- Step 1 Complete: Synthetic Dataset Created
Total Emails: 300 (100 for each category: HR, IT, Other)
Saved as: [`emails-N.csv`]

- Step 2 Complete: Email Classification Agent (ML)
Model Used: Random Forest (with TF-IDF)
Accuracy: `100%` on synthetic test data
Classification Report: Perfect precision, recall, and F1-score for all 3 categories
Confusion Matrix:

[[22, 0, 0], # HR
[ 0, 19, 0], # IT
[ 0, 0, 19]] # Other
Model Saved: [`model.pkl`]

- [`escalation_agent.py`]
  Logs low-confidence or
“Other” emails for review.
Next: Create `orchestrator.py` to manage the flow
Workflow:
1. Pass email to classifier.
2. If confidence ≥ 0.6 and category ≠ "Other"
3. Else → escalate.

- - Created Components:
1. ML Model: Trained Random Forest on synthetic 300-email dataset. \[✔ Accuracy: 100%]
2. Files Created:
[`emails.csv`]
[`model.pkl`]
[`email_classifier.py`]
[`response_generator.py`]
[`escalation_agent.py`]
3. Orchestrator (planned): Would control full workflow from email input → classification →
response/escalation. Code is ready to be written locally.

- Agentic Workflow:
  <img width="1184" height="1920" alt="image" src="https://github.com/user-attachments/assets/906b320f-e8be-4b3d-945e-a5d25ae60404" />

  - Folder Structure:
    smart-email-assistant/
├── app/
│   ├── agents/
│   │   ├── email_classifier.py
│   │   ├── response_generator.py / crewai_response_agent.py
│   │   └── escalation_agent.py
│   ├── orchestrator.py
│   └── streamlit_ui.py
├── data/
│   └── emails.csv
├── notebooks/
│   └── data_cleaning.ipynb
├── logs/
│   └── history.csv
├── models/
│   └── model.pkl
├── Dockerfile
├── pyproject.toml
├── poetry.lock
├── requirements.txt
└── README.md

