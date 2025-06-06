import textwrap

roles = [
    "chief marketing officer",
    "marketing director",
    "marketing manager",
    "brand manager",
    "product marketing manager",
    "digital marketing manager",
    "content marketing manager",
    "social media manager",
    "seo specialist",
    "sem specialist",
    "email marketing manager",
    "marketing analyst",
    "marketing coordinator",
    "marketing assistant",
    "market research analyst",
    "public relations manager",
    "communications manager",
    "event coordinator",
    "creative director",
    "copywriter",
    "graphic designer",
    "web designer",
    "marketing operations manager",
    "marketing automation specialist",
    "growth hacker",
    "crm manager",
    "demand generation manager",
    "lead generation specialist",
    "advertising manager",
    "media buyer",
    "marketing strategist",
    "influencer marketing specialist",
    "affiliate marketing manager",
    "field marketing manager",
    "channel marketing manager",
    "partner marketing manager",
    "business development manager",
    "marketing project manager",
    "telemarketing representative",
    "sales enablement specialist",
    "marketing data scientist",
    "marketing consultant",
    "marketing technologist",
    "community manager",
    "sponsorship manager",
    "ecommerce manager",
    "brand ambassador",
    "creative producer",
    "content strategist",
    "ux designer",
]

aspects = [
    "strategic planning",
    "campaign management",
    "market research",
    "brand development",
    "digital initiatives",
    "content creation",
    "analytics",
    "team leadership",
    "vendor relations",
    "budget oversight",
    "industry standards",
    "policy perspectives",
    "cultural impacts",
    "future trends",
    "educational resources",
    "career guidance",
    "innovation strategies",
    "risk assessment",
    "community engagement",
    "global outlook",
]

domains = [
    "wikipedia.org",
    "forbes.com",
    "hbr.org",
    "npr.org",
    "bbc.co.uk",
    "nytimes.com",
    "marketingweek.com",
    "adweek.com",
    "reuters.com",
    "ama.org",
]

def create_paragraph(role, aspect, idx):
    search_terms = [
        f"{role} {aspect}",
        f"{aspect} {role} tips",
        f"{role} {aspect} resources",
    ]
    search_call = (
        f"Search Call {idx}: search([" + ", ".join(f'\"{t}\"' for t in search_terms) + "], domains=[" + ", ".join(f'\"{d}\"' for d in domains) + "])"
    )
    return (
        f"Section {idx}: Advice on {aspect} for the {role}. Provide explanations and recommendations. "
        + search_call
    )

def generate_prompt(role):
    text = ""
    for i in range(1, 21):
        aspect = aspects[(i - 1) % len(aspects)]
        text += create_paragraph(role, aspect, i) + "\n\n"
    filler = (
        f"Additional advice: Continue building expertise as the {role} through research, collaboration, and practical experience. "
    )
    while len(text) < 8000:
        text += filler
    return text[:8000]

def main():
    import os
    os.makedirs("marketing_agents", exist_ok=True)
    for idx, role in enumerate(roles, start=1):
        prompt = generate_prompt(role)
        with open(f"marketing_agents/agent{idx:02}.md", "w") as f:
            f.write(prompt)

if __name__ == "__main__":
    main()
