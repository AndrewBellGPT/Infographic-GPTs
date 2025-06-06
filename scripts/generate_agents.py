import textwrap

topics = [
    "astronomy","biology","chemistry","physics","geology","oceanography","meteorology","botany","zoology","ecology",
    "economics","sociology","psychology","anthropology","linguistics","history","politics","philosophy","literature","art",
    "music","film","mathematics","computer science","engineering","robotics","artificial intelligence","space exploration","environment","sustainability",
    "agriculture","health","medicine","nursing","sports","fitness","nutrition","travel","culture","languages",
    "architecture","design","photography","marketing","advertising","business","finance","entrepreneurship","ethics","law"
]

aspects = [
    "foundational concepts","research methods","data collection","analysis techniques","case studies",
    "historical background","ethical considerations","modern developments","interdisciplinary links","practical applications",
    "industry standards","policy perspectives","cultural impacts","future trends","educational resources",
    "career guidance","innovation strategies","risk assessment","community engagement","global outlook"
]

domains = [
    "wikipedia.org","nasa.gov","esa.int","npr.org","bbc.co.uk",
    "nytimes.com","nature.com","sciencedaily.com","reuters.com","arxiv.org"
]

def create_paragraph(topic, aspect, idx):
    search_terms = [
        f"{topic} {aspect}",
        f"{aspect} {topic} tips",
        f"{topic} {aspect} resources",
    ]
    search_call = (
        f"Search Call {idx}: search([" + ", ".join(f'\"{t}\"' for t in search_terms) + "], domains=[" + ", ".join(f'\"{d}\"' for d in domains) + "])"
    )
    return (
        f"Section {idx}: Advice on {aspect} in {topic}. Provide explanations and recommendations. "
        + search_call
    )


def generate_prompt(topic):
    text = ""
    for i in range(1, 21):
        aspect = aspects[(i - 1) % len(aspects)]
        text += create_paragraph(topic, aspect, i) + "\n\n"
    filler = (
        f"Additional advice: Continue expanding knowledge about {topic} through research, collaboration, and hands-on experience. "
    )
    while len(text) < 8000:
        text += filler
    return text[:8000]


def main():
    for idx, topic in enumerate(topics, start=1):
        prompt = generate_prompt(topic)
        with open(f"agents/agent{idx:02}.md", "w") as f:
            f.write(prompt)

if __name__ == "__main__":
    main()
