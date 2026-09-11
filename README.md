# IND422_Risk_Project

**Startup Risk & Opportunity Radar** — a simple MVP web app (student project for IND422)
that helps startups identify possible risks, opportunities, and next steps.

## What it does

1. You describe your company or project in a short form.
2. The app analyzes the description (using simple keyword matching against
   mock/demo data — no external AI calls) and shows a structured overview of:
   - **Risks**
   - **Opportunities**
   - **Suggested next steps**

This is an MVP: the "analysis" in `analysis.py` is a rule-based mock that can
later be replaced with a real model or a call to an AI API.

## Tech stack

- Python + [Flask](https://flask.palletsprojects.com/) for the web server
- Plain HTML/CSS (Jinja2 templates), no JS framework needed

## Running locally

```bash
# 1. Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Then open http://localhost:5000 in your browser.

## Project structure

```
app.py                 # Flask routes (/ and /analyze)
analysis.py             # Mock keyword-based risk/opportunity/next-step logic
templates/
  base.html             # Shared layout
  index.html            # Input form
  results.html          # Structured results overview
static/
  style.css             # Styling
requirements.txt
```
