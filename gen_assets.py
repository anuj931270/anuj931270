"""Generates assets/hero-orbit.svg and assets/skills.svg.
Edit the CONFIG block, run:  python gen_assets.py
"""
import random

# ================= CONFIG: EDIT THIS =================
NAME = "Anuj"
TITLE = "Data Scientist &amp; AI/ML Engineer | LLMs · RAG · MLOps"
TAGLINE = "Turning messy data into models that ship."
CORE = "AI/ML"

# (ring radius-x, radius-y, color, seconds per lap, direction, [skills])
ORBITS = [
    (130, 62, "#38bdf8", 28, 1,  ["Python", "PyTorch", "TensorFlow", "Scikit-learn"]),
    (235, 108, "#a78bfa", 46, -1, ["LLMs", "LangChain", "RAG", "HuggingFace", "NLP"]),
    (345, 150, "#34d399", 70, 1,  ["SQL", "Docker", "AWS", "FastAPI", "MLflow", "Airflow"]),
]

SKILLS = [  # (label, color, text)  -> keep text under ~78 chars
    ("ML / DL",     "#38bdf8", "Scikit-learn · XGBoost · PyTorch · TensorFlow · Keras · Feature Engineering"),
    ("GEN AI / LLM","#a78bfa", "LLMs · RAG · LangChain · LlamaIndex · HuggingFace · Fine-tuning · Agents"),
    ("NLP / CV",    "#f472b6", "Transformers · BERT · spaCy · OpenCV · YOLO · Embeddings · FAISS"),
    ("DATA",        "#34d399", "Python · SQL · Pandas · NumPy · PySpark · Airflow · ETL · Statistics"),
    ("MLOPS",       "#fb923c", "Docker · MLflow · FastAPI · Git · GitHub Actions · DVC · CI/CD"),
    ("CLOUD",       "#facc15", "AWS (S3, EC2, SageMaker) · GCP Vertex AI · Azure ML"),
    ("VIZ / BI",    "#f87171", "Power BI · Tableau · Matplotlib · Plotly · Streamlit · A/B Testing"),
]
# =====================================================

FONT = "font-family=\"'Courier New', Consolas, monospace\""


def hero():
    W, H, cx, cy = 900, 540, 450, 275
    random.seed(7)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    o.append(f'''<defs>
<radialGradient id="bg" cx="50%" cy="50%" r="75%"><stop offset="0" stop-color="#0b1b2b"/><stop offset="1" stop-color="#03070d"/></radialGradient>
<radialGradient id="core" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#bfe9ff"/><stop offset="0.45" stop-color="#2cb1ff"/><stop offset="1" stop-color="#0a5fa8"/></radialGradient>
<linearGradient id="comet" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#f0abfc" stop-opacity="0"/><stop offset="1" stop-color="#f0abfc"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="{W}" height="{H}" rx="6" fill="url(#bg)"/>''')

    for _ in range(70):  # twinkling stars
        x, y = random.randint(8, W - 8), random.randint(8, H - 8)
        r = random.choice([0.8, 1, 1.3])
        d = random.uniform(2, 6)
        o.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#cfe8ff"><animate attributeName="opacity" values="0.15;1;0.15" dur="{d:.1f}s" repeatCount="indefinite" begin="-{random.uniform(0,5):.1f}s"/></circle>')

    # shooting stars
    for i, (y0, dur, delay) in enumerate([(60, 7, 0), (300, 9, 4)]):
        o.append(f'<g opacity="0.9"><line x1="-90" y1="0" x2="0" y2="40" stroke="url(#comet)" stroke-width="2.5" stroke-linecap="round"/>'
                 f'<animateTransform attributeName="transform" type="translate" values="-100,{y0}; 1000,{y0+420}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/></g>')

    o.append(f'<text x="{cx}" y="52" text-anchor="middle" fill="#fff" font-size="32" font-weight="bold" {FONT}>{NAME}</text>')
    o.append(f'<text x="{cx}" y="82" text-anchor="middle" fill="#5cc8ff" font-size="15" {FONT}>{TITLE}</text>')

    for rx, ry, col, lap, direction, skills in ORBITS:  # rings
        o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{col}" stroke-opacity="0.28" stroke-width="1.2"/>')

    for rx, ry, col, lap, direction, skills in ORBITS:  # planets
        sweep = 0 if direction == 1 else 1
        path = (f"M{cx-rx},{cy} a{rx},{ry} 0 1,{sweep} {2*rx},0 a{rx},{ry} 0 1,{sweep} {-2*rx},0")
        n = len(skills)
        for i, s in enumerate(skills):
            off = lap * i / n
            o.append(f'<g filter="url(#glow)"><circle r="6" fill="{col}"/><text x="11" y="4" fill="{col}" font-size="13" {FONT}>{s}</text>'
                     f'<animateMotion dur="{lap}s" repeatCount="indefinite" begin="-{off:.1f}s" path="{path}"/></g>')

    o.append(f'<circle cx="{cx}" cy="{cy}" r="38" fill="url(#core)" filter="url(#glow)"><animate attributeName="r" values="36;40;36" dur="4s" repeatCount="indefinite"/></circle>')
    o.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" fill="#04243d" font-size="15" font-weight="bold" {FONT}>{CORE}</text>')
    o.append(f'<text x="{cx}" y="{H-28}" text-anchor="middle" fill="#8aa0b4" font-size="14" font-style="italic" {FONT}>"{TAGLINE}"</text>')
    o.append('</svg>')
    open("assets/hero-orbit.svg", "w", encoding="utf-8").write("\n".join(o))


def skills():
    row, top, W = 46, 24, 900
    H = top + row * len(SKILLS) + 20
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    o.append(f'<rect width="{W}" height="{H}" rx="10" fill="#0b1220"/>')
    o.append(f'<line x1="34" y1="{top}" x2="34" y2="{H-20}" stroke="#1f2d44" stroke-width="2"/>')
    for i, (lab, col, txt) in enumerate(SKILLS):
        y = top + i * row + 18
        o.append(f'<circle cx="34" cy="{y}" r="5" fill="{col}"><animate attributeName="opacity" values="0.4;1;0.4" dur="{3+i*0.4:.1f}s" repeatCount="indefinite"/></circle>')
        o.append(f'<rect x="58" y="{y-16}" width="150" height="32" rx="16" fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-width="1.3"/>')
        o.append(f'<text x="133" y="{y+5}" text-anchor="middle" fill="{col}" font-size="13" {FONT}>{lab}</text>')
        o.append(f'<text x="226" y="{y+5}" fill="#dbe7f5" font-size="13" {FONT}>{txt}</text>')
    o.append('</svg>')
    open("assets/skills.svg", "w", encoding="utf-8").write("\n".join(o))


hero(); skills(); print("assets generated")
