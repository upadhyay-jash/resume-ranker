AI-Powered Resume Ranker
This project is an intelligent recruitment tool designed to automate and streamline the initial screening process. It allows a user to upload a job description along with multiple resumes and leverages a Large Language Model (LLM) to score and rank each resume based on its suitability for the role.

The application, built with Streamlit, provides a clear and ranked list of candidates, saving recruiters significant time and effort.

🎯 Project Goal
The goal is to create an automated system that can intelligently parse and compare resumes against a specific job description. The application should:

Allow uploading one job description and multiple resume PDFs simultaneously.

Use an LLM to analyze the content of each resume in the context of the job requirements.

Generate a relevance score for each candidate.

Display a ranked list of candidates, making it easy to identify the top prospects.

🛠️ Tech Stack
Application Framework: Streamlit

LLM Provider: Azure Chat OpenAI

LLM Orchestration: LangChain

Core Language: Python

⚙️ System Workflow
The application uses an LLM to perform a sophisticated comparison that goes beyond simple keyword matching.

Input Upload: A user uploads a job description (as text or a file) and up to 10 resume PDFs via the Streamlit interface.

Content Extraction: The system programmatically extracts the text content from the job description and each of the uploaded resume files.

LLM-Powered Comparison: For each resume, the system constructs a detailed prompt. This prompt contains both the full job description and the full text of the resume.

Scoring and Justification: The prompt instructs the Azure Chat OpenAI model to act as a senior recruiter. The LLM is asked to:

Carefully compare the candidate's skills and experience against the job requirements.

Provide a suitability score (e.g., on a scale of 1-100).

Give a brief, one-sentence justification for the score.

Ranking and Display: The system gathers the scores for all resumes, sorts the candidates from highest to lowest score, and displays the final ranked list in a clean table format within the Streamlit app.

🏁 How to Run
Prerequisites
Python 3.8+

An Azure OpenAI API Key and endpoint

Installation & Execution
Clone the repository:

git clone https://github.com/upadhyay-jash/resume-ranker.git
cd resume-ranker

Install dependencies:

pip install -r requirements.txt

Set up environment variables:

Create a .env file in the root directory.

Add your Azure OpenAI credentials to the .env file:

AZURE_OPENAI_API_KEY="YOUR_API_KEY"
AZURE_OPENAI_ENDPOINT="YOUR_ENDPOINT"

Run the Streamlit app:

streamlit run app.py
