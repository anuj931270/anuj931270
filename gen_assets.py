"""Generates assets/hero-neural.svg and assets/skills-cards.svg
Edit the CONFIG block, then run:  python gen_assets.py
"""
import random

# ================= CONFIG: EDIT THIS =================
NAME = "Anuj"
TITLE = "Data Scientist &amp; AI Engineer"
TAGLINE = "Building RAG and agentic AI systems that ship to production."

# Neural-network layers: (header, color, [skills])
LAYERS = [
    ("DATA",    "#22d3ee", ["SQL", "Pandas", "NumPy", "MySQL"]),
    ("ML / DL", "#a78bfa", ["XGBoost", "LSTM", "TensorFlow", "BERT"]),
    ("GEN AI",  "#f472b6", ["RAG", "LangChain", "OpenAI", "Pinecone"]),
    ("AGENTS",  "#fbbf24", ["LangGraph", "MCP", "Tool Calling"]),
    ("DEPLOY",  "#34d399", ["FastAPI", "Docker", "AWS", "Azure"]),
]

# Skill cards: (title, color, [chips])
SKILLS = [
    ("AGENTIC AI",       "#fbbf24", ["AI Agents", "LangGraph", "MCP Server", "Tool Calling", "Multi-Agent", "HITL"]),
    ("GEN AI / LLM",     "#f472b6", ["LLMs", "RAG", "LangChain", "OpenAI API", "Hugging Face", "Prompt Eng", "LangSmith"]),
    ("VECTOR DB",        "#22d3ee", ["Pinecone", "FAISS", "ChromaDB", "Semantic Search"]),
    ("DEEP LEARNING",    "#a78bfa", ["NLP", "Transformers", "BERT", "LSTM", "RNN", "CNN", "Word2Vec", "TensorFlow"]),
    ("MACHINE LEARNING", "#fb923c", ["XGBoost", "Random Forest", "AdaBoost", "SVM", "KNN", "K-Means", "Time Series"]),
    ("CLOUD / MLOPS",    "#34d399", ["AWS", "SageMaker", "Bedrock", "Azure ML", "GCP", "Docker", "Kubernetes", "CI/CD"]),
    ("BACKEND / DATA",   "#60a5fa", ["FastAPI", "Flask", "Python", "SQL", "Pandas", "NumPy", "MySQL", "MongoDB"]),
    ("AT A GLANCE",      "#e879f9", ["5+ years", "4 client projects", "Production AI"]),
]
# =====================================================

FONT = "font-family=\"'Courier New', Consolas, monospace\""


def hero():
    W, H = 900, 540
    random.seed(11)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    o.append('''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050b18"/><stop offset="1" stop-color="#0d1633"/></linearGradient>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#22d3ee"/><stop offset="0.5" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6"/></linearGradient>
<pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M36 0H0V36" fill="none" stroke="#1b2745" stroke-width="1" stroke-opacity="0.55"/></pattern>
<filter id="glow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>''')
    o.append(f'<rect width="{W}" height="{H}" rx="8" fill="url(#bg)"/><rect width="{W}" height="{H}" rx="8" fill="url(#grid)"/>')
    o.append(f'<text x="{W/2}" y="56" text-anchor="middle" fill="url(#tg)" font-size="34" font-weight="bold" {FONT}>{NAME}</text>')
    o.append(f'<text x="{W/2}" y="84" text-anchor="middle" fill="#9fb3c8" font-size="15" {FONT}>{TITLE}</text>')

    xs = [110 + i * 170 for i in range(len(LAYERS))]
    cy, gap = 292, 80
    pos = []  # per layer list of (x, y)
    for i, (_, _, items) in enumerate(LAYERS):
        n = len(items)
        pos.append([(xs[i], cy + (k - (n - 1) / 2) * gap) for k in range(n)])

    edges = []
    for i in range(len(LAYERS) - 1):
        col = LAYERS[i][1]
        for (x1, y1) in pos[i]:
            for (x2, y2) in pos[i + 1]:
                edges.append((x1, y1, x2, y2, col))
                o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-opacity="0.20" stroke-width="1"/>')

    for (x1, y1, x2, y2, col) in random.sample(edges, 30):  # flowing data pulses
        dur = random.uniform(2.2, 4.6)
        o.append(f'<circle r="3.2" fill="{col}" filter="url(#glow)"><animateMotion dur="{dur:.1f}s" repeatCount="indefinite" '
                 f'begin="-{random.uniform(0, 4):.1f}s" path="M{x1},{y1} L{x2},{y2}"/></circle>')

    for i, (head, col, items) in enumerate(LAYERS):
        x = xs[i]
        o.append(f'<rect x="{x-46}" y="108" width="92" height="24" rx="12" fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-opacity="0.7"/>')
        o.append(f'<text x="{x}" y="124" text-anchor="middle" fill="{col}" font-size="12" font-weight="bold" {FONT}>{head}</text>')
        for k, (nx, ny) in enumerate(pos[i]):
            d = 2.4 + (i + k) % 4 * 0.5
            o.append(f'<circle cx="{nx}" cy="{ny}" r="12" fill="#0a1225" stroke="{col}" stroke-width="2"/>')
            o.append(f'<circle cx="{nx}" cy="{ny}" r="5" fill="{col}" filter="url(#glow)"><animate attributeName="r" values="4;6.5;4" dur="{d:.1f}s" repeatCount="indefinite" begin="-{k*0.6:.1f}s"/></circle>')
            o.append(f'<text x="{nx}" y="{ny+31}" text-anchor="middle" fill="#e2e8f0" font-size="12" {FONT}>{items[k]}</text>')

    o.append(f'<text x="{W/2}" y="{H-26}" text-anchor="middle" fill="#7d8fa6" font-size="14" font-style="italic" {FONT}>{TAGLINE}</text>')
    o.append('</svg>')
    open("assets/hero-neural.svg", "w", encoding="utf-8").write("\n".join(o))


def skills():
    W, PAD, GAP, COLW = 900, 20, 20, 430
    CH, CG, HEAD, INNER = 26, 8, 40, COLW - 32
    cw = lambda t: len(t) * 7.4 + 22

    cards = []
    for title, col, chips in SKILLS:  # lay out chips with wrapping
        rows, cur, x = [], [], 0
        for c in chips:
            w = cw(c)
            if cur and x + w > INNER:
                rows.append(cur); cur, x = [], 0
            cur.append((c, w)); x += w + CG
        rows.append(cur)
        cards.append((title, col, rows, HEAD + len(rows) * (CH + CG) + 10))

    o_body, y = [], PAD
    for r in range(0, len(cards), 2):
        pair = cards[r:r + 2]
        h = max(c[3] for c in pair)
        for j, (title, col, rows, _) in enumerate(pair):
            x0 = PAD + j * (COLW + GAP)
            o_body.append(f'<rect x="{x0}" y="{y}" width="{COLW}" height="{h}" rx="12" fill="#0d1428" stroke="{col}" stroke-opacity="0.45"/>')
            o_body.append(f'<rect x="{x0}" y="{y}" width="{COLW}" height="4" rx="2" fill="{col}" fill-opacity="0.9"/>')
            o_body.append(f'<circle cx="{x0+22}" cy="{y+24}" r="5" fill="{col}"><animate attributeName="opacity" values="0.35;1;0.35" dur="3s" repeatCount="indefinite" begin="-{(r+j)*0.5:.1f}s"/></circle>')
            o_body.append(f'<text x="{x0+36}" y="{y+29}" fill="{col}" font-size="14" font-weight="bold" {FONT}>{title}</text>')
            for ri, row in enumerate(rows):
                cx = x0 + 16
                cyy = y + HEAD + ri * (CH + CG)
                for ci, (chip, w) in enumerate(row):
                    o_body.append(f'<rect x="{cx:.1f}" y="{cyy}" width="{w:.1f}" height="{CH}" rx="13" fill="{col}" fill-opacity="0.10" stroke="{col}" stroke-opacity="0.55">'
                                  f'<animate attributeName="stroke-opacity" values="0.35;0.9;0.35" dur="{4+(ci+ri)%3}s" repeatCount="indefinite" begin="-{(ci*0.7+ri):.1f}s"/></rect>')
                    o_body.append(f'<text x="{cx+w/2:.1f}" y="{cyy+17}" text-anchor="middle" fill="#e2e8f0" font-size="12" {FONT}>{chip}</text>')
                    cx += w + CG
        y += h + GAP
    H = int(y - GAP + PAD)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
           f'<rect width="{W}" height="{H}" rx="12" fill="#070d1d"/>'] + o_body + ['</svg>']
    open("assets/skills-cards.svg", "w", encoding="utf-8").write("\n".join(out))


hero(); skills(); print("assets generated")