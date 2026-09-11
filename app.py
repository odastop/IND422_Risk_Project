"""
Startup Risk & Opportunity Radar - MVP

A simple Flask web app where a user describes their startup/project and
receives a structured (mock) overview of risks, opportunities, and
suggested next steps.
"""
from flask import Flask, render_template, request

from analysis import analyze_description

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    description = request.form.get("description", "").strip()
    company_name = request.form.get("company_name", "").strip() or "Your company"

    if not description:
        return render_template(
            "index.html",
            error="Please describe your company or project before submitting.",
            company_name=company_name,
        )

    result = analyze_description(description)

    return render_template(
        "results.html",
        company_name=company_name,
        description=description,
        result=result,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
