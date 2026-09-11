"""
Mock analysis logic for the Startup Risk & Opportunity Radar MVP.

This module does NOT use any external AI/API calls. It uses simple keyword
matching against a hand-written knowledge base to simulate what a smarter
analysis engine could return later. It is intentionally easy to read and
extend for a student project.
"""

# Each entry maps keywords (found in the user's description) to extra,
# domain-specific risks/opportunities/next steps that get added on top of
# the generic ones every submission receives.
KEYWORD_INSIGHTS = {
    "saas": {
        "risks": ["High customer churn if onboarding is not smooth",
                   "Subscription fatigue in a crowded SaaS market"],
        "opportunities": ["Recurring revenue enables predictable growth",
                           "Upsell/cross-sell potential via tiered pricing"],
        "next_steps": ["Define your ideal customer profile (ICP) clearly",
                        "Set up churn and retention tracking from day one"],
    },
    "app": {
        "risks": ["App store approval delays or policy changes",
                   "User acquisition cost can be high on mobile"],
        "opportunities": ["Viral growth loops through sharing features",
                           "Push notifications enable strong re-engagement"],
        "next_steps": ["Prototype the core user flow and test with 5-10 users",
                        "Plan for both iOS and Android from a budget perspective"],
    },
    "ai": {
        "risks": ["Model performance may not generalize to real users",
                   "Regulatory scrutiny around AI is increasing (e.g. EU AI Act)"],
        "opportunities": ["Automation can create strong cost advantages",
                           "AI differentiation can be a strong marketing story"],
        "next_steps": ["Document data sources and check for licensing issues",
                        "Define clear evaluation metrics for model quality"],
    },
    "fintech": {
        "risks": ["Financial regulation and licensing requirements",
                   "High trust bar required from users handling money"],
        "opportunities": ["Large addressable market in underserved segments",
                           "Partnerships with banks/PSPs can accelerate growth"],
        "next_steps": ["Consult a lawyer about licensing requirements early",
                        "Map out KYC/AML requirements for your target market"],
    },
    "health": {
        "risks": ["Strict regulatory approval processes (e.g. medical device rules)",
                   "Liability concerns around health-related claims"],
        "opportunities": ["Strong willingness to pay for proven health outcomes",
                           "Potential for partnerships with clinics or insurers"],
        "next_steps": ["Check whether your product classifies as a medical device",
                        "Talk to potential clinical partners for early validation"],
    },
    "hardware": {
        "risks": ["Manufacturing delays and supply chain disruptions",
                   "Higher upfront capital requirements than software"],
        "opportunities": ["Physical products can build strong brand loyalty",
                           "Potential for defensible IP via patents"],
        "next_steps": ["Build a low-cost prototype before committing to tooling",
                        "Identify at least two alternative suppliers per component"],
    },
    "ecommerce": {
        "risks": ["Thin margins and price competition from large platforms",
                   "Dependence on third-party marketplaces or ad platforms"],
        "opportunities": ["Direct-to-consumer relationship builds customer data",
                           "Niche positioning can command premium pricing"],
        "next_steps": ["Validate demand with a small pre-order or landing page test",
                        "Plan logistics and returns handling before scaling"],
    },
    "marketplace": {
        "risks": ["Chicken-and-egg problem balancing supply and demand",
                   "Risk of disintermediation once buyers/sellers connect directly"],
        "opportunities": ["Network effects can create a defensible moat",
                           "Take-rate model scales well with transaction volume"],
        "next_steps": ["Focus on one side of the marketplace first to seed liquidity",
                        "Define trust & safety mechanisms early (reviews, verification)"],
    },
    "sustainability": {
        "risks": ["Greenwashing accusations if claims are not substantiated",
                   "Impact metrics can be hard to measure and communicate"],
        "opportunities": ["Growing consumer and investor demand for sustainable options",
                           "Possible access to green grants or impact funding"],
        "next_steps": ["Define measurable sustainability KPIs early",
                        "Research relevant grants, subsidies or ESG-focused investors"],
    },
    "education": {
        "risks": ["Long sales cycles when selling to schools/institutions",
                   "Budget cycles can delay adoption by a full year"],
        "opportunities": ["Strong word-of-mouth potential among educators",
                           "Public funding programs may be available"],
        "next_steps": ["Pilot with a small number of classrooms or institutions",
                        "Research procurement processes for your target segment"],
    },
}

GENERIC_RISKS = [
    "Uncertain product-market fit before validating with real customers",
    "Limited runway/funding to reach key milestones",
    "Key-person dependency if critical knowledge sits with one founder",
    "Competitors with more resources entering the same space",
]

GENERIC_OPPORTUNITIES = [
    "Early-mover advantage if the market is validated quickly",
    "Opportunity to build a strong brand and community from the start",
    "Potential to attract talent excited about an early-stage mission",
]

GENERIC_NEXT_STEPS = [
    "Talk to 10-15 potential customers to validate the problem",
    "Define your minimum viable product (MVP) and target launch date",
    "Create a simple financial plan covering the next 12 months",
    "Identify your 2-3 biggest assumptions and design tests for them",
]


def analyze_description(description: str) -> dict:
    """Return a mock structured analysis for the given free-text description.

    This is a simple keyword-matching heuristic meant to simulate a more
    sophisticated (e.g. AI-based) analysis engine in a later iteration.
    """
    text = description.lower()

    risks = list(GENERIC_RISKS)
    opportunities = list(GENERIC_OPPORTUNITIES)
    next_steps = list(GENERIC_NEXT_STEPS)
    matched_topics = []

    for keyword, insights in KEYWORD_INSIGHTS.items():
        if keyword in text:
            matched_topics.append(keyword)
            risks.extend(insights["risks"])
            opportunities.extend(insights["opportunities"])
            next_steps.extend(insights["next_steps"])

    return {
        "matched_topics": matched_topics,
        "risks": risks,
        "opportunities": opportunities,
        "next_steps": next_steps,
    }
